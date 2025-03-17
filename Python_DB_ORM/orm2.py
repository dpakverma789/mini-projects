import os
import platform
import sys
PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(PROJECT_DIRECTORY,'requirements.txt')
root_dir = os.path.dirname(PROJECT_DIRECTORY)
sys.path.insert(0, root_dir)

def install_requirements(file=None):
    return os.system(f'pip install -r {file}')

def remove_requirements(file=None):
    if os.path.isfile(file):
        return os.system(f'pip uninstall -y -r {file}')
    return False

try:
    import psycopg2
    from dotenv import load_dotenv
    from tabulate import tabulate
except ModuleNotFoundError:
    try:
        if not os.path.isfile(REQUIREMENTS_FILE):
            raise FileNotFoundError
        install_requirements(REQUIREMENTS_FILE)
    except FileNotFoundError:
        os.system('python -m pip install --upgrade pip')
        db = 'psycopg2' if platform.system() == 'Windows' else 'psycopg2-binary'
        for pack in (db, 'python-dotenv', 'tabulate'):
            os.system(f'pip install {pack}')
        import psycopg2
        from dotenv import load_dotenv
        from tabulate import tabulate
    finally:
        os.system('pip freeze > requirements.txt')



def validate_mandatory_fields(**kwargs):
    result = True
    required_fields = kwargs.get('field_list')
    for fields in required_fields:
        if not kwargs.get(fields, False):
            print(f'Missing Mandatory Keys: {fields}')
            result = False
    return result

def is_database_exist(**kwargs):
    """
    parameter: kwargs
    functionality: checks if database exist or not
    return: True/False
    """
    database_name = kwargs.get('db_name')
    db_cursor = kwargs.get('db_cursor')
    if database_name:
        try:
            sql_database = f"SELECT 1 FROM pg_database WHERE datname = '{database_name}'"
            db_cursor.execute(sql_database)
            sql_table_exist = db_cursor.fetchall()
            if not bool(sql_table_exist):
                return False
            return True
        except Exception as error:
            print(error)
    return False

def is_table_exist(**kwargs):
    """
    parameter: kwargs
    functionality: checks if table exist or not
    return: True/False
    """
    table_name = kwargs.get('table_name')
    db_cursor = kwargs.get('db_cursor')
    if table_name:
        try:
            sql_table = f"SELECT count(*) FROM information_schema.tables WHERE table_schema = 'public' AND table_name = '{table_name}'"
            db_cursor.execute(sql_table)
            sql_table_exist = db_cursor.fetchall()
            if not bool(sql_table_exist[0][0]):
                return False
            return True
        except Exception as error:
            print(error)
    return False

def get_database_cursor(function):
    """
    parameter: function and kwargs
    functionality: make connection to the database
    return: database connection and cursor
    """
    def core_function(**kwargs):
        result = False
        try:
            load_dotenv()
            user = os.getenv("DEFAULT_USER")
            password = os.getenv("DEFAULT_PASSWORD")
            host = os.getenv("DEFAULT_HOST")
            db_name = os.getenv("DEFAULT_DATABASE")
            if not any((user,password,host,db_name)):
                print('Connection Parameter are not Found!')
                return False
            db_connection = psycopg2.connect(host=host, user=user, password=password, database=db_name)
            db_connection.autocommit = True
            db_cursor = db_connection.cursor()
            new_db_name = kwargs.get('db_name')
            if new_db_name:
                result = is_database_exist(db_name=new_db_name,db_cursor=db_cursor,db_connection=db_connection)
            if result:
                db_connection = psycopg2.connect(host=host, user=user, password=password,database=new_db_name)
                db_connection.autocommit = True
                db_cursor = db_connection.cursor()
            else:
                print(f'{new_db_name} NOT EXISTS, DEFAULT DATABASE IS POSTGRES')
            kwargs.update({'db_cursor': db_cursor, 'db_connection': db_connection, 'db_exists':result})
            return function(**kwargs)
        except Exception as error:
            print(error)
            return False
    return core_function

@get_database_cursor
def create_database(**kwargs):
    """
    parameter: kwargs
    functionality: create database
    return: True/False
    """
    database_name = kwargs.get('db_name')
    db_cursor = kwargs.get('db_cursor')
    db_connection = kwargs.get('db_connection')
    db_exists = kwargs.get('db_exists')
    if not db_exists and database_name:
        try:
            sql_database = f"CREATE DATABASE {database_name} WITH OWNER = 'postgres'"
            db_cursor.execute(sql_database)
            sql_database_exist = is_database_exist(db_name=database_name,db_cursor=db_cursor,db_connection=db_connection)
            if sql_database_exist:
                print('DATABASE CREATED...OK')
                return True
            return False
        except Exception as error:
            print(error)
            db_connection.rollback()
        finally:
            db_cursor.close()
            db_connection.close()

@get_database_cursor
def create_table(**kwargs):
    """
    parameter: kwargs
    functionality: create table
    return: True/False
    """
    db_connection = kwargs.get('db_connection')
    db_cursor = kwargs.get('db_cursor')
    table_name = kwargs.get('table_name')
    columns = kwargs.get('columns')  # mandatory
    try:
        if table_name:
            table_exist = is_table_exist(**kwargs)
            if table_exist:
                print(f'{table_name} Already exist!')
                return False
            if columns:
                sql_query = f"CREATE TABLE {table_name} (\n"
                for column_name, data_type in columns.items():
                    sql_query += f"{column_name} {data_type.upper()},\n"
                sql_query = sql_query.rstrip(",\n") + "\n);"
                db_cursor.execute(sql_query)
                table_exist = is_table_exist(**kwargs)
                if table_exist:
                    print(f'{table_name} TABLE CREATED...OK')
                    return True
                else:
                    print(f'{table_name} created failed')
                    return False
            print("columns={'column_name':'data_type'} Required!")
            return False
        print("table='table_name' Required!")
        return False
    except Exception as error:
        print(error)
        db_connection.rollback()
        return False
    finally:
        db_connection.close()
        db_cursor.close()

@get_database_cursor
def create_record(**kwargs):
    """
    parameter: kwargs
    functionality: insert record into database
    return: True/False
    """
    kwargs.update({'field_list':('table_name','values')})
    verified = validate_mandatory_fields(**kwargs)
    if not verified:
        return
    table_name = kwargs.get('table_name')
    vals = kwargs.get('values')
    db_connection = kwargs.get('db_connection')
    db_cursor = kwargs.get('db_cursor')
    try:
        table_exist = is_table_exist(**kwargs)
        if not table_exist:
            print('Table Do not Exist')
            return False
        if vals:
            columns = ','.join(vals.keys())
            input_data = ','.join(f"'{val}'" for val in vals.values())
            sql_query = f'insert into {table_name}({columns}) values({input_data})'
            db_cursor.execute(sql_query)
            rowcount = db_cursor.rowcount
            print(f'Record created {rowcount} ...OK')
            return rowcount
        else:
            print('\nExpect data for Insertion!')
            return False
    except Exception as error:
        print(error)
        db_connection.rollback()
    finally:
        db_connection.close()
        db_cursor.close()

@get_database_cursor
def update_record(**kwargs):
    """
    parameter: kwargs
    functionality: update record in database
    return: True/False
    """
    kwargs.update({'field_list':('table_name','values')})
    verified = validate_mandatory_fields(**kwargs)
    if not verified:
        return
    table_name = kwargs.get('table_name')  # mandatory
    vals = kwargs.get('values')  # mandatory
    where = kwargs.get('where', False)  # optional
    db_connection = kwargs.get('db_connection')
    db_cursor = kwargs.get('db_cursor')
    try:
        table_exist = is_table_exist(**kwargs)
        if not table_exist:
            print('Table Do not Exist')
            return False
        if vals:
            set_clause = ','.join(f'{key}={val}' for key, val in vals.items())
            sql_query = f'update {table_name} set {set_clause}'
            if where:
                sql_query = f'{sql_query} where {where}'
            db_cursor.execute(sql_query)
            rowcount = db_cursor.rowcount
            print(f'Record Updated {rowcount} ...OK')
            return rowcount
        else:
            print('\nExpect data for Insertion!')
            return False
    except Exception as error:
        print(error)
        db_connection.rollback()
    finally:
        db_connection.close()
        db_cursor.close()

@get_database_cursor
def delete_record(**kwargs):
    """
    parameter: kwargs
    functionality: delete record from database
    return: True/False
    """
    kwargs.update({'field_list':('table_name','where')})
    verified = validate_mandatory_fields(**kwargs)
    if not verified:
        return
    table_name = kwargs.get('table_name')
    where = kwargs.get('where', False)
    db_connection = kwargs.get('db_connection')
    db_cursor = kwargs.get('db_cursor')
    try:
        table_exist = is_table_exist(**kwargs)
        if not table_exist:
            print(f'{table_name} do not Exist')
            return False
        sql_query = f'delete from {table_name}'
        if where:
            sql_query = f'{sql_query} where {where}'
        else:
            print('\n\t\t\t======> WARNING <====== \nMissing where clause, '
                  'this will delete all record for the "%s"' % table_name)
            user_waring_flag = input("Are You Sure You want to delete All Records? (write: yes): ")
            if user_waring_flag == '' or user_waring_flag.strip() != 'yes':
                print('user didn\'t writen yes, aborting deletion')
                return False
        db_cursor.execute(sql_query)
        rowcount = db_cursor.rowcount
        print(f'Record Deleted {rowcount} ...OK')
        return rowcount
    except Exception as error:
        print(error)
        db_connection.rollback()
    finally:
        db_cursor.close()
        db_connection.close()

@get_database_cursor
def fetch_record(**kwargs):
    """
    params: kwargs
    function: show records from database
    return: records
    """
    info = {};data = []
    kwargs.update({'field_list':('table_name',)})
    verified = validate_mandatory_fields(**kwargs)
    if not verified:
        return
    table_name = kwargs.get('table_name')
    db_cursor = kwargs.get('db_cursor')
    db_connection = kwargs.get('db_connection')
    print_table = kwargs.get('print_table', False)
    where_clause = kwargs.get('where', False)
    order_by = kwargs.get('order_by', False)
    count = kwargs.get('count', False)
    try:
        table_exist = is_table_exist(**kwargs)
        if not table_exist:
            print('Table Do not Exist')
            return False
        sql_query = f'select * from {table_name}'
        if count:
            sql_query = f'select count(*) from {table_name}'
        if where_clause:
            sql_query = ' '.join((sql_query, f'where {where_clause}'))
        if order_by:
            sql_query = ' '.join((sql_query, f'order by {order_by}'))
        db_cursor.execute(sql_query)
        column_name_list = [desc[0] for desc in db_cursor.description]
        records = db_cursor.fetchall()
        if not records:
            print('\nNo Matching Record Found!!')
            return False
        for row in records:
            for column_name, value in zip(column_name_list, row):
                info.update({column_name: value})
            data.append(info)
            info = {}
        if print_table:
            print(tabulate(records, headers=column_name_list, tablefmt="grid"))
        return data
    except Exception as error:
        print(error)
        db_connection.rollback()
    finally:
        db_cursor.close()
        db_connection.close()


if __name__ == "__main__":
    # create_database(db_name="virtual_atm")
    # create_table(db_name='virtual_atm',table_name='customer_profile',columns={
    #         'account_number': 'INT',
    #         'first_name': 'VARCHAR(100)',
    #         'last_name': 'VARCHAR(100)',
    #         'pin': 'INT',
    #         'amount': 'INT',
    #     })
    # data = {'first_name': 'Test', 'last_name': 'kumar', 'account_number': 101, 'pin': 1324, 'amount': 2000}
    # create_record(db_name='virtual_atm',table_name='customer_profile', values=data)
    # data = {'pin': 4560}
    # update_record(db_name='virtual_atm',table_name='customer_profile', values=data, where='account_number=456')
    # delete_record(db_name="virtual_atm",table_name='customer_profile',where='account_number=102')
    fetch_record(db_name="virtual_atm",table_name='customer_profile',print_table=True)
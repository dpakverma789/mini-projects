import os
import platform
import random

# importing packages
try:
    import psycopg2
    from dotenv import load_dotenv
except ModuleNotFoundError:
    db = 'psycopg2' if platform.system() == 'Windows' else 'psycopg2-binary'
    for pack in (db, 'python-dotenv'):
        os.system(f'pip install {pack}')
    import psycopg2
    from dotenv import load_dotenv


def db_connection():
    load_dotenv()
    db_name = os.getenv("NAME")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST")
    mydb = psycopg2.connect(
        host=host,
        database=db_name,
        user=user,
        password=password
    )
    return mydb, mydb.cursor()


# updating database with new questions
def update_question(question, option_1, option_2, option_3, option_4, answer):
    try:
        mydb, database = db_connection()
        # ---- for postgres database ----
        sql_table = f"SELECT count(*) FROM information_schema.tables where table_name = 'questionbank_questionbank'"
        database.execute(sql_table)
        sql_table_exist = database.fetchall()
        # ----------------------------

        # if not is_database_exist:
        if not bool(sql_table_exist[0][0]):
            # ---- for postgres database ----
            sql_create_table = "CREATE TABLE questionbank_questionbank(id SERIAL PRIMARY KEY, question varchar(500)," \
                               "option_1 VARCHAR(200),option_2 VARCHAR(200)," \
                               "option_3 VARCHAR(200),option_4 VARCHAR(200),answer VARCHAR(200))"
            database.execute(sql_create_table)
            sql_values = (question, option_1, option_2, option_3, option_4, answer)
            sql_query = "insert into questionbank_questionbank(question,option_1,option_2," \
                        "option_3,option_4,answer) values {}".format(sql_values)
            # ----------------------------
            database.execute(sql_query)
        else:
            sql_values = (question, option_1, option_2, option_3, option_4, answer)
            # ---- for postgres database ----
            sql_query = "insert into questionbank_questionbank(question,option_1,option_2," \
                        "option_3,option_4,answer) values {}".format(sql_values)
            print("\n\t\t\tPlease wait Updating Question in QuestionBank!!")
            # ----------------------------
            database.execute(sql_query)
        print("\n\t\t\tUpdated Question in QuestionBank!!\n\n")
    except Exception as error:
        print(error)
    finally:
        mydb.commit()
        mydb.close()
    return


# fetching questions from database
def get_question():
    # ---- for postgres database ----
    from_table = 'from questionbank_questionbank'
    # ----------------------------
    point = 0
    incorrect_list = []
    mydb, database = db_connection()
    try:
        database.execute(f"select id {from_table}")
        question_ids = database.fetchall()
        ids = list(map(lambda x: x[0], question_ids))
        total_question = len(ids)
        while ids:
            question_id = random.choice(ids)
            database.execute(f"select * {from_table} where id = {question_id}")
            question = database.fetchall()
            if question:
                QUESNO = (11 - len(ids))
                question_data = {
                    QUESNO: question[0][1],
                    'A': question[0][2],
                    'B': question[0][3],
                    'C': question[0][4],
                    'D': question[0][5],
                }
                ANSKEY = [key for key, val in question_data.items() if val == question[0][6]][0]
                question_data.update({'ANS': ANSKEY})
                for key, val in question_data.items():
                    if key != 'ANS':
                        print(f'{key}: {val}')
                user_answer = input('\nEnter your answer: ').strip()
                ans_key = question_data.get('ANS')
                if user_answer in (ans_key, question_data.get(ans_key)):
                    point += 10
                else:
                    if user_answer not in ('exit', 'quit'):
                        incorrect_list.append(f'Q{QUESNO}:{user_answer}')
                if user_answer in ('exit', 'quit'):
                    break
            ids.remove(question_id)
            print("==="*20)
    except Exception as e:
        print(e)
    finally:
        mydb.commit()
        mydb.close()
    return point, total_question, incorrect_list


# collecting question and its details
def question_collection():
    question = input('Enter your Question? :')
    option_1 = input('Enter your option_1? :')
    option_2 = input('Enter your option_2? :')
    option_3 = input('Enter your option_3? :')
    option_4 = input('Enter your option_4? :')
    answer = input('Enter your answer? :')
    return update_question(question, option_1, option_2, option_3, option_4, answer)


# main thread
if __name__ == '__main__':
    try:
        choice = int(input("\nPRESS 1 FOR PLay Quiz  \t\t PRESS 2 FOR Update Question Bank: "))
        if choice == 1:
            name = input("\nEnter your name: ")
            print("\n\t\t\t===== WELCOME TO QUIZ GAME %s =====" % name.upper())
            print("\t\t\tTo quit type exit or quit")
            print("\t\t\tPlease wait loading the questions... \n")
            point, total, incorrect = get_question()
            print(f'\n\n\tWell Played "{name.upper()}" Your Score is "{point}" out of "{total*10}"')
            print(f'\n\tYour incorrect answers are {incorrect}')
            del point, total, incorrect
        elif choice == 2:
            number_of_question = int(input("Enter Number of Question to be Updated? :"))
            try:
                for _ in range(1, number_of_question+1):
                    question_collection()
                    # question_tuple = question_collection()
                    # update_question(*question_tuple)
                print("\n\t\t\tAll Questions are Updated!!\n\n")
            except Exception as error:
                print('\n\t\t\t\t QuestionBank Update Failed!!\n', error)
        else:
            print('\n\t\t\t\tOpps Invalid Selection !!\n')
    except:
        print('\n\t\t\t\tDatabase Connection Failed!!\n')


def syntax(*args):
    odoo_data_type = { 'c': 'Char', 'i': 'Integer', 'f': 'Float', 'd': 'date', 'dt': 'Datetime', 'bi': 'Binary',
                       's': 'Selection', 'b': 'Boolean', 'mo': 'Many2one', 'om': 'One2many', 'mm': 'Many2many' }
    variable, py_container, xml_container = args
    variable_name, variable_type = variable.split(".")
    line_string = ' '.join(variable_name.split("_")).title()
    if variable_type == 'mo':
        variable_name = f'{variable_name}_id'
    if variable_type in ('om', 'mm'):
        variable_name = f'{variable_name}_ids'
    partial_string = f"{variable_name} = fields.{odoo_data_type[variable_type]}"
    line_format = {
        'mo': f"{partial_string}(comodel_name='your.model_name', string='{line_string}')",
        'om': f"{partial_string}(comodel_name='your.model_name',inverse_name='', string='{line_string}')",
        's': f"{partial_string}([('option_1','Option 1'),('option_2','Option 2')], string='{line_string}', default='option_1')",
        'mm': f"{partial_string}(comodel_name='your.model_name', 'TableName1_TableName2_rel',"
              f" 'table1_column_id', 'table2_column_id', string='{line_string}')"
    }
    py_line = line_format.get(variable_type, f"{partial_string}(string='{line_string}')")
    xml_line = f'<field name="{variable_name}"/>'
    if variable_type == 'mm':
        xml_line =  f'<field name="{variable_name}" widget="many2many_tags"/>'
    if variable_type == 'bi':
        xml_line = f'<field name="{variable_name}" widget="image" class="oe_avatar"/>'
    py_container.append(py_line)
    xml_container.append(xml_line)
    return py_container, xml_container


def odoo_syntax_generator(variable_tuple=None):
    py_container = []
    xml_container = []
    if variable_tuple:
        for variable in variable_tuple:
            py_container, xml_container = syntax(variable, py_container, xml_container)
        print('\n\n#==== Odoo Python Syntax ====\n')
        [print(line) for line in py_container]
        print('\n\n#==== Odoo xml Syntax ====\n')
        [print(line) for line in xml_container]
        del py_container, xml_container
    else:
        print('\n\n==== No Variable List is Given ====')
    return


variable_list = (
    'name.c',
    'age.i',
    'salary.f',
    'date_of_birth.d',
    'date_of_joining.dt',
    'profile_image.bi',
    'gender.s',
    'is_employee.b',
    'project_manager.mo',
    'employee_assets.om',
    'projects_involves.mm'
)

odoo_syntax_generator(variable_list)
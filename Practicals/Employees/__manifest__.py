{
    'name': 'Employee Data',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Employee Details',
    'description': 'This module display all details of employees',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',
    ],
    'installable': True,
    'application': True,
}
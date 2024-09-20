{
    'name': 'Students',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'A Student List',
    'description': 'This module displays Students.',
    'depends': ['base'],  # Add any necessary dependencies here
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
    ],
    'installable': True,
    'application': True,
}

{
    'name': 'currency nbrb',
    'version': '0.0.1',
    'category': 'Accounting',
    'description': 'module fetches currency nbrb',
    'sequence': '-100',
    'author': 'Administriva',
    'license': 'LGPL-3',
    'depends': [
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/currency_action.xml',
    ],
    'application': True,
}

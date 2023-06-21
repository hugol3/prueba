{
    'name': "Mi Modulo",
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Track groceeries to be delivered',
    'depends': [
        'base'
    ],
    'author': "Author Name",
    'category': 'Category',
    'description': """
        Track groceeries to be delivered
    """,
    # data files always loaded at installation
    'data': ['views/inventario.xml'],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets':{
        'web.assets_backend': [
           
        ]
    },
}
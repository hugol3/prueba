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
    'images' : ['images/placeholder.png'],
    # data files always loaded at installation
    'data': [
        'views/menu.xml',
        'views/inventario.xml',
        'views/crear.xml',


    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets':{
        'web.assets_backend': [
           
        ]
    },
    'icon': 'account_dashboard_onboarding_bg.jpg',
    'menu': {
        'name': 'Menu',
        'sequence': 100
    }
}
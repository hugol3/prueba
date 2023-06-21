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
        'views/bienvenida.xml',
        # CRUD VIEWS
        'views/ordenes_view.xml',
        'views/productos_view.xml',
        'views/beneficiarios_view.xml',
        #'views/inventario.xml',
        'views/crear_usuario.xml',
        'views/crear_inventario.xml',
        'views/actualizar.xml',
        #'views/eliminar.xml',
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
    'menu': {
        'name': 'Menu',
        'sequence': 100
    }
}
{
    'name':        'Queue Management',
    'version':     '17.0.0.1',
    'summary':     'Module for queue appointments.',
    'description': 'Remake of the original Queue Management.',
    'category':    'Administration',
    'icon':        '/queue_management/static/description/icon.png',
    'author':      'Bruno Bonassi Montico',
    'license':     'AGPL-3',
    'depends':     ['base'],
    'installable': True,
    'auto_install':False,

    'data':[
        # menus
        'views/menu_root.xml',
        'views/menus_customer_service.xml',
        'views/menus_module_config.xml',

        # tree
        'views/tree_customer_service.xml',
    ]
}
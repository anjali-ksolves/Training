{
    'name': 'Device Management',
    'author': 'Anjali',
    'summary': 'Device Management System',
    'description': """Device Management System""",
    'depends': ['base', 'hr', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/device_management_settings.xml',
        'views/menu.xml',
        'views/device_type.xml',
        'views/employee.xml',
        'views/device_assignment.xml',
        'views/device_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'device_management/static/src/xml/customer_rating.xml',
            'device_management/static/src/xml/device_button.xml',
            'device_management/static/src/scss/customer_rating.scss',
            'device_management/static/src/js/customer_rating.js',
            'device_management/static/src/js/device_button.js',

        ]
    },
    'installable': True,
    'application': True,
    'sequence': -100,
}

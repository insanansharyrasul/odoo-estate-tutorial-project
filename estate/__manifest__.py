{
    'name' : 'Estate',
    'version': '1.0',
    'depends': ['base', 'website'],
    'author': "Insan Anshary R.",
    'category': 'Real Estate/Brokerage',
    'description': "",
    'Description text':"",
    'license' : 'LGPL-3',
    'data' : [
        'security/ir.model.access.csv',
        'views/estate_property_tag_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_views.xml',
        'views/res_users_views.xml',
        'views/estate_menus.xml',
        'views/page.xml',
        'views/test.xml',
        'views/snippets/snippet.xml',
        'views/snippets/thing.xml',
        'data/master_data.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'estate/static/src/scss/main.scss'
        ]
    },
    # 'demo' : [
    #     'demo/demo_data.xml',
    #     'demo/estate_property_data.csv'
    # ],
    'application' : True,
}
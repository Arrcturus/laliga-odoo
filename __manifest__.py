# -*- coding: utf-8 -*-
{
    'name': "laliga",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Arthur Bringhenti and Pablo Castro",
    'website': "https://github.com/Arrcturus/laliga-odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/league.xml',
        'views/team.xml',
        'views/stadium.xml',
        'views/member.xml',
        'views/staff.xml',
        'views/employment.xml',
        'views/menu.xml',
        # EL MENÚ SIEMPRE VA ABAJO DEL TODO

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

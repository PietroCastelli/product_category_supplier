# -*- coding: utf-8 -*-
{
    'name': "product_category_supplier",

    'summary': """
        extender to implement vender and add to the group""",


    'author': "STeSI",
    'website': "https://www.stesi.eu",


    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inventory_product.xml',

    ],

}

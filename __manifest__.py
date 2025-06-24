# -*- coding: utf-8 -*-

{
    'name': 'Purchase Category',
    'version': '1.0',
    'category': 'Inventory/Purchase',
    'summary': 'Categorías para ordenes de compra',
    'depends': ['purchase'],
    'data': [
        'security/purchase_security.xml',
        'security/ir.model.access.csv',
        'views/purchase_views.xml',
        'views/res_user_views.xml',
        'data/server_acction.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

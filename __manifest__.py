# -*- coding: utf-8 -*-
{
    'name': 'Product Auto Code',
    'version': '0.1.0',
    'author': 'Benlever Pvt Ltd',
    'company': 'Benelever Pvt Ltd',
    'website': 'https://www.benlever.com',
    'maintainer': 'Benlever Pvt Ltd',
    'category': 'Sales/Sales',
    'sequence': 6,
    'summary': 'Generates Product Code automatically',
    'description': """
Sequential generation of product code
""",
    'depends': ['product'],
    'data': [
        'security/ir.sequence.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

{
    "name": "HLM Studio Rebuild (POS + Delivery Fields)",
    "version": "19.0.1.0.0",
    "category": "Hidden/Tools",
    "summary": "Rebuilds x_studio custom fields and server actions from Odoo Online",
    "description": "Rebuilds HLM Studio customizations from production: POS cashier field, POS DO to invoice delivery fields automation, POS session to invoice employee automation.",
    "author": "HLM IT",
    "license": "LGPL-3",
    "depends": ["point_of_sale", "account", "stock"],
    "data": [
        "views/account_move_views.xml",
    ],
    "installable": True,
    "application": False,
}

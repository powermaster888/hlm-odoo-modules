{
    "name": "HLM Security & Access Control",
    "version": "19.0.1.0.0",
    "category": "Hidden/Tools",
    "summary": "HLM custom user groups, menu visibility, and record rules",
    "description": """
Healthy Living Medical Supplies custom security structure.
Rebuilds the 16 custom groups from Odoo Online production:
- Menu visibility switches (Show Menu - Master/User/Salesperson, per-app Show menus)
- Business rules (HLM Cost Visibility, Mask Non-local Vendor, Hide Stock Report Buttons)
- Vendor bills partner button access
    """,
    "author": "HLM IT",
    "license": "LGPL-3",
    "depends": ["base", "account", "stock", "point_of_sale", "sale_management", "purchase"],
    "data": [
        "security/hlm_security_groups.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}

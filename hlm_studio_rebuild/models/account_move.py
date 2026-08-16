from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    hlm_pos_cashier = fields.Char(
        string="POS Cashier",
        compute="_compute_hlm_pos_cashier",
        store=True,
        help="Name of the POS cashier who created this invoice (rebuilt from x_studio field)",
    )
    hlm_delivery_origin = fields.Char(
        string="Delivery Origin",
        compute="_compute_hlm_delivery_origin",
        store=True,
        help="Source delivery order reference linked to this invoice",
    )

    @api.depends("pos_order_ids")
    def _compute_hlm_pos_cashier(self):
        for move in self:
            if move.pos_order_ids:
                order = move.pos_order_ids[0]
                move.hlm_pos_cashier = order.employee_id.name or order.user_id.name or ""
            else:
                move.hlm_pos_cashier = ""

    @api.depends("pos_order_ids")
    def _compute_hlm_delivery_origin(self):
        for move in self:
            if move.pos_order_ids:
                order = move.pos_order_ids[0]
                pickings = order.picking_ids.filtered(lambda p: p.picking_type_code == "outgoing")
                move.hlm_delivery_origin = ", ".join(p.name for p in pickings)
            else:
                move.hlm_delivery_origin = ""

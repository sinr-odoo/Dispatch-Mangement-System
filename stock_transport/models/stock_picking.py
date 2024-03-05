from odoo import api,fields, models

class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume = fields.Float(compute="_compute_volume")

    @api.depends('move_line_ids')
    def _compute_volume(self):
        for record in self:
            volume = 0
            if(record.move_line_ids):
                for products in record.move_line_ids:
                    volume += products.product_id.volume * products.quantity
                record.volume = volume
            else:
                record.volume = 0
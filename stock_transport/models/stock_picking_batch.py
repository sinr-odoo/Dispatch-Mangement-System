from odoo import api,fields, models

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"
    dock = fields.Many2one('stock.transport.dock')
    vehicle = fields.Many2one('fleet.vehicle', placeholder="Third Party Provider")
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category', placeholder="eg. Semi-truck")
    weight = fields.Float(compute="_compute_weight", store=True)
    volume = fields.Float(compute="_compute_volume", store=True)
    no_of_transfers = fields.Integer(compute="_compute_no_of_transfers", store=True)
    no_of_lines = fields.Integer(compute="_compute_no_of_lines", store=True)

    @api.depends('vehicle_category_id', 'move_line_ids')
    def _compute_weight(self):
        for record in self:
            if(record.vehicle_category_id):
                product_weight = 0
                for products in record.move_line_ids:
                    product_weight += products.product_id.weight * products.quantity
                record.weight = (product_weight / record.vehicle_category_id.max_weight) * 100
            else:
                record.weight = 0.0
    
    @api.depends('vehicle_category_id', 'move_line_ids')
    def _compute_volume(self):
        for record in self:
            if(record.vehicle_category_id):
                product_volume = 0
                for products in record.move_line_ids:
                    product_volume += products.product_id.volume * products.quantity
                record.volume = (product_volume / record.vehicle_category_id.max_volume) * 100
            else:
                record.volume = 0.0


    @api.depends('picking_ids')
    def _compute_no_of_transfers(self):
        for record in self:
            record.no_of_transfers = len(record.picking_ids)
    
    @api.depends('move_line_ids')
    def _compute_no_of_lines(self):
        for record in self:
            record.no_of_lines = len(record.move_line_ids)

    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.name}: {record.weight} kg, {record.volume} m2"
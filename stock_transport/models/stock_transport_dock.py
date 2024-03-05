from odoo import fields, models

class Dock(models.Model):
    _name = "stock.transport.dock"
    _description = "Dock"

    name = fields.Char()
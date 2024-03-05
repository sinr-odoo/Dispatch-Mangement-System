from odoo import fields, models

class Dock(models.Model):
    _name = "stock.transport.dock"
    _description = "Dock station for stocks."

    name = fields.Char()
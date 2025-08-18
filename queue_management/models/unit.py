from odoo import fields, models

class Unit(models.Model):
    _name = "unit.model"
    _description = "model for units"

    name = fields.Char(string="Unit Name", required=True)
    description = fields.Text(string="description")

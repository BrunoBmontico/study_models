from odoo import fields, models

class Group(models.Model):
    _name = "group.model"
    _description = "model for Groups"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="description")
    unit_id = fields.One2many(comodel_name='unit.model', string="Unit")
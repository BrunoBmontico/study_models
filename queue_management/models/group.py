from odoo import fields, models

class Group(models.Model):
    _name = "group.model"
    _description = "model for Groups"

    name = fields.Char(string="Name", required=True)
    unit_id = fields.One2many(comodel_name='unit.model', string="Unit")
    code_amount = fields.Int(string="Code Amount", required=True)
    description = fields.Text(string="Description")
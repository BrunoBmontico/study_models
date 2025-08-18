from odoo import fields, models

class Group(models.Model):
    _name = "group.model"
    _description = "model for Groups"

    name = fields.Char(string="Group Name", required=True)
    description = fields.Text(string="description")
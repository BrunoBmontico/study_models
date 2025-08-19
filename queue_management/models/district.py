from odoo import fields, models

class District(models.Model):
    _name = "district.model"
    _description = "model for districts"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
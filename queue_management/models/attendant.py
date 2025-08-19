from odoo import fields, models

class Attendant(models.Model):
    _name = "attendant.model"
    _description = "model for attendants"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
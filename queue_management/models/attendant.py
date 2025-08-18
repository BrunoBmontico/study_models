from odoo import fields, models

class Attendant(models.Model):
    _name = "Attendant.model"
    _description = "model for attendants"

    name = fields.Char(string="Attendant Name", required=True)
    description = fields.Text(string="Description")
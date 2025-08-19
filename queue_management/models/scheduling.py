from odoo import fields, models

class Scheduling(models.Model):
    _name = "scheduling.model"
    _description = "model for appointments"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="description")

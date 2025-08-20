from odoo import fields, models

class Attendant(models.Model):
    _name = "attendant.model"
    _description = "model for attendants"

    name = fields.Char(string="Name", required=True)

    scheduling_ids = fields.One2many(
        comodel_name="scheduling.model",
        inverse_name="attendant_id",
        string="Appointments"
    )
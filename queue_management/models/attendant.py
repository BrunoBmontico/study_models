from odoo import fields, models

class Attendant(models.Model):
    _name = "queue.attendant"
    _description = "model for attendants"

    name = fields.Char(string="Name", required=True)

    scheduling_ids = fields.One2many(
        comodel_name="queue.scheduling",
        inverse_name="attendant_id",
        string="Appointments"
    )
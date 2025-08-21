from odoo import fields, models

class Attendant(models.Model):
    _name = "queue.attendant"
    _description = "model for attendants"

    name = fields.Char(string="Name", required=True)

    unit_ids = fields.Many2many(
        comodel_name="queue.unit",
        relation="unit_attendant_rel",
        column1="attendant_id",
        column2="unit_id",
        string="Units"
    )

    group_ids = fields.Many2many(
        comodel_name="queue.group",
        relation="group_attendant_rel",
        column1="attendant_id",
        column2="group_id",
        string="Groups"
    )

    appointment_ids = fields.One2many(
        comodel_name="queue.appointment",
        inverse_name="attendant_id",
        string="Appointments"
    )
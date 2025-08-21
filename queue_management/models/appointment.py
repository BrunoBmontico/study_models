from odoo import fields, models

class Appointment(models.Model):
    _name = "queue.appointment"
    _description = "model for appointments"

    applicant = fields.Char(string="Applicant", required=True)
    appointment_date = fields.Date(string="Appointment Date", required=True)

    unit_id = fields.Many2one(
        comodel_name="queue.unit",
        string="Unit"
    )
    
    group_id = fields.Many2one(
        comodel_name="queue.group",
        string="Group"
    )
    
    attendant_id = fields.Many2one(
        comodel_name="queue.attendant",
        string="Attendant"
    )

from odoo import fields, models

class Scheduling(models.Model):
    _name = "queue.scheduling"
    _description = "model for appointments"

    applicant = fields.Char(string="Applicant", required=True)
    scheduling_date = fields.Date(string="Scheduling Date", required=True)

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

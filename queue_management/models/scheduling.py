from odoo import fields, models

class Scheduling(models.Model):
    _name = "scheduling.model"
    _description = "model for appointments"

    applicant = fields.Char(string="Applicant", required=True)
    scheduling_date = fields.Date(string="Scheduling Date", required=True)

    unit_id = fields.Many2one(
        comodel_name="unit.model",
        string="Unit"
        )
    
    group_id = fields.Many2one(
        comodel_name="group.model",
        string="Group"
    )
    
    attendant_id = fields.Many2one(
        comodel_name="attendant.model",
        string="Attendant"
    )

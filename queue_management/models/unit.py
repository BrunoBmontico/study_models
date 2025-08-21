from odoo import fields, models

class Unit(models.Model):
    _name = "queue.unit"
    _description = "model for units"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")

    district_ids = fields.Many2many(
        comodel_name="queue.district",
        relation="unit_district_rel",
        column1="unit_id",
        column2="district_id",
        string="Districts"
    )
    
    group_ids = fields.One2many(
        comodel_name="queue.group", 
        inverse_name="unit_id", 
        string="Groups"
    )
    
    attendant_ids = fields.Many2many(
        comodel_name="queue.attendant",
        relation="unit_attendant_rel",
        column1="unit_id",
        column2="attendant_id",
        string="Attendants"
    )
    
    scheduling_ids = fields.One2many(
        comodel_name="queue.scheduling",
        inverse_name="unit_id",
        string="Appointments"
    )

    
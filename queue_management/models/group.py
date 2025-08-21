from odoo import fields, models

class Prefix(models.model):
    _name = "queue.Prefix.group"
    _description = "Model for prefix codes"

    name = fields.Char(string="Name", required=True)
    prefix = fields.Char(string="Prefix", required=True)
    increment = fields.Int(string="Increment", default=1, required=True)
    digit = fields.Int(string="Digit", required=True)
    
    group_ids = fields.One2many(
        comodel_name="queue.group",
        inverse_name="prefix_id",
        string="Groups"
    )
    
class Group(models.Model):
    _name = "queue.group"
    _description = "Model for Groups"

    name = fields.Char(string="Name", required=True)
    code_amount = fields.Int(string="Code Amount", required=True)
    description = fields.Text(string="Description")

    unit_id = fields.Many2one(
        comodel_name='queue.unit',
        string="Unit"
    )

    prefix_id = fields.Many2one(
        comodel_name='queue.Prefix.group',
        string="Prefix",
        required=True
    )
    
    attendant_ids = fields.Many2many(
        comodel_name="queue.attendant",
        relation="group_attendant_rel",
        column1="group_id",
        column2="attendant_id",
        string="Attendants"
    )
    
    scheduling_ids = fields.One2many(
        comodel_name="queue.scheduling",
        inverse_name="unit_id",
        string="Appointments"
    )

from odoo import fields, models

class Prefix(models.model):
    _name = "Prefix.group.model"
    _description = "Model for prefix codes"

    name = fields.Char(string="Name", required=True)
    prefix = fields.Char(string="Prefix", required=True)
    increment = fields.Int(string="Increment", default=1, required=True)
    digit = fields.Int(string="Digit", required=True)
    
    group_ids = fields.One2many(
        comodel_name="group.model",
        inverse_name="prefix_id",
        string="Groups"
    )
    
class Group(models.Model):
    _name = "group.model"
    _description = "Model for Groups"

    name = fields.Char(string="Name", required=True)
    code_amount = fields.Int(string="Code Amount", required=True)
    description = fields.Text(string="Description")

    unit_id = fields.Many2one(
        comodel_name='unit.model',
        string="Unit"
    )

    prefix_id = fields.Many2one(
        comodel_name='prefix.group.model',
        string="Prefix",
        required=True
    )
    
    attendant_ids = fields.Many2many(
        comodel_name="attendant.model",
        relation="group_attendant_rel",
        column1="group_id",
        column2="attendant_id",
        string="Attendants"
    )
    
    scheduling_ids = fields.One2many(
        comodel_name="scheduling.model",
        inverse_name="unit_id",
        string="Appointments"
    )

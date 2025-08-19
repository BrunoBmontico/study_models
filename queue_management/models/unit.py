from odoo import fields, models

class Unit(models.Model):
    _name = "unit.model"
    _description = "model for units"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    district_ids = fields.Many2many(comodel_name="district.model", relation="unit_district_rel", column1="unit_id", column2="district_id", string="Districts")
    group_ids = fields.One2many(comodel_name="group.model", inverse_name="Unit_id", string="Groups")
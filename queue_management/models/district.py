from odoo import fields, models

class District(models.Model):
    _name = "queue.district"
    _description = "model for districts"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")

    cep_ids = fields.Many2many(
        comodel_name="queue.cep",
        relation="cep_district_rel",
        column1="district_id",
        column2="cep_id", 
        string="Districts"
    )

    unit_ids = fields.Many2many(
        comodel_name="queue.unit",
        relation="unit_district_rel",
        column1="district_id",
        column2="unit_id",
        string="Units"
    )
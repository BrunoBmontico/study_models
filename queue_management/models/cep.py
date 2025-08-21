from odoo import fields, models

class Cep(models.Model):
    _name = "queue.cep"
    _description = "model for CEPs"

    name = fields.Char(string="CEP", required=True)

    district_ids = fields.Many2many(
        comodel_name="queue.district",
        relation="cep_district_rel",
        column1="cep_id",
        column2="district_id", 
        string="Districts"
    )

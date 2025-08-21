from odoo import fields, models

class District(models.Model):
    _name = "queue.district"
    _description = "model for districts"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
from odoo import models, fields, api


class Employment(models.Model):
    _name = 'league.employment'
    _description = 'Staff employment'

    name = fields.Char(string="Name", required=True)
    min_wage = fields.Monetary('Minimun Wage')

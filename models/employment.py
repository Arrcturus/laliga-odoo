from odoo import models, fields, api


class Employment(models.Model):
    _name = 'league.employment'
    _description = 'Employment'

    name = fields.Char(String='Employment name', required=True)
    minWage = fields.Monetary('Minimun wage')

from odoo import models, fields, api


models
class employment(models.Model):
    _name = 'league.employment'
    _description = 'Employment'

    name = fields.Char(String='Employment name', required=True)
    minWage = fields.Monetary('Minimun wage')

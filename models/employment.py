from odoo import models, fields, api


class employment(models.Model):
    _name = 'league.employment'
    _description = 'Employment'

    name = fields.Char(String='Employment name')
    minWage = fields.Monetary('Minimun wage')
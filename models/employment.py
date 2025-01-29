from odoo import models, fields, api


class Employment(models.Model):
    _name = 'laliga.employment'
    _description = 'Employment'

    name = fields.Char(String='Employment name', required=True)
    min_wage = fields.Monetary('Minimun Wage', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))

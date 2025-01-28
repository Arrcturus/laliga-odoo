from odoo import models, fields, api


class Employee(models.Model):
    _name = 'league.employee'
    _description = 'Employee'
    _inherit = 'league.person'

    wage = fields.Monetary('Wage', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))
    #TODO img
    contractStart = fields.Date(string='Contract start date', required=True)
    contractEnd = fields.Date(string='Contract end date', required=True) 
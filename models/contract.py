from odoo import models, fields, api


class Contract(models.Model):
    _name = 'laliga.contract'
    _description = 'Contract'

    name = fields.Char(string="Contract")
    wage = fields.Monetary('Wage', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))
    start = fields.Date('Start')
    end = fields.Date('End')

    #player_id = fields.Many2one('laliga.player', string='employee')
    staff_id = fields.Many2one('laliga.staff', string='employee')
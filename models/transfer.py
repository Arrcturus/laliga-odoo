from odoo import models, fields, api


class Transfer(models.Model):
    _name = 'laliga.transfer'
    _description = 'Player transfers'

    player_id = fields.Many2one('laliga.player', string='Player')
    type = fields.Selection([
        ('1', 'Traspaso'),
        ('2', 'Cesión'),
        ('3', 'Libre')
    ], string='Transfer type', default='1')
    duration = fields.Integer('Duration (years) (0 for free transfers)')
    transfer_amount = fields.Monetary('Transfer amount', required=True, currency_field='currency_id')
    wage = fields.Monetary('Wage', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))
    team_from_id = fields.Many2one('laliga.team', string='Team From')
    team_to_id = fields.Many2one('laliga.team', string='Team To')
    date = fields.Date('Date')

from odoo import models, fields, api


class Transfer(models.Model):
    _name = 'league.transfer'
    _description = 'Player transfers'

    type = fields.Selection([
        ('1', 'Traspaso'),
        ('2', 'Cesión'),
        ('3', 'Libre')
    ], string='Transfer type', default='1')
    duration = fields.Integer('Duration (years) (0 for free transfers)')
    price = fields.Monetary('Price')
    wage = fields.Monetary('Wage')
    team_from_id = fields.Many2one('league.team', string='Team From')
    team_to_id = fields.Many2one('league.team', string='Team To')
    date = fields.Date('Date')

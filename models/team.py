from odoo import models, fields, api


class Team(models.Model):
    _name = 'league.team'
    _description = 'Team'

    name = fields.Char(string="Name", required=True)
    badge = fields.Image('Badge')
    players_ids = fields.One2many('league.player', 'team', string='Players')
    staff_ids = fields.One2many('league.staff', 'team', string='Staff')
    members = fields.One2many('league.member', 'team', string='Members')
    stadium_id = fields.Many2one('league.stadium', string='Stadium')
    salary_cap = fields.Monetary('Salary Cap', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))

    league = fields.Many2one('league.league', string="League")



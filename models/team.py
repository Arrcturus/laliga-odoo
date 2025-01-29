from odoo import models, fields, api


class Team(models.Model):
    _name = 'laliga.team'
    _description = 'Team'

    name = fields.Char(string="Name", required=True)
    badge = fields.Image('Badge')
    players_ids = fields.One2many('laliga.player', 'team', string='Players')
    staff_ids = fields.One2many('laliga.staff', 'team', string='Staff')
    members = fields.One2many('laliga.member', 'team', string='Members')
    stadium_id = fields.Many2one('laliga.stadium', string='Stadium')
    salary_cap = fields.Monetary('Salary Cap', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))

    league = fields.Many2one('laliga.league', string="League")



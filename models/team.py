from odoo import models, fields, api


class Team(models.Model):
    _name = 'league.team'
    _description = 'Team'

    name = fields.Char(string="Name", required=True)
    badge = fields.Image('Badge')
    players_ids = fields.One2many('league.player', 'player.league', string='Players')
    staff_ids = fields.One2many('league.staff', 'staff.league', string='Staff')
    members = fields.One2many('league.member', 'member.league', string='Members')
    stadium_id = fields.Many2one('league.stadium', string='Stadium')
    salary_cap = fields.Monetary('Salary Cap')



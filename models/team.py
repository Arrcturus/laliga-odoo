from odoo import models, fields, api
from odoo.exceptions import ValidationError

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

    @api.constrains('name')
    def _check_unique_name(self):
        for t in self:
            if t.name:
                duplicate_cs = self.search([('id', '!=', t.id), ('name', '=', t.name)])
            if duplicate_cs:
                raise ValidationError("The name is already assigned to another team.")

    @api.constrains('players_ids')
    def _check_players_limit(self):
        for team in self:
            if len(team.players_ids) > 24:
                raise ValidationError("The maximum number of players is 24.")

    @api.constrains('salary_cap', 'players_ids')
    def _check_salary_cap_not_surpassed(self):
        for team in self:
            total_salary = sum(player.wage for player in team.players_ids)
            if total_salary > team.salary_cap:
                raise ValidationError("The total salary of the players exceeds the salary cap.")
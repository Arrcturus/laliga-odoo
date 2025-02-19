from odoo import models, fields, api
from odoo.exceptions import ValidationError

class League(models.Model):
    _name = 'laliga.league'
    _description = 'League'

    name = fields.Char(string="Name", required=True)
    teams = fields.One2many('laliga.team', 'league', string='Teams')
    country = fields.Many2one('res.country', string='Country')
    img = fields.Image('Image')
    """
    @api.model
    def create(self, vals):
        league = super(League, self).create(vals)
        league._update_teams_league()
        return league

    def write(self, vals):
        res = super(League, self).write(vals)
        self._update_teams_league()
        return res

    def unlink(self):
        for league in self:
            league.teams.write({'league': False})
        return super(League, self).unlink()

    
    This method is called when a league is created or updated. It updates the league of the teams that are part of the league.
    And removes the league from the teams that are no longer part of the league.
    
    def _update_teams_league(self):
        for league in self:
            for team in league.teams:
                if team.league.id != league.id:
                    team.league = league.id
            other_teams = self.env['laliga.team'].search([('league', '=', league.id), ('id', 'not in', league.teams.ids)])
            other_teams.write({'league': False})
    """

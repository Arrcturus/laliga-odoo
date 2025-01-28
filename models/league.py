from odoo import models, fields, api


class League(models.Model):
    _name = 'league.league'
    _description = 'League'

    name = fields.Char(string="Name", required=True)
    teams = fields.One2many('league.team', 'league', string='Teams')
    country = fields.Many2one('res.country', string='Country')
    img = fields.Image('Image')

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class League(models.Model):
    _name = 'laliga.league'
    _description = 'League'

    name = fields.Char(string="Name", required=True)
    teams = fields.One2many('laliga.team', 'league', string='Teams')
    country = fields.Many2one('res.country', string='Country')
    img = fields.Image('Image')

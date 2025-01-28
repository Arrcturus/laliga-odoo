from odoo import models, fields, api


class Stats(models.Model):
    _name = 'league.stats'
    _description = 'Player stats'

    minutes = fields.Integer('Minutes', default=0)
    goals = fields.Integer('Goals', default=0)
    assists = fields.Integer('Assists', default=0)
    played_matches = fields.Integer('Played matches', default=0)
    sanctions = fields.Integer('Sanctions', default=0)

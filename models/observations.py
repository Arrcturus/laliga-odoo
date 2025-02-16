from odoo import models, fields, api


class Observations(models.Model):
    #_name = 'laliga.player'
    #_description = 'Player'
    _inherit = 'laliga.person'

    observations = fields.Text(string='Observations')

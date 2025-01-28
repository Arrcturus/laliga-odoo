from odoo import models, fields, api


class Player(models.Model):
    _name = 'league.player'
    _description = 'Player'
    _inherit = 'league.employee'

    jerseyNum = fields.Integer(string='Jersey Number', required=True)
    position = fields.Many2one(comodel_name='league.position', string='Position', required=True)
    height = fields.Integer(string='Height (cm)', required=True)
    weight = fields.Integer(string='Weight (kg)', required=True)
    value = fields.Float(string='Player value', required=True)
    medicalRecord = fields.Many2many(string='Medical record', comodel_name='league.injury')
    transfers = fields.Many2many(string='Transfer record', comodel_name='league.transfer')
    stats = fields.Many2one(comodel_name='league.stats', string='Stats', required=True)
    minWage = fields.Float(string='Wage', required=True)

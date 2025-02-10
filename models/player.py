from odoo import models, fields, api


class Player(models.Model):
    _name = 'laliga.player'
    _description = 'Player'
    _inherit = 'laliga.employee'

    jerseyNum = fields.Integer(string='Jersey Number', required=True)
    position = fields.Selection([
        ('1', 'Goalkeeper'),
        ('2', 'Defender'),
        ('3', 'Midfielder'),
        ('4', 'Attacker')
    ], string='Position', default = '1')
    height = fields.Integer(string='Height (cm)', required=True)
    weight = fields.Integer(string='Weight (kg)', required=True)
    value = fields.Float(string='Player value', required=True)
    medicalRecord = fields.Many2many(string='Medical record', comodel_name='laliga.injury')
    transfers = fields.Many2many(string='Transfer record', comodel_name='laliga.transfer')
    stats = fields.Many2one(comodel_name='laliga.stats', string='Stats', required=True)
    min_wage = fields.Monetary('Minimun Wage', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))

    team = fields.Many2one('laliga.team', string="Team")

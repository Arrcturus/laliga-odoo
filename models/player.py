from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Player(models.Model):
    _name = 'laliga.player'
    _description = 'Player'
    _inherit = 'laliga.person'

    jerseyNum = fields.Integer(string='Jersey Number', required=True)
    position = fields.Selection([
        ('1', 'Goalkeeper'),
        ('2', 'Defender'),
        ('3', 'Midfielder'),
        ('4', 'Attacker')
    ], string='Position', default='1')
    height = fields.Integer(string='Height (cm)', required=True)
    weight = fields.Integer(string='Weight (kg)', required=True)
    value = fields.Float(string='Player value', required=True)
    medicalRecord = fields.Many2many(string='Medical record', comodel_name='laliga.injury')
    transfers = fields.Many2many(string='Transfer record', comodel_name='laliga.transfer')
    
    stats = fields.Many2one('laliga.stats')
    minutes = fields.Integer(related='stats.minutes')
    goals = fields.Integer(related='stats.goals')
    assists = fields.Integer(related='stats.assists')
    played_matches = fields.Integer(related='stats.played_matches')
    sanctions = fields.Integer(related='stats.sanctions')

    goal_contributions_per_match = fields.Float(string='Goal Contributions per Match', compute='_compute_goal_contributions_per_match')

    contract = fields.Many2one('laliga.contract', string='Contract')
    wage = fields.Monetary(related="contract.wage", string="Wage")
    start = fields.Date(related="contract.start")
    end = fields.Date(related="contract.end")
    min_wage = fields.Monetary('Minimum Wage', required=False, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))
    injury = fields.One2many('laliga.injury', 'player_id', string='Injuries', required=False)
    
    team = fields.Many2one('laliga.team', string="Team")

    image = fields.Image('Image')

    @api.depends('goals', 'assists', 'played_matches')
    def _compute_goal_contributions_per_match(self):
        for player in self:
            if player.played_matches > 0:
                player.goal_contributions_per_match = (player.goals + player.assists) / player.played_matches
            else:
                player.goal_contributions_per_match = 0

    @api.constrains('contract')
    def _check_minimum_wage(self):
        for player in self:
            if player.contract and player.contract.wage < 190000:
                raise ValidationError("The player's salary cannot be less than 190,000.")

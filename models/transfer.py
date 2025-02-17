from odoo import models, fields, api


class Transfer(models.Model):
    _name = 'laliga.transfer'
    _description = 'Player transfers'

    player_id = fields.Many2one('laliga.player', string='Player')
    type = fields.Selection([
        ('1', 'Traspaso'),
        ('2', 'Cesión'),
        ('3', 'Libre')
    ], string='Transfer type', default='1')
    transfer_amount = fields.Monetary('Transfer amount (0 for free transfers)', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))
    team_from_id = fields.Many2one('laliga.team', string='Team From')
    team_to_id = fields.Many2one('laliga.team', string='Team To')
    contract = fields.Many2one('laliga.contract', string="Contract")

    @api.constrains("team_to_id")
    def _check_team_to(self):
        self.player_id.team = self.team_to_id
        self.player_id.contract = self.contract
        
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Transfer(models.Model):
    _name = 'laliga.transfer'
    _description = 'Player transfers'

    player_id = fields.Many2one('laliga.player', string='Player', required=True)
    transfer_type = fields.Selection([
        ('1', 'Transfer'),
        ('2', 'Loan'),
        ('3', 'Free')
    ], string='Transfer type', default='1', required=True)
    transfer_amount = fields.Monetary('Transfer amount (0 for free transfers)', required=True, currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))
    team_from_id = fields.Many2one('laliga.team', string='Team From')
    team_to_id = fields.Many2one('laliga.team', string='Team To')
    contract = fields.Many2one('laliga.contract', string="Contract")
    date = fields.Date('Date', required=True)

    @api.onchange('player_id')
    def _onchange_player_id(self):
        if self.player_id:
            self.team_from_id = self.player_id.team.id

    @api.constrains('team_to_id', 'contract', 'transfer_type')
    def _check_transfer_constraints(self):
        for transfer in self:
            if transfer.transfer_type == '3' and not transfer.team_to_id:
                if transfer.transfer_amount != 0:
                    raise ValidationError("The transfer amount must be 0 for free transfers without a team.")
                if transfer.contract:
                    raise ValidationError("A contract cannot be assigned to a player without a team.")
            if transfer.contract and transfer.contract.wage < 190000:
                raise ValidationError("The player's salary cannot be less than 190,000.")
            transfer.player_id.team = transfer.team_to_id
            transfer.player_id.contract = transfer.contract

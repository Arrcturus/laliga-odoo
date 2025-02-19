from odoo import models, fields, api
from datetime import timedelta

class Injury(models.Model):
    _name = 'laliga.injury'
    _description = 'Player injury history'

    description = fields.Char(string="Description", required=True)
    aprox_duration = fields.Integer(string="Aprox. duration (days)", required=True)
    injury_number = fields.Integer(string="The number of the injury", readonly=True)
    player_id = fields.Many2one('laliga.player', string="Related player", ondelete='cascade')
    start = fields.Date('Start', required=True)
    end = fields.Date('End', compute="_compute_end", store=True)

    @api.model
    def create(self, vals):
        player_id = vals.get('player_id')
        if player_id:
            existing_injuries = self.search_count([('player_id', '=', player_id)])
            vals['injury_number'] = existing_injuries + 1
        return super(Injury, self).create(vals)

    @api.depends('start', 'aprox_duration')
    def _compute_end(self):
        for record in self:
            if record.start and record.aprox_duration:
                record.end = record.start + timedelta(days=record.aprox_duration)
            else:
                record.end = False

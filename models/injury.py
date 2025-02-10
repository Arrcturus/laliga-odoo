from odoo import models, fields, api


class Injury(models.Model):
    _name = 'laliga.injury'
    _description = 'Player injury history'

    description = fields.Char(string="Description", required=True)
    aprox_duration = fields.Integer(string="Aprox. duration (days)", required=True)
    injury_number = fields.Integer(string="The number of the injury", readonly=True)
    player_id = fields.Many2one('laliga.player', string="Related player", ondelete='cascade')

    @api.model
    def create(self, vals):
        # Obtener el player asociado
        player_id = vals.get('player_id')
        if player_id:
            # Contar las lesiones existentes del player
            existing_injuries = self.search_count([('player_id', '=', player_id)])
            # Asignar el número consecutivo de la lesión
            vals['injury_number'] = existing_injuries + 1
        # Crear el registro de la lesión
        return super(Injury, self).create(vals)

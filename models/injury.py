from odoo import models, fields, api


class Injury(models.Model):
    _name = 'league.injury'
    _description = 'Player injury history'

    description = fields.Char(string="Description", required=True)
    aprox_duration = fields.Integer(string="Aprox. duration (days)", required=True)
    injury_number = fields.Integer(string="The number of the injury", readonly=True)
    jugador_id = fields.Many2one('league.jugador', string="Related player", ondelete='cascade')

    @api.model
    def create(self, vals):
        # Obtener el jugador asociado
        jugador_id = vals.get('jugador_id')
        if jugador_id:
            # Contar las lesiones existentes del jugador
            existing_injuries = self.search_count([('jugador_id', '=', jugador_id)])
            # Asignar el número consecutivo de la lesión
            vals['injury_number'] = existing_injuries + 1
        # Crear el registro de la lesión
        return super(Injury, self).create(vals)

from odoo import models, fields, api


class Staff(models.Model):
    _name = 'laliga.staff'
    _description = 'Staff'

    wage = fields.Many2one('laliga.employment', String='Employment', required=True)

    team = fields.Many2one('laliga.team', string="Team")
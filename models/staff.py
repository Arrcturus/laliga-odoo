from odoo import models, fields, api


class Staff(models.Model):
    _name = 'league.staff'
    _description = 'Staff'

    wage = fields.Many2one('league.employment', String='Employment', required=True)
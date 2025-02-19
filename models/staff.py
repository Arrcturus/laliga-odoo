from odoo import models, fields, api


class Staff(models.Model):
    _name = 'laliga.staff'
    _description = 'Staff'
    _inherit = 'laliga.person'

    team = fields.Many2one('laliga.team', string="Team")
    contract = fields.One2many('laliga.contract', 'staff_id', string='Contract')
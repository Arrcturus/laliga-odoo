from odoo import models, fields, api


class Member(models.Model):
    _name = 'laliga.member'
    _inherit = "laliga.person"
    _description = 'Member'

    team = fields.Many2one('laliga.team', string="Team")
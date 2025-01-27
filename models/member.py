from odoo import models, fields, api


class Member(models.Model):
    _name = 'league.member'
    _inherit = "league.person"
    _description = 'Member'

    id = fields.Integer('ID', required=True)
from odoo import models, fields, api


class Position(models.Model):
    _name = 'laliga.position'
    _description = 'Player position'

    name = fields.Char(string="Name", required=True)

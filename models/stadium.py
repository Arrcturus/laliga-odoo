from odoo import models, fields, api


class Stadium(models.Model):
    _name = 'league.stadium'
    _description = 'Team'

    name = fields.Char(string="Name", required=True)
    capacity = fields.Integer('Capacity')
    construction_date = fields.Date('Construction Date')
    city = fields.Char('City')



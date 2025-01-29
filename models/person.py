from odoo import models, fields, api


class Person(models.Model):
    _name = 'laliga.person'
    _description = 'Person'

    name = fields.Char(String="Name", required=True)
    dni = fields.Char(String="DNI", required=True)
    birthDate = fields.Date(String="Fecha de nacimiento", required=True)
    nationality = fields.Many2one('res.country', string='País', required=True)
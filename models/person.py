import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Person(models.Model):
    _name = 'laliga.person'
    _description = 'Person'

    name = fields.Char(String="Name", required=True)
    dni = fields.Char(String="DNI", required=True)
    birthDate = fields.Date(String="Fecha de nacimiento", required=True)
    nationality = fields.Many2one('res.country', string='País', required=True)

    @api.constrains('dni')
    def _comprobar_dni(self):
        """ Validar que el DNI sea correcto según el cálculo del módulo 23. """
        letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
        dni_regex = r'^\d{8}[A-Z]$'

        for record in self:
            if not record.dni:
                continue

            if not re.match(dni_regex, record.dni):
                raise ValidationError("The DNI must have 8 digits followed by an uppercase letter.")

            numero = int(record.dni[:-1])
            letra = record.dni[-1]

            if letra != letras_dni[numero % 23]:
                raise ValidationError("The DNI is not valid.")

    @api.constrains('dni')
    def _check_unique_dni(self):
        for d in self:
            if d.dni:
                duplicate_ds = self.search([('id', '!=', d.id), ('dni', '=', d.dni)])
            if duplicate_ds:
                raise ValidationError("The DNI must be unique")
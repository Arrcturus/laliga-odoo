from odoo import models, fields, api


class Employee(models.Model):
    _name = 'laliga.employee'
    _description = 'Employee'
    _inherit = 'laliga.person'

    #TODO img
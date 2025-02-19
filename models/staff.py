from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Staff(models.Model):
    _name = 'laliga.staff'
    _description = 'Staff'
    _inherit = 'laliga.person'

    name = fields.Char(string="Name", required=True)
    team_id = fields.Many2one('laliga.team', string='Team')
    employment_id = fields.Many2one('laliga.employment', string='Employment', required=True)
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.ref('base.EUR'))

    team = fields.Many2one('laliga.team', string="Team")
    contract = fields.Many2one('laliga.contract', string='Contract')
    wage = fields.Monetary(related="contract.wage", string="Wage")
    start = fields.Date(related="contract.start")
    end = fields.Date(related="contract.end")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    address = fields.Char(string="Address")

    @api.constrains('employment_id')
    def _check_min_wage(self):
        for staff in self:
            if staff.contract and any(contract.wage < staff.employment_id.min_wage for contract in staff.contract):
                raise ValidationError(f"The wage for {staff.name} cannot be less than the minimum wage for the employment position {staff.employment_id.name}.")
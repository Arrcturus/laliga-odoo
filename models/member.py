from odoo import models, fields, api


class Member(models.Model):
    _name = 'laliga.member'
    _inherit = "laliga.person"
    _description = 'Member'

    team = fields.Many2one('laliga.team', string="Team", ondelete="set null")
    member_number = fields.Integer(string="Member Number", readonly=True)

    @api.model
    def create(self, vals):
        team_id = vals.get('team')
        if team_id:
            existing_members = self.search_count([('team', '=', team_id)])
            vals['member_number'] = existing_members + 1 
        return super(Member, self).create(vals)

    def write(self, vals):
        for record in self:
            old_team = record.team.id
            new_team = vals.get('team')

            if new_team and new_team != old_team:
                existing_members = self.search_count([('team', '=', new_team)])
                vals['member_number'] = existing_members + 1

                old_team_members = self.search([('team', '=', old_team)], order="member_number asc")
                for index, member in enumerate(old_team_members, start=1):
                    member.member_number = index 

        return super(Member, self).write(vals)

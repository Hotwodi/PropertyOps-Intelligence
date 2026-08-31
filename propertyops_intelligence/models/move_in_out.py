from odoo import fields, models


class PoiMoveInOut(models.Model):
    _name = 'poi.move.in.out'
    _description = 'Move In / Move Out'
    _order = 'scheduled_date desc'

    name = fields.Char(string='Reference', required=True)
    lease_id = fields.Many2one(
        comodel_name='poi.lease',
        string='Lease',
        ondelete='cascade',
    )
    tenant_id = fields.Many2one(
        comodel_name='poi.tenant',
        string='Tenant',
        required=True,
        ondelete='restrict',
    )
    unit_id = fields.Many2one(
        comodel_name='poi.unit',
        string='Unit',
        required=True,
        ondelete='restrict',
    )
    type = fields.Selection(
        selection=[
            ('move_in', 'Move In'),
            ('move_out', 'Move Out'),
        ],
        string='Type',
        required=True,
    )
    scheduled_date = fields.Date(string='Scheduled Date', required=True)
    completed_date = fields.Date(string='Completed Date')
    inspection_checklist = fields.Html(string='Inspection Checklist')
    deposit_held = fields.Monetary(
        string='Deposit Held',
        currency_field='currency_id',
    )
    deposit_returned = fields.Monetary(
        string='Deposit Returned',
        currency_field='currency_id',
    )
    deductions = fields.Monetary(
        string='Deductions',
        currency_field='currency_id',
    )
    unit_readiness = fields.Selection(
        selection=[
            ('not_ready', 'Not Ready'),
            ('in_progress', 'In Progress'),
            ('ready', 'Ready'),
        ],
        string='Unit Readiness',
        default='not_ready',
    )
    vacancy_days = fields.Integer(string='Vacancy Days')
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    active = fields.Boolean(string='Active', default=True)

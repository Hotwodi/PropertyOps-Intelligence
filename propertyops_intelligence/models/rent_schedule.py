from odoo import fields, models


class PoiRentSchedule(models.Model):
    _name = 'poi.rent.schedule'
    _description = 'Rent Schedule Entry'
    _order = 'due_date desc'

    name = fields.Char(string='Reference', required=True)
    lease_id = fields.Many2one(
        comodel_name='poi.lease',
        string='Lease',
        required=True,
        ondelete='cascade',
    )
    due_date = fields.Date(string='Due Date', required=True)
    amount = fields.Monetary(
        string='Amount',
        currency_field='currency_id',
    )
    cam_amount = fields.Monetary(
        string='CAM Amount',
        currency_field='currency_id',
    )
    total_due = fields.Monetary(
        string='Total Due',
        currency_field='currency_id',
        compute='_compute_total_due',
        store=True,
    )
    paid_date = fields.Date(string='Paid Date')
    state = fields.Selection(
        selection=[
            ('scheduled', 'Scheduled'),
            ('due', 'Due'),
            ('paid', 'Paid'),
            ('overdue', 'Overdue'),
            ('partial', 'Partial'),
        ],
        string='State',
        default='scheduled',
        required=True,
    )
    days_late = fields.Integer(
        string='Days Late',
        compute='_compute_days_late',
        store=True,
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )

    def _compute_total_due(self):
        for record in self:
            record.total_due = (record.amount or 0.0) + (record.cam_amount or 0.0)

    def _compute_days_late(self):
        today = fields.Date.context_today(self)
        for record in self:
            if record.paid_date and record.due_date and record.paid_date > record.due_date:
                record.days_late = (record.paid_date - record.due_date).days
            elif not record.paid_date and record.due_date and record.due_date < today:
                record.days_late = (today - record.due_date).days
            else:
                record.days_late = 0

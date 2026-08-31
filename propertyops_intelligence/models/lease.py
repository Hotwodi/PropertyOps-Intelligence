from odoo import fields, models


class PoiLease(models.Model):
    _name = 'poi.lease'
    _description = 'Lease'
    _inherit = ['mail.thread']
    _order = 'start_date desc'

    name = fields.Char(string='Lease Name', required=True, tracking=True)
    lease_number = fields.Char(string='Lease Number', required=True, copy=False)
    property_id = fields.Many2one(
        comodel_name='poi.property',
        string='Property',
        required=True,
        ondelete='restrict',
    )
    unit_id = fields.Many2one(
        comodel_name='poi.unit',
        string='Unit',
        ondelete='restrict',
    )
    tenant_id = fields.Many2one(
        comodel_name='poi.tenant',
        string='Tenant',
        required=True,
        ondelete='restrict',
    )
    start_date = fields.Date(string='Start Date', required=True, tracking=True)
    end_date = fields.Date(string='End Date', required=True, tracking=True)
    base_rent = fields.Monetary(
        string='Base Rent',
        currency_field='currency_id',
    )
    rent_frequency = fields.Selection(
        selection=[
            ('monthly', 'Monthly'),
            ('quarterly', 'Quarterly'),
            ('annually', 'Annually'),
        ],
        string='Rent Frequency',
        default='monthly',
        required=True,
    )
    escalation_type = fields.Selection(
        selection=[
            ('fixed', 'Fixed'),
            ('index_cpi', 'Index (CPI)'),
            ('step', 'Step'),
        ],
        string='Escalation Type',
        default='fixed',
    )
    escalation_rate = fields.Float(
        string='Escalation Rate (%)',
        digits=(5, 2),
    )
    next_escalation_date = fields.Date(string='Next Escalation Date')
    renewal_option = fields.Boolean(string='Renewal Option')
    renewal_notice_days = fields.Integer(string='Renewal Notice (Days)')
    deposit_amount = fields.Monetary(
        string='Deposit Amount',
        currency_field='currency_id',
    )
    cam_charges = fields.Monetary(
        string='CAM Charges',
        currency_field='currency_id',
    )
    status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('expired', 'Expired'),
            ('terminated', 'Terminated'),
            ('renewed', 'Renewed'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
    )
    ai_renewal_probability = fields.Float(
        string='AI Renewal Probability (%)',
        digits=(5, 2),
    )
    rent_schedule_ids = fields.One2many(
        comodel_name='poi.rent.schedule',
        inverse_name='lease_id',
        string='Rent Schedule',
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    active = fields.Boolean(string='Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            name = record.name
            if record.lease_number:
                name = '[%s] %s' % (record.lease_number, record.name)
            result.append((record.id, name))
        return result

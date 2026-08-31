from odoo import fields, models


class PoiTenant(models.Model):
    _name = 'poi.tenant'
    _description = 'Tenant'
    _inherit = ['mail.thread']
    _order = 'name'

    name = fields.Char(string='Tenant Name', required=True, tracking=True)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Related Partner',
        ondelete='restrict',
    )
    company_name = fields.Char(string='Company Name')
    contact_phone = fields.Char(string='Phone')
    contact_email = fields.Char(string='Email')
    credit_score = fields.Integer(string='Credit Score')
    tenant_since = fields.Date(string='Tenant Since')
    ai_churn_risk = fields.Float(
        string='AI Churn Risk (%)',
        digits=(5, 2),
    )
    total_lease_count = fields.Integer(
        string='Total Lease Count',
        compute='_compute_total_lease_count',
        store=True,
    )
    lease_ids = fields.One2many(
        comodel_name='poi.lease',
        inverse_name='tenant_id',
        string='Leases',
    )
    active = fields.Boolean(string='Active', default=True)

    def _compute_total_lease_count(self):
        for record in self:
            record.total_lease_count = len(record.lease_ids)

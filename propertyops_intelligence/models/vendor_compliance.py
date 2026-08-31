from odoo import fields, models


class PoiVendorCompliance(models.Model):
    _name = 'poi.vendor.compliance'
    _description = 'Vendor Compliance'
    _order = 'expiry_date'

    name = fields.Char(string='Reference', required=True)
    vendor_id = fields.Many2one(
        comodel_name='res.partner',
        string='Vendor',
        required=True,
        ondelete='restrict',
        domain="[('supplier_rank', '>', 0)]",
    )
    property_id = fields.Many2one(
        comodel_name='poi.property',
        string='Property',
        ondelete='restrict',
    )
    insurance_type = fields.Char(string='Insurance Type')
    policy_number = fields.Char(string='Policy Number')
    coverage_amount = fields.Monetary(
        string='Coverage Amount',
        currency_field='currency_id',
    )
    expiry_date = fields.Date(string='Expiry Date')
    compliance_score = fields.Float(
        string='Compliance Score (%)',
        digits=(5, 2),
    )
    state = fields.Selection(
        selection=[
            ('compliant', 'Compliant'),
            ('expiring', 'Expiring'),
            ('expired', 'Expired'),
        ],
        string='State',
        default='compliant',
        required=True,
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    active = fields.Boolean(string='Active', default=True)

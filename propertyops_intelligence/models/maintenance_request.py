from odoo import fields, models


class PoiMaintenanceRequest(models.Model):
    _name = 'poi.maintenance.request'
    _description = 'Maintenance Request'
    _inherit = ['mail.thread']
    _order = 'created_date desc'

    name = fields.Char(string='Request Title', required=True, tracking=True)
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
        ondelete='restrict',
    )
    request_type = fields.Selection(
        selection=[
            ('plumbing', 'Plumbing'),
            ('electrical', 'Electrical'),
            ('hvac', 'HVAC'),
            ('structural', 'Structural'),
            ('appliance', 'Appliance'),
            ('common_area', 'Common Area'),
            ('other', 'Other'),
        ],
        string='Request Type',
        default='other',
        required=True,
    )
    priority = fields.Selection(
        selection=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
            ('emergency', 'Emergency'),
        ],
        string='Priority',
        default='medium',
        required=True,
    )
    description = fields.Html(string='Description')
    ai_urgency_score = fields.Float(
        string='AI Urgency Score',
        digits=(5, 2),
    )
    ai_suggested_vendor = fields.Char(string='AI Suggested Vendor')
    assigned_to = fields.Many2one(
        comodel_name='res.partner',
        string='Assigned To',
        domain="[('is_company', '=', True)]",
    )
    state = fields.Selection(
        selection=[
            ('submitted', 'Submitted'),
            ('triaged', 'Triaged'),
            ('assigned', 'Assigned'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
        ],
        string='State',
        default='submitted',
        required=True,
        tracking=True,
    )
    created_date = fields.Datetime(
        string='Created Date',
        default=fields.Datetime.now,
    )
    completed_date = fields.Datetime(string='Completed Date')
    active = fields.Boolean(string='Active', default=True)

    def action_triage(self):
        for record in self:
            record.state = 'triaged'

    def action_assign(self):
        for record in self:
            record.state = 'assigned'

    def action_start(self):
        for record in self:
            record.state = 'in_progress'

    def action_complete(self):
        for record in self:
            record.state = 'completed'
            record.completed_date = fields.Datetime.now()

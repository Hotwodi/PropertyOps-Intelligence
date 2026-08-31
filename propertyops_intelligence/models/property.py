from odoo import fields, models


class PoiProperty(models.Model):
    _name = 'poi.property'
    _description = 'Property'
    _order = 'code, name'

    name = fields.Char(string='Property Name', required=True)
    code = fields.Char(string='Property Code', required=True, copy=False)
    property_type = fields.Selection(
        selection=[
            ('office', 'Office'),
            ('retail', 'Retail'),
            ('industrial', 'Industrial'),
            ('mixed_use', 'Mixed Use'),
            ('multifamily', 'Multifamily'),
            ('self_storage', 'Self Storage'),
            ('hoa', 'HOA'),
        ],
        string='Property Type',
        default='office',
        required=True,
    )
    address = fields.Char(string='Address')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip = fields.Char(string='ZIP')
    total_units = fields.Integer(string='Total Units')
    total_sqft = fields.Float(string='Total Sq Ft')
    acquisition_date = fields.Date(string='Acquisition Date')
    owner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Owner',
    )
    ai_occupancy_forecast = fields.Float(
        string='AI Occupancy Forecast (%)',
        digits=(5, 2),
    )
    unit_ids = fields.One2many(
        comodel_name='poi.unit',
        inverse_name='property_id',
        string='Units',
    )
    active = fields.Boolean(string='Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            name = record.name
            if record.code:
                name = '[%s] %s' % (record.code, record.name)
            result.append((record.id, name))
        return result

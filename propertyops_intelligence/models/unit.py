from odoo import fields, models


class PoiUnit(models.Model):
    _name = 'poi.unit'
    _description = 'Unit / Suite'
    _order = 'property_id, name'

    name = fields.Char(string='Unit Name', required=True)
    property_id = fields.Many2one(
        comodel_name='poi.property',
        string='Property',
        required=True,
        ondelete='cascade',
    )
    unit_number = fields.Char(string='Unit Number')
    floor = fields.Char(string='Floor')
    sqft = fields.Float(string='Sq Ft')
    monthly_rent = fields.Monetary(
        string='Monthly Rent',
        currency_field='currency_id',
    )
    status = fields.Selection(
        selection=[
            ('vacant', 'Vacant'),
            ('occupied', 'Occupied'),
            ('maintenance', 'Maintenance'),
            ('reserved', 'Reserved'),
        ],
        string='Status',
        default='vacant',
        required=True,
    )
    ai_market_rent_estimate = fields.Monetary(
        string='AI Market Rent Estimate',
        currency_field='currency_id',
    )
    last_turnover_date = fields.Date(string='Last Turnover Date')
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
            if record.property_id and record.unit_number:
                name = '%s / %s' % (record.property_id.code or record.property_id.name, record.unit_number)
            result.append((record.id, name))
        return result

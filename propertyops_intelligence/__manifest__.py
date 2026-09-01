{
    'name': 'PropertyOps Intelligence: Lease Administration, Tenant Portal & Portfolio Control',
    'version': '18.0.1.0.0',
    'images': ['static/description/cover.png'],
    'summary': 'AI-powered lease administration, tenant portal, and portfolio control for commercial and residential property management.',
    'description': """
PropertyOps Intelligence: Lease Administration, Tenant Portal & Portfolio Control
==================================================================================

A comprehensive property management module for Odoo 18 that streamlines lease
administration, tenant lifecycle, rent scheduling, maintenance operations,
vendor compliance, and move-in/move-out workflows across your real estate
portfolio.

Key Features
------------
* **Properties & Units** - Track buildings, suites, square footage, occupancy
  status and AI occupancy forecasts at the portfolio level.
* **Tenants** - Maintain tenant master data with credit scores, churn-risk
  scoring and lease history.
* **Leases** - Full lease lifecycle with escalation types (fixed, CPI, step),
  renewal options, CAM charges and AI renewal probability.
* **Rent Schedule** - Automated rent schedule entries with overdue tracking,
  partial payments and days-late calculations.
* **Maintenance Requests** - Tenant-submittable work orders with AI urgency
  scoring, vendor suggestions and triage workflow.
* **Vendor Compliance** - Insurance and policy tracking with compliance scoring
  and expiring/expired alerts.
* **Move In/Out** - Inspection checklists, deposit handling, deductions and
  unit readiness tracking with vacancy-day metrics.

AI-Driven Insights
------------------
Each core record carries an AI field (occupancy forecast, churn risk, renewal
probability, market rent estimate, urgency score, suggested vendor) so
portfolio managers can act on predictive signals rather than hindsight.
""",
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'category': 'Productivity/AI',
    'license': 'LGPL-3',
    'price': 899.99,
    'currency': 'USD',
    'application': True,
    'installable': True,
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/unit_views.xml',
        'views/tenant_views.xml',
        'views/lease_views.xml',
        'views/rent_schedule_views.xml',
        'views/maintenance_request_views.xml',
        'views/vendor_compliance_views.xml',
        'views/move_in_out_views.xml',
        'views/menu.xml',
    ],
}

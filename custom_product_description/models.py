from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Assuming you have these custom fields
    ingredients = fields.Text('Ingredients')
    howtouse = fields.Text('How to Use')
    benefits = fields.Text('Benefits')
    when_to_use = fields.Text('When to Use')
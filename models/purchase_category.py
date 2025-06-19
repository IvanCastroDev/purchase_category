from odoo import models, fields

class Purchase_category(models.Model):
    _name = 'purchase.category'

    name = fields.Char('Name')
    description = fields.Char('Description')
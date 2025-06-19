from odoo import models, fields

class Users(models.Model):
    _inherit = "res.users"

    purchase_category_ids = fields.Many2many("purchase.category", string="Categorias de compras")
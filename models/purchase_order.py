from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    """ Domain para que solo sea posible seleccionar las categorias que el usuario tenga configuradas """
    purchase_category = fields.Many2one(
        'purchase.category', 
        string='Categoria de Compra', 
        domain=lambda self: [('id', 'in', self.env.user.purchase_category_ids.ids)]
    )

    """ Este campo se utilizar para computar el readonly del campo en la vista """
    purchase_category_read_only_in_form = fields.Boolean(compute='_compute_read_only')

    def _compute_read_only(self):
        for rec in self:
            """ Si el usuario no tiene el grupo 'group_purchase_category', el campo tendrá la propiedad readonly """
            if not rec.env.user.has_group("purchase_category.group_purchase_category"):
                rec.purchase_category_read_only_in_form = True
            else:
                rec.purchase_category_read_only_in_form = False
from odoo import api, fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    partner_ids = fields.Many2many('res.partner', 'partner_id', 'categ_id')

    @api.onchange('partner_ids')
    def onchange_partner_ids(self):
        for categ in self:
            product_ids = self.env['product.template'].search([('categ_id', 'in', categ.ids)])
            for p in product_ids:
                for c in categ.partner_ids.filtered(lambda l: l.ids[0] not in p.seller_ids.name.ids):
                    seller_id = self.env['product.supplierinfo'].create({
                        'name': c.ids[0],
                        'price': 0,
                    })
                    p.seller_ids |= seller_id
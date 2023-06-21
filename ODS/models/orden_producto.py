from odoo import models, fields

class Orden_producto(models.Model):
    _name = "orden_producto.model"
    _description = "Orden_producto"

    id_orden_entrega = fields.Many2many("entrega.model",string="Entrega")
    id_inventario = fields.Many2many("inventario.model",string="Inventario")
    cantidad = fields.Integer()
    
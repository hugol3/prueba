from odoo import models, fields

class Orden_producto(models.Model):
    _name = "orden_producto.model"
    _description = "Orden_producto"

    id_orden_entrega = fields.Integer()
    id_inventario = fields.Integer()
    cantidad = fields.Integer()
    
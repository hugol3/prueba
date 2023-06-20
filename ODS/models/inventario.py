from odoo import models, fields

class Inventario(models.Model):
    _name = "inventario.model"
    _description = "Inventario"

    id = fields.Integer()
    nombre = fields.Char()
    fecha_recibido = fields.Text()
    id_categoria = fields.Integer()
    id_usuario = fields.Integer()
    cantidad = fields.Integer()
    fecha_caducidad = fields.Text()
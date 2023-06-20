from odoo import models, fields

class Orden_entrega(models.Model):
    _name = "entrega.model"
    _description = "Entrega"

    id = fields.Integer()
    status = fields.Text()
    fecha = fields.Text()
    id_usuario = fields.Integer()
    id_beneficiario = fields.Integer()
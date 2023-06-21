from odoo import models, fields

class Orden_entrega(models.Model):
    _name = "entrega.model"
    _description = "Entrega"

    id = fields.Integer()
    status = fields.Text()
    fecha = fields.Text()
    id_usuario = fields.Many2one("usuario.model",string="Usuario")
    id_beneficiario = fields.Many2one("beneficiario.model",string="Beneficiario")
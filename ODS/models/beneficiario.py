from odoo import models, fields

class Beneficiario(models.Model):
    _name = "beneficiario.model"
    _description = "Beneficiario"

    id = fields.Integer()
    name = fields.Char()
    rfc = fields.Text()
    direccion = fields.Text()
    correo = fields.Text()



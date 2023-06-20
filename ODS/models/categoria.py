from odoo import models, fields

class Categoria(models.Model):
    _name = "categoria.model"
    _description = "Categoria"

    id = fields.Integer()
    nombre = fields.Char()
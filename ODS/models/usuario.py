from odoo import models, fields

class Usuario(models.Model):
    _name = "usuario.model"
    _description = "Usuario"


    name = fields.Char()
    id = fields.Integer()
    correo = fields.Text()
    admin = fields.Boolean()







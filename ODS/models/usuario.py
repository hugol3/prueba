from odoo import models, fields

class Usuario(models.Model):
    _name = "usuario.model"
    _description = "Usuario"

   
    id = fields.Integer()
    name = fields.Char()
    correo = fields.Text()
    admin = fields.Boolean()







from odoo import models, fields

class Usuario(models.Model):
    _name = "usuario.model"
    _description = "Usuario"


    name = fields.Char()
    id = fields.Interger()
    correo = fields.Text()
    admin = fields.Boolean()







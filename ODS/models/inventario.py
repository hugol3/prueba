from odoo import models, fields,http

class Inventario(models.Model):
    _name = "inventario.model"
    _description = "Inventario"

    id = fields.Integer()
    nombre = fields.Char()
    fecha_recibido = fields.Date()
    id_categoria = fields.Many2one("categoria.model", string="Categoria")
    id_usuario = fields.Many2one("usuario.model", string="Usuario")
    cantidad = fields.Integer()
    fecha_caducidad = fields.Date()
    img = fields.Text()

    def unlink(self):
        return super(Inventario, self).unlink()

    def create(self, vals):
        if vals.get('id'):
            self.browse(vals['id']).unlink()
        else:
            self.create({
                'id': vals.get('id', False),
                'nombre': vals.get('nombre', False),
                'fecha_recibido': vals.get('fecha_recibido', False),
                'id_categoria': vals.get('id_categoria', False),
                'id_usuario': vals.get('id_usuario', False),
                'cantidad': vals.get('cantidad', False),
                'fecha_caducidad': vals.get('fecha_caducidad', False),
            })




        
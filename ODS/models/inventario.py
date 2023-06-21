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
        for record in self:
            if record.id:
                record.unlink()
            else:
                self.id = vals.id
                nombre = vals.nombre
                fecha_recibido = vals.fecha_recibido
                id_categoria = vals.id_categoria
                id_usuario = vals.id_usuario
                cantidad = vals.cantidad
                fecha_caducidad = vals.fecha_caducidad 



        
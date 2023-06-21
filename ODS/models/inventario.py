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
                return super(Inventario, self).create(vals)



        
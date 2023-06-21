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

    def update(self,id,nombre, fecha_recibido, id_categoria, id_usuario, cantidad, fecha_caducidad):
        Inventario = self.env['inventario.model'].browse(id)
        Inventario.write({
            'nombre': nombre,
            'fecha_recibo' : fecha_recibido,
            'id_categoria' : id_categoria,
            'id_usuario' : id_usuario,
            'cantidad' : cantidad,
            'fecha_caducidad' : fecha_caducidad
        })
    def redireccionar(self):
        view_id = self.env.ref('ODS.actualizar').id
        model = self._name
        url = '/web#id={}&view_type=form&model={}&action={}'.format(self.id, model, view_id)
        return http.request.redirect(url)



        
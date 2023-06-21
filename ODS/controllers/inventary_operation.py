from odoo import http
from odoo.http import request

class MyController(http.Controller):
    @http.route('/mi_modulo/registro', auth='user', website=True)
    def create_product(self, **kwargs):
        data = request.jsonerquest
        # Lógica para crear un nuevo registro
        # Obtener los datos de la solicitud y guardarlos en un nuevo registro
        # Devolver una respuesta adecuada (redirección, mensaje de éxito, etc.)
        return 

    @http.route('/mi_modulo/registro/<int:id>', auth='user', website=True)
    def read_product(self, id, **kwargs):
        # Lógica para leer un registro existente
        # Consultar el registro con el ID especificado
        # Preparar y devolver una respuesta con los datos del registro
        return

    @http.route('/mi_modulo/registro/<int:id>/editar', auth='user', website=True)
    def update_product(self, id, **kwargs):
        # Lógica para actualizar un registro existente
        # Obtener los datos de la solicitud y aplicarlos al registro con el ID especificado
        # Devolver una respuesta adecuada (redirección, mensaje de éxito, etc.)
        return

    @http.route('/mi_modulo/registro/<int:id>/eliminar', auth='user', website=True)
    def delete_product(self, id, **kwargs):
        # Lógica para eliminar un registro existente
        # Buscar el registro con el ID especificado y eliminarlo de la base de datos
        # Devolver una respuesta adecuada (redirección, mensaje de éxito, etc.)
        return 
from odoo import http
from odoo.http import request

class RegistrosController(http.Controller):

    @http.route('/registros', auth='auth', website=True)
    def registros(self, **kwargs):
        registros = request.env['inventario.model'].sudo().search([])  # Obtén todos los registros

        return http.request.render('mimodulo.registros_template', {
            'registros': registros,
        })

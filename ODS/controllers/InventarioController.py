from odoo import http
from odoo.addons.my_module.models import MyModel


class InventarioController(http.Controller):

    @http.route('/ruta', auth='public', website=True)
    def mi_metodo(self, **kwargs):
        registros = MyModel.search([])
        return http.request.render('inventario.model.inventario2', {'registros': registros})
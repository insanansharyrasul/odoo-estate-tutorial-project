from odoo import http
from odoo.http import request

class EstateCustomer(http.Controller):

    @http.route('/customerform', type="http", auth='public', website='True')
    def customer(self, **kw):
        return http.request.render("estate.create_customer", {})

    @http.route('/create/customer', type="http", auth='public', website='True')
    def index(self, **kw):
        request.env['estate.property'].sudo().create(kw)
        return request.render("estate.customer_thanks", {})
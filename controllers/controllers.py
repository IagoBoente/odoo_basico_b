# -*- coding: utf-8 -*-
# from odoo import http


# class OdooBasicoB(http.Controller):
#     @http.route('/odoo_basico_b/odoo_basico_b/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_basico_b/odoo_basico_b/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_basico_b.listing', {
#             'root': '/odoo_basico_b/odoo_basico_b',
#             'objects': http.request.env['odoo_basico_b.odoo_basico_b'].search([]),
#         })

#     @http.route('/odoo_basico_b/odoo_basico_b/objects/<model("odoo_basico_b.odoo_basico_b"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_basico_b.object', {
#             'object': obj
#         })

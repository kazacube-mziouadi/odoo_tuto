# -*- coding: utf-8 -*-
from openerp import http

# class Ditefacts(http.Controller):
#     @http.route('/ditefacts/ditefacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ditefacts/ditefacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ditefacts.listing', {
#             'root': '/ditefacts/ditefacts',
#             'objects': http.request.env['ditefacts.ditefacts'].search([]),
#         })

#     @http.route('/ditefacts/ditefacts/objects/<model("ditefacts.ditefacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ditefacts.object', {
#             'object': obj
#         })
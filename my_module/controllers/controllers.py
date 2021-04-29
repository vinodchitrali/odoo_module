# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class MyModule(http.Controller):
    @http.route('/my_module/my_module/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_module/my_module/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('my_module.listing', {
            'root': '/my_module/my_module',
            'objects': http.request.env['my_module.my_module'].search([]),
        })

    @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_module.object', {
            'object': obj
        })
        
class HospitalForm(http.Controller):
    #mention class name
    @http.route(['/hospital/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("my_module.tmp_hospital_form", {})

    @http.route(['/hospital/form/submit'], type='http', auth="user", website=True)
    #next controller with url for submitting data from the form#
    def hospital_form_submit(self, **post):
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'street': post.get('location'),
            'phone': post.get('phone'),            
            'tbeds' : post.get('tbeds'),
            'vents' : post.get('vents'),
            'meds' : post.get('meds'),
            'cbeds' : post.get('cbeds'),
            'contact_type': 'hospital'
        })
        vals = {
            'partner': partner,
        }
        #inherited the model to pass the values to the model from the form#
        return request.render("my_module.tmp_hospital_form_success", vals)
        #finally send a request to render the thank you page#
        
            
    @http.route(['/gethospital'], type='http', auth="public", website=True)
    def hospital_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('my_module.hospital_index', {
            'teachers': Teachers.sudo().search([('contact_type','=', 'hospital')])
        })
        
        
        
        
        
        
        
        
        
        
        
class PatientForm(http.Controller):
   
    @http.route(['/patient/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("my_module.tmp_patient_form", {})

    @http.route(['/patient/form/submit'], type='http', auth="user", website=True)
    def patient_form_submit(self, **post):
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'ask': post.get('ask'),
            'contact_type': 'patient'

        })
        vals = {
            'partner': partner,
        }
        return request.render("my_module.tmp_patient_form_success", vals)


    @http.route(['/getpatient'], type='http', auth="public", website=True)
    def patient_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('my_module.patient_index', {
            'teachers': Teachers.sudo().search([('contact_type','=', 'patient')])
        })
        
        
class TribulanceInformation(http.Controller):
   
    @http.route(['/tribulance/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("my_module.tmp_tribulance_form", {})

    @http.route(['/tribulance/form/submit'], type='http', auth="user", website=True)
    def tribulance_form_submit(self, **post):
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'contact_type': 'tribulance'

        })
        vals = {
            'partner': partner,
        }
        return request.render("my_module.tmp_tribulance_form_success", vals)


    @http.route(['/gettribulance'], type='http', auth="public", website=True)
    def tribulance_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('my_module.tribulance_index', {
            'teachers': Teachers.sudo().search([('contact_type','=', 'tribulance')])
        })



      
class CovidTestCenterInformation(http.Controller):
   
    @http.route(['/covidtestcenter/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("my_module.tmp_covidtestcenter_form", {})

    @http.route(['/covidtestcenter/form/submit'], type='http', auth="user", website=True)
    def covidtestcenter_form_submit(self, **post):
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'contact_type': 'covidtestcenter'

        })
        vals = {
            'partner': partner,
        }
        return request.render("my_module.tmp_covidtestcenter_form_success", vals)


    @http.route(['/getcovidtestcenter'], type='http', auth="public", website=True)
    def covidtestcenter_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('my_module.covidtestcenter_index', {
            'teachers': Teachers.sudo().search([('contact_type','=', 'covidtestcenter')])
        })





      
class FuneralService(http.Controller):
   
    @http.route(['/funeralservice/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("my_module.tmp_funeralservice_form", {})

    @http.route(['/funeralservice/form/submit'], type='http', auth="user", website=True)
    def funeralservice_form_submit(self, **post):
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'contact_type': 'funeralservice'

        })
        vals = {
            'partner': partner,
        }
        return request.render("my_module.tmp_funeralservice_form_success", vals)


    @http.route(['/getfuneralservice'], type='http', auth="public", website=True)
    def funeralservice_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('my_module.funeralservice_index', {
            'teachers': Teachers.sudo().search([('contact_type','=', 'funeralservice')])
        })


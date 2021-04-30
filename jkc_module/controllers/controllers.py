# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MyModule(http.Controller):
    @http.route('/jkc_module/jkc_module/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/jkc_module/jkc_module/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('jkc_module.listing', {
            'root': '/jkc_module/jkc_module',
            'objects': http.request.env['jkc_module.jkc_module'].search([]),
        })

    @http.route('/jkc_module/jkc_module/objects/<model("jkc_module.jkc_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('jkc_module.object', {
            'object': obj
        })


class HospitalForm(http.Controller):
    # mention class name
    @http.route(['/hospital/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_hospital_form", {})

    @http.route(['/hospital/form/submit'], type='http', auth="user", website=True)
    #next controller with url for submitting data from the form#
    def hospital_form_submit(self, post_id="", **post):
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            obj = Teachers.search([('id', '=', post_id)])[0]
            obj.update({
                'email': post.get('email'),
                'street': post.get('location'),
                'phone': post.get('phone'),
                'tbeds': post.get('tbeds'),
                'vents': post.get('vents'),
                'meds': post.get('meds'),
                'cbeds': post.get('cbeds'),
            })            
            vals = {
                'o': obj,
            }
            return request.render("jkc_module.tmp_hospital_form_success", vals)

        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'street': post.get('location'),
            'phone': post.get('phone'),
            'tbeds': post.get('tbeds'),
            'vents': post.get('vents'),
            'meds': post.get('meds'),
            'cbeds': post.get('cbeds'),
            'contact_type': 'hospital'
        })
        vals = {
            'partner': partner,
        }
        #inherited the model to pass the values to the model from the form#
        return request.render("jkc_module.tmp_hospital_form_success", vals)

    @http.route(['/gethospital'], type='http', auth="public", website=True)
    def hospital_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.hospital_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'hospital')])
        })


    @http.route(['/edithospital'], type='http', auth="user", website=True)
    def edit_hospital(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_hospital_form', {
            'teacher': Teachers.search([('contact_type', '=', 'hospital'), ('id', '=', post_id)])[0]
        })


class PatientForm(http.Controller):

    @http.route(['/patient/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_patient_form", {})

    @http.route(['/patient/form/submit'], type='http', auth="user", website=True)
    def patient_form_submit(self, post_id="", **post):        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
                'ask': post.get('ask'),

            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_patient_form_success", vals)
                
                
                
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
        return request.render("jkc_module.tmp_patient_form_success", vals)

    @http.route(['/getpatient'], type='http', auth="public", website=True)
    def patient_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.patient_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'patient')])
        })

    @http.route(['/editpatient'], type='http', auth="user", website=True)
    def edit_patient(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_patient_form', {
            'teacher': Teachers.search([('contact_type', '=', 'patient'), ('id', '=', post_id)])[0]
        })



class TriambulanceInformation(http.Controller):

    @http.route(['/triambulance/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_triambulance_form", {})

    @http.route(['/triambulance/form/submit'], type='http', auth="user", website=True)
    def triambulance_form_submit(self, post_id="", **post):
        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),

            })
            vals = {
                        'partner': partner,
            }
            return request.render("jkc_module.tmp_triambulance_form_success", vals)

        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'contact_type': 'triambulance'

        })
        vals = {
            'partner': partner,
        }
        return request.render("jkc_module.tmp_triambulance_form_success", vals)

    @http.route(['/gettriambulance'], type='http', auth="public", website=True)
    def triambulance_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.triambulance_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'triambulance')])
        })


    @http.route(['/edittriambulance'], type='http', auth="user", website=True)
    def edit_triambulance(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_triambulance_form', {
            'teacher': Teachers.search([('contact_type', '=', 'triambulance'), ('id', '=', post_id)])[0]
        })
        
        
class CovidTestCenterInformation(http.Controller):

    @http.route(['/covidtestcenter/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_covidtestcenter_form", {})

    @http.route(['/covidtestcenter/form/submit'], type='http', auth="user", website=True)
    def covidtestcenter_form_submit(self, post_id="", **post):

        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location')
            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_covidtestcenter_form_success", vals)
            
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
        return request.render("jkc_module.tmp_covidtestcenter_form_success", vals)

    @http.route(['/getcovidtestcenter'], type='http', auth="public", website=True)
    def covidtestcenter_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.covidtestcenter_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'covidtestcenter')])
        })

    @http.route(['/editcovidtestcenter'], type='http', auth="user", website=True)
    def edit_covidtestcenter(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_covidtestcenter_form', {
            'teacher': Teachers.search([('contact_type', '=', 'covidtestcenter'), ('id', '=', post_id)])[0]
        })

class FuneralService(http.Controller):

    @http.route(['/funeralservice/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_funeralservice_form", {})

    @http.route(['/funeralservice/form/submit'], type='http', auth="user", website=True)
    def funeralservice_form_submit(self, post_id="", **post):
         
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_funeralservice_form_success", vals)        
        
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
        return request.render("jkc_module.tmp_funeralservice_form_success", vals)

    @http.route(['/getfuneralservice'], type='http', auth="public", website=True)
    def funeralservice_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.funeralservice_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'funeralservice')])
        })

    @http.route(['/editfuneralservice'], type='http', auth="user", website=True)
    def edit_funeralservice(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_funeralservice_form', {
            'teacher': Teachers.search([('contact_type', '=', 'funeralservice'), ('id', '=', post_id)])[0]
        })
   

class OxygenForm(http.Controller):

    @http.route(['/oxygen/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_oxygen_form", {})

    @http.route(['/oxygen/form/submit'], type='http', auth="user", website=True)
    def oxygen_form_submit(self, post_id="", **post):        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
                'ask': post.get('ask'),

            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_oxygen_form_success", vals)
                
                
                
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'ask': post.get('ask'),
            'contact_type': 'oxygen'

        })
        vals = {
            'partner': partner,
        }
        return request.render("jkc_module.tmp_oxygen_form_success", vals)

    @http.route(['/getoxygen'], type='http', auth="public", website=True)
    def oxygen_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.oxygen_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'oxygen')])
        })

    @http.route(['/editoxygen'], type='http', auth="user", website=True)
    def edit_oxygen(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_oxygen_form', {
            'teacher': Teachers.search([('contact_type', '=', 'oxygen'), ('id', '=', post_id)])[0]
        })

class PhysicianForm(http.Controller):

    @http.route(['/physician/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_physician_form", {})

    @http.route(['/physician/form/submit'], type='http', auth="user", website=True)
    def physician_form_submit(self, post_id="", **post):        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
                'ask': post.get('ask'),

            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_physician_form_success", vals)
                
                
                
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'ask': post.get('ask'),
            'contact_type': 'physician'

        })
        vals = {
            'partner': partner,
        }
        return request.render("jkc_module.tmp_physician_form_success", vals)

    @http.route(['/getphysician'], type='http', auth="public", website=True)
    def physician_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.physician_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'physician')])
        })

    @http.route(['/editphysician'], type='http', auth="user", website=True)
    def edit_physician(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_physician_form', {
            'teacher': Teachers.search([('contact_type', '=', 'physician'), ('id', '=', post_id)])[0]
        })
    
        
        
        

class FoodForm(http.Controller):

    @http.route(['/food/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_food_form", {})

    @http.route(['/food/form/submit'], type='http', auth="user", website=True)
    def food_form_submit(self, post_id="", **post):        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
                'ask': post.get('ask'),

            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_food_form_success", vals)
                
                
                
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'ask': post.get('ask'),
            'contact_type': 'food'

        })
        vals = {
            'partner': partner,
        }
        return request.render("jkc_module.tmp_food_form_success", vals)

    @http.route(['/getfood'], type='http', auth="public", website=True)
    def food_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.food_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'food')])
        })

    @http.route(['/editfood'], type='http', auth="user", website=True)
    def edit_food(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_food_form', {
            'teacher': Teachers.search([('contact_type', '=', 'food'), ('id', '=', post_id)])[0]
        })
    

class VaccineForm(http.Controller):

    @http.route(['/vaccine/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_vaccine_form", {})

    @http.route(['/vaccine/form/submit'], type='http', auth="user", website=True)
    def vaccine_form_submit(self, post_id="", **post):        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
                'ask': post.get('ask'),

            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_vaccine_form_success", vals)
                
                
                
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'ask': post.get('ask'),
            'contact_type': 'vaccine'

        })
        vals = {
            'partner': partner,
        }
        return request.render("jkc_module.tmp_vaccine_form_success", vals)

    @http.route(['/getvaccine'], type='http', auth="public", website=True)
    def vaccine_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.vaccine_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'vaccine')])
        })

    @http.route(['/editvaccine'], type='http', auth="user", website=True)
    def edit_vaccine(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_vaccine_form', {
            'teacher': Teachers.search([('contact_type', '=', 'vaccine'), ('id', '=', post_id)])[0]
        })

class PharmacyForm(http.Controller):

    @http.route(['/pharmacy/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_pharmacy_form", {})

    @http.route(['/pharmacy/form/submit'], type='http', auth="user", website=True)
    def pharmacy_form_submit(self, post_id="", **post):        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
                'ask': post.get('ask'),

            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_pharmacy_form_success", vals)
                
                
                
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'ask': post.get('ask'),
            'contact_type': 'pharmacy'

        })
        vals = {
            'partner': partner,
        }
        return request.render("jkc_module.tmp_pharmacy_form_success", vals)

    @http.route(['/getpharmacy'], type='http', auth="public", website=True)
    def pharmacy_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.pharmacy_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'pharmacy')])
        })

    @http.route(['/editpharmacy'], type='http', auth="user", website=True)
    def edit_pharmacy(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_pharmacy_form', {
            'teacher': Teachers.search([('contact_type', '=', 'pharmacy'), ('id', '=', post_id)])[0]
        })

class WasteAndDisposalForm(http.Controller):

    @http.route(['/wasteandsan/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_wasteandsan_form", {})

    @http.route(['/wasteandsan/form/submit'], type='http', auth="user", website=True)
    def wasteandsan_form_submit(self, post_id="", **post):        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
                'ask': post.get('ask'),

            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_wasteandsan_form_success", vals)
                
                
                
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'ask': post.get('ask'),
            'contact_type': 'wasteandsan'

        })
        vals = {
            'partner': partner,
        }
        return request.render("jkc_module.tmp_wasteandsan_form_success", vals)

    @http.route(['/getwasteandsan'], type='http', auth="public", website=True)
    def wasteandsan_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.wasteandsan_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'wasteandsan')])
        })

    @http.route(['/editwasteandsan'], type='http', auth="user", website=True)
    def edit_wasteandsan(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_wasteandsan_form', {
            'teacher': Teachers.search([('contact_type', '=', 'wasteandsan'), ('id', '=', post_id)])[0]
        })



class PlasmaDonorForm(http.Controller):

    @http.route(['/plasmadonor/form'], type='http', auth="user", website=True)
    def partner_form(self, **post):
        return request.render("jkc_module.tmp_plasmadonor_form", {})

    @http.route(['/plasmadonor/form/submit'], type='http', auth="user", website=True)
    def plasmadonor_form_submit(self, post_id="", **post):        
        if post_id!="":
            # then its edit mode
            Teachers = http.request.env['res.partner']        
            partner = Teachers.search([('id', '=', post_id)])[0]
            partner.update({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone'),
                'street': post.get('location'),
                'ask': post.get('ask'),

            })
            vals = {
                'partner': partner,
            }
            return request.render("jkc_module.tmp_plasmadonor_form_success", vals)
                
                
                
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone'),
            'street': post.get('location'),
            'ask': post.get('ask'),
            'contact_type': 'plasmadonor'

        })
        vals = {
            'partner': partner,
        }
        return request.render("jkc_module.tmp_plasmadonor_form_success", vals)

    @http.route(['/getplasmadonor'], type='http', auth="public", website=True)
    def plasmadonor_partner_form(self, **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.plasmadonor_index', {
            'teachers': Teachers.sudo().search([('contact_type', '=', 'plasmadonor')])
        })

    @http.route(['/editplasmadonor'], type='http', auth="user", website=True)
    def edit_plasmadonor(self, post_id="", **post):
        Teachers = http.request.env['res.partner']
        return http.request.render('jkc_module.tmp_plasmadonor_form', {
            'teacher': Teachers.search([('contact_type', '=', 'plasmadonor'), ('id', '=', post_id)])[0]
        })

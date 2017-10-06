#
#  Sample Project
#  
#
#  Created by mohammad abdillah wahab on 10/05/17.
#  Copyright (c) 2017 mohammad abdillah wahab. All rights reserved.
#

from odoo import api, fields, models, tools, exceptions, _
from odoo.osv import osv

class ClassFirst(models.Model):
	_name = 'class.first' #this for define what the model name and table name (in database) thats you create

	#FIRST STEP
	#default datatype --------------------------
	# for more informastion, u can open in Odoo Documentation https://www.odoo.com/documentation/10.0/reference/orm.html

	#field 'name' is must to create
	name = fields.Char(string='Name Of Char Field', readonly=False, required=False, default='default value of name')
	#you also can devine this filed just like 
	#	name = fields.Char('Name Of Char Field')
	#the first parameter is string, and the value of other parameters id 'False'

	number_interger = fields.Integer('this is Integer')
	number_float 	= fields.Float('this is Float')
	date_field		= fields.Date('this is Date')
	datetime_field	= fields.Datetime('this is Datetime')
	text_field		= fields.Text('this is Text')
	boolean_field	= fields.Boolean('this is Boolean')

	#the next field is selection field. before u create a field, u must devine ur list (array) of selection option.
	SELECTION = [('value_option','label in the output'),('second_value','this is label second value')]
	#and then u create the field
	selection_field = fields.Selection(string='this is selection field', selection=SELECTION)
	#end of default datatype -------------------

	#SECOND STEP
	#the relation field
	#1. Many2one is the field that ur value is taken from another model()
	#before u create this field, u must create ur model reference first, or u taken the reference from odoo default models, like 'res.partner'
	# for example, i create class.second in second_class.py file
	city_id			= fields.Many2one('class.second','this is city fields', help=' (Many2one from city model)')
	

	#this sample Many2one from res.partner
	#dont forget for this rule, if u will, taken relation from other model in outside of ur module, u must depend that module in manifest
	#
	partner_id 		= fields.Many2one('res.partner','this is partner field', help=' (Many2one from Partner model)' )

	#2 One2many
	#this is the field for relation ur line.
	#before u cretae this field, u must create the Many2one field at ur model reference, and that field will taken ID from this model
	#fore axample, i create class.third model in third_class.py file
	lines			= fields.One2many('class.third','first_id',string='Lines')
	#fris parameter is model reference, and second one is field that save id from this model


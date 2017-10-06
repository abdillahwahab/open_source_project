#
#  Sample Project
#  
#
#  Created by mohammad abdillah wahab on 10/05/17.
#  Copyright (c) 2017 mohammad abdillah wahab. All rights reserved.
#

from odoo import api, fields, models, tools, exceptions, _
from odoo.osv import osv

class ClassThird(models.Model):
	_name = 'class.third' #this for define what the model name and table name (in database) thats you create

	name 		= fields.Char('Line')
	first_id	= fields.Many2one('class.first','ID from FIRST')
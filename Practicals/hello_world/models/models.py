from future.backports.email.policy import default
from google.protobuf.text_encoding import string
from odoo_17.odoo.odoo import models, fields, api

class HelloWorld(models.Model):
    _name = 'hello.sanjay'
    _description = 'Hello World model'

    name = fields.Char(string = 'name', default="Hello World")

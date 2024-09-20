from odoo import models, fields

class Student(models.Model):
    _name = 'wb.student'
    _description = 'Student'

    name = fields.Char(string='Name')

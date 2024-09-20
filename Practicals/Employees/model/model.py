from odoo import models, fields

class Employee(models.Model):
    _name = 'wb.employee'
    _description = 'Employee'

    employee_id = fields.Char(string='Employee ID')
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone_number = fields.Char(string='Phone Number')
    salary = fields.Float(string='Salary')
    joining_year = fields.Char(string='Joining Year')
    technology_working_on = fields.Char(string='Technology Working On')

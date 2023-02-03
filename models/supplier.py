from odoo import fields, models

class Supplier(models.Model):
    _name = 'material.supplier'
    _description = 'Data Supplier'
    _rec_name = 'supplier'

    id = fields.Char()
    supplier = fields.Char(string="Related Supplier", required=True)
    
    _sql_constraints = [
        ('supplier_unique', 'UNIQUE (supplier)', 'This supplier is already exists')
    ]
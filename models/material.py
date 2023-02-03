from odoo import fields, models

class Material(models.Model):
    _name         = 'material.data'
    _description  = 'Data Material'
    id            = fields.Char()
    material_code = fields.Char(string="Material Code", required=True)
    material_name = fields.Char(string="Material Name", required=True)

    tipe = fields.Selection([
        ('',''),
        ('fabric','Fabric'),
        ('jeans','Jeans'),
        ('cotton','Cotton')
    ],default='',string='Material Type',required=True)

    price    = fields.Integer(string="Material Buy Price", required=True)
    supplier = fields.Many2one(string="Related Supplier", comodel_name="material.supplier",
               onupdate="cascade",ondelete="cascade",required=True)

    _sql_constraints = [
        ('check_price', 'CHECK(price >= 100)', 'Price should not be below 100'),
        ('material_code_unique', 'UNIQUE (material_code)', 'This material code is already exists')
    ]

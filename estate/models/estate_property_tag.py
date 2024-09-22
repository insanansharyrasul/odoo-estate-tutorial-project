from odoo import fields, models

class EstatePropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tags"
    _sql_constraints = [
        ('check_name', 'UNIQUE(name)', "This name must be unique")
    ]
    _order = "name"
    name = fields.Char(required=True)
    color = fields.Integer("Color")

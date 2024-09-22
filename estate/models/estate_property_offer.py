from dateutil.relativedelta import relativedelta
from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools import float_compare

class EstatePropertyOFfer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', "The price must be positive")
    ]
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(
        selection=[('accepted', 'Accepted'), ('refused', 'Refused')]
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date", inverse="_inverse_date")
    property_type_id = fields.Many2one("estate.property.type", related="property_id.property_type_id", string="Property Type", store=True)

    @api.depends("create_date", "validity")
    def _compute_date(self):
        for record in self:
            date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = date + relativedelta(days=record.validity)

    def _inverse_date(self):
        for record in self:
            date = record.create_date.date() if record.create_date else fields.Date.today()
            record.validity = (record.date_deadline - date).days

    def action_accept(self):
        if "accepted" in self.mapped("property_id.offer_ids.status"):
            raise UserError("An offer is already been accepted")
        self.write(
            {
                "status" : "accepted"
            }
        )
        return self.mapped("property_id").write(
            {
                "state" : "offerAccepted",
                "selling_price" : self.price,
                "buyer_id" : self.partner_id.id
            }
        )
    
    def action_refuse(self):
        return self.write(
            {
                "status" : "refused"
            }
        )

    @api.model
    def create(self, vals):
        if vals.get("property_id") and vals.get("price"):
            prop = self.env["estate.property"].browse(vals["property_id"])
            if prop.offer_ids:
                max_offer = max(prop.mapped("offer_ids.price"))
                if float_compare(vals["price"], max_offer, precision_rounding=0.01) <= 0:
                    raise UserError("The offer muse be higher than %.2f" % max_offer)
            prop.state = "offerReceived"
        return super().create(vals)
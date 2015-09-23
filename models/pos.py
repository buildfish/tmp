# -*- coding: utf-8 -*-

from openerp import models, fields, api

class pos_config(models.Model):
    _inherit = "pos.config"

    more_options = fields.Boolean("More Option")
    url_lat_lng = fields.Char("Get latitude longitude", default="https://justgetflux.com/map.html", readonly=True)
    lat = fields.Float("Latitude")
    lng = fields.Float("Longitude")
    info = fields.Text("Panel info.", help="Info location")
    radius = fields.Float("Radius coverage", help="Radio measure in meters")

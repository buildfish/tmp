# -*- coding: utf-8 -*-
from openerp import http, SUPERUSER_ID
from openerp.http import request
from datetime import date
import werkzeug.utils
import urllib2
import werkzeug.wrappers
import json
import simplejson
from openerp.tools.translate import _


class FoodDelivery(http.Controller):
    @http.route(['/page/point_locals_radius_json'], type='http', auth="public", website=True, cors="*")
    def point_locals_radius_json(self, **kwargs):
        cr, uid, context, registry = request.cr, request.uid, request.context, request.registry
        orm_pos_config = registry.get('pos.config')
        pos_config_ids = orm_pos_config.search(cr, SUPERUSER_ID, [('more_options','=',True)], context=context)
        values = orm_pos_config.read(cr, SUPERUSER_ID, pos_config_ids, ["lat", "lng", "radius", "info", "name"], context)
        vals = {}
        for i in values:
            info = i['name'] if  i['info'] == '<br>' or i['info'] == False else i['info']
            vals.update({i['id']: {'center': {'lat': i['lat'], 'lng': i['lng']}, 'population': i['radius'], 'phillyContent': info}})

        #data = json.dumps(vals)
        data = simplejson.dumps(vals)
        return werkzeug.wrappers.Response(data, content_type='application/json;charset=utf-8')

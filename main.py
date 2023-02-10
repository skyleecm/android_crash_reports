import os
import webapp2
from admin import admin
from crashreports import api, crashreports
from google.appengine.api import wrap_wsgi_app

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect('/reports/all')

routes = api.routes + crashreports.routes + admin.routes
routes.append( ('/', MainHandler) )
app = wrap_wsgi_app(webapp2.WSGIApplication(routes, debug=True))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


import cherrypy
import pymysql
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

class HelloWorld(object):
    def index(self):
        tmpl = env.get_template('index.html')
        return tmpl.render()

    index.exposed = True

    def bonjour(self, nom=None):
        if nom:
            return "Bonjour " + nom + "! <br/> <a href=\"/\">Accueil</a>"
        else:
            return "Bonjour ! <br/> <a href=\"/\">Accueil</a>"
    bonjour.exposed = True

    def liste(self):
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='mimo',
                             password='Z65mimo2016_',
                             database='mimo')

        cur = db.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT id, item FROM liste")
        tmpl = env.get_template('liste.html')
        return tmpl.render(items=cur)
    liste.exposed = True

    def ajouter(self, item=None):
        if item:
            db = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='mimo',
                                 password='Z65mimo2016_',
                                 database='mimo')
            cur = db.cursor()
            cur.execute("insert into liste values (NULL, '" + item +"')")
            db.commit()
            return "Votre item a bien été enregistré ! <br/><a href=\"/\">Home</a>"
        else:
            return "<form method='GET' action='ajouter'>" \
               "  Quel est le nouvel item?" \
               "  <input type='text' name='item'>" \
               "  <input type='submit' value='Enregistrer'>" \
               "</form>" \
               "  <a href=\"/liste\">liste</a><br/>" \
               "  <a href=\"/ajouter\">ajouter</a>"
    ajouter.exposed = True

cherrypy.quickstart(HelloWorld(), config='server.conf')

import os
from flask import Flask
from application.database import db
from application.config import *

app = Flask(__name__)
app.config.from_object(DebugConfig)
db.init_app(app)
app.app_context().push()

from application.controllers import *

#db.drop_all()
db.create_all()
db.session.commit()

if __name__== '__main__':
    app.run()

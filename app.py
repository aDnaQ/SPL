from flask import Flask
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db

from models import ParkplatzConfig


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/parkraumueberwachung"

db = SQLAlchemy(app)

@app.route("/")
def run_app():

    session: db.orm.scoping.scoped_session = db.session

    parkplatzConfig = session.query(ParkplatzConfig).order_by(ParkplatzConfig.ParkplatzID).all()

    return render_template("base.html",parkplatzConfig = parkplatzConfig)
 
 
app.run()
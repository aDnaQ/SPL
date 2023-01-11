from flask import Flask
from flask.templating import render_template
import sqlalchemy as db


app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/parkraumueberwachung"

 
@app.route("/")
def run_app():
    return render_template("base.html")
 
 
app.run()
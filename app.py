from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "fe67028f75429bd8aaf676201960ec9f"
ENV = "prod"

if ENV == "dev":
    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 
        "mysql+pymysql://root:" "@localhost/mortgage"    
else:
    app.debug = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://qmvrzjessgktbo:4e6f4e53a31faef60de2e82592131bbf98b66cfdc897a390eea3af79bca3fe99@ec2-174-129-253-104.compute-1.amazonaws.com:5432/dcr3ivcuj3u1te"
                            

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = "CalculationInfo"
    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(200))
    Price = db.Column(db.String(200))
    Deposit = db.Column(db.String(200))
    Bond = db.Column(db.String(200))
    Interest = db.Column(db.String(200))
    AmountDue = db.Column(db.String(200))

    def __init__(self, name, price, deposit, bond, interest, amountdue):
        self.Name = name
        self.Price = price
        self.Deposit = deposit
        self.Bond = bond
        self.Interest = interest
        self.AmountDue = amountdue



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():

    if request.method == "POST":
        name = request.form["nameFd"]
        price = request.form["priceFd"]
        deposit = request.form["depositFd"]
        bond = request.form["termFd"]
        interest = request.form["interestFd"]
        amountdue = request.form["amountFd"]

        if name == "" or price == "" or deposit == "" or bond == '''
                        or interest == ''':

            return render_template("index.html", message='''
                                    Please enter required fields''')

        data = Feedback(name, price, deposit, bond, interest, amountdue)
        db.session.add(data)
        db.session.commit()
        return render_template(
            "index.html",
            message="Thank you, your information is saved.",
            message2="You can do another calculation, if you want!",
        )


if __name__ == "__main__":

    app.run()

from datetime import datetime
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/qwe/board.sql'
db = SQLAlchemy(app)

class Board(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name_add_comment =db.Column(db.String, nullable=True)
    comment = db.Column(db.String, nullable=True)
    time_comment = db.Column(db.String, nullable=True)

@app.route("/",methods=["GET","POST"])
@app.route("/add_comment",methods=["GET","POST"])
def add_comment():

    if request.method == "POST":
        name_add_comment = request.form["name_add_comment"]
        comment = request.form["comment"]

        add_data = Board(

            name_add_comment=name_add_comment,
            comment=comment,
            time_comment=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        db.session.add(add_data)
        db.session.flush()
        db.session.commit()

        return render_template("index.html", items=Board.query.all())

    else:

        return render_template("index.html",items=Board.query.all())




if __name__ == "__main__":
    app.run(debug=True)
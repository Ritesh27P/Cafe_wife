from flask import Flask, render_template
import sqlalchemy as db
from sqlalchemy import Column
from sqlalchemy.orm import declarative_base

app = Flask(__name__)
Base = declarative_base()


class Cafe(Base):
    __tablename__ = 'cafedata'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, nullable=False)
    address = Column(db.String, nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

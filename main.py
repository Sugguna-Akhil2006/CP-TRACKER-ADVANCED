from flask import Flask, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base, mapped_column, Mapped

app = Flask(__name__)

Base = declarative_base()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cptracker.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class cptracker(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(100))
    email: Mapped[str] = mapped_column(db.String(100), unique=True)
    year: Mapped[str] = mapped_column(db.String(10))
    password: Mapped[str] = mapped_column(db.String(100))

with app.app_context():
    db.create_all()

@app.route("/")
def landing():
    return send_from_directory('frontend', 'landing_page.html')

@app.route("/analytics")
def analytics():
    return send_from_directory('frontend', 'analytics.html')

@app.route("/dashboard")
def dashboard():
    return send_from_directory('frontend', 'dashboard.html')

@app.route("/leaderboard")
def leaderboard():
    return send_from_directory('frontend', 'leaderboard.html')

@app.route("/login")
def login_page():
    return send_from_directory('frontend', 'login.html')

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    user = cptracker.query.filter_by(email=data["email"]).first()
    if user and user.password == data["password"]:
        return send_from_directory('frontend', 'dashboard.html')
        
    return send_from_directory('frontend', 'login.html' , error = "Invalid email or password")
    

@app.route("/notifications")
def notifications():
    return send_from_directory('frontend', 'notifications.html')

@app.route("/practice_planner")
def practice_planner():
    return send_from_directory('frontend', 'practice_planner.html')

@app.route("/profile")
def profile():
    return send_from_directory('frontend', 'profile.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.form
        new_user = cptracker(
            name=data["fullname"],
            email=data["email"],
            year=data["year"],
            password=data["password"]
        )
        db.session.add(new_user)
        db.session.commit()
        return send_from_directory('frontend', 'login.html')
    return send_from_directory('frontend', 'signup.html')

if __name__ == "__main__":
    app.run(debug=True)

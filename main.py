from flask import Flask, render_template, request, send_from_directory
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

# -------- ROUTES -------- #

@app.route("/")
def landing():
    return render_template("/frontend/landing_page.html")

@app.route("/analytics")
def analytics():
    return render_template("/frontend/analytics.html")

@app.route("/dashboard")
def dashboard():
    return render_template("/frontend/dashboard.html")

@app.route("/leaderboard")
def leaderboard():
    return render_template("/frontend/leaderboard.html")

@app.route("/login")
def login_page():
    return render_template("/frontend/login.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    with app.app_context():
        result = db.execute(db.select(cptracker).where(cptracker.email == data["email"], cptracker.password == data["password"])).first()
    if result:
        user = result[0]
        return render_template("/frontend/dashboard.html", user=user)
    
@app.route("/notifications")
def notifications():
    return render_template("/frontend/notifications.html")

@app.route("/practice_planner")
def practice_planner():
    return render_template("/frontend/practice_planner.html")

@app.route("/profile")
def profile():
    return render_template("/frontend/profile.html")

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
        return render_template("/frontend/login.html")

    return render_template("/frontend/signup.html")

# -------- RUN -------- #

if __name__ == "__main__":
    app.run(debug=True)
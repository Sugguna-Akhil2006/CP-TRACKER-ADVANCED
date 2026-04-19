#dependencies
from flask import Flask, send_from_directory


app = Flask(__name__)

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
def login():
    return send_from_directory('frontend', 'login.html')

@app.route("/notifications")
def notifications():
    return send_from_directory('frontend', 'notifications.html')

@app.route("/practice_planner")
def practice_planner():
    return send_from_directory('frontend', 'practice_planner.html')

@app.route("/profile")
def profile():
    return send_from_directory('frontend', 'profile.html')

@app.route("/signup")
def signup():
    return send_from_directory('frontend', 'signup.html')

if __name__ == "__main__":
    app.run(debug=True)
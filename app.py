from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)
current_session = {"otp": None}

# Master Credentials
ADMIN_ID = "gsbhadoriya"
ADMIN_KEY = "Gaurav@2002"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login_page')
def login_view():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def auth_logic():
    data = request.get_json()
    uid = data.get('id')
    pwd = data.get('pass')

    if uid == ADMIN_ID and pwd == ADMIN_KEY:
        otp = str(random.randint(111111, 999999))
        current_session["otp"] = otp
        return jsonify({"success": True, "otp": otp})
    return jsonify({"success": False, "message": "Invalid Access Key!"})

@app.route('/verify_otp', methods=['POST'])
def verify_logic():
    data = request.get_json()
    if data.get('otp') == current_session["otp"]:
        return jsonify({"success": True, "redirect": "/dashboard"})
    return jsonify({"success": False})

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
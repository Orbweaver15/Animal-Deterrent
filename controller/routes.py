"""HTTP routes for the web controller."""

from flask import jsonify, render_template

from config import VALID_ACTIONS, VALID_KEYS


def register_routes(app, arduino):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/<key>/<action>')
    def handle_key(key, action):
        if key in VALID_KEYS and action in VALID_ACTIONS:
            if arduino.ensure_connected() and arduino.is_open:
                command = f"{key}_{action}\n"
                try:
                    arduino.send(command)
                    print(f"📤 Sent: {command.strip()}")
                    return jsonify(success=True, command=command.strip())
                except Exception as e:
                    print(f"❌ Send failed: {str(e)}")
                    return jsonify(success=False, error=str(e)), 500
        return jsonify(success=False, error="Invalid command"), 400

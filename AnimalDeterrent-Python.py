from flask import Flask, render_template_string, jsonify
import serial
import time
from threading import Lock

app = Flask(__name__)

# Arduino setup
ARDUINO_PORT = '/dev/arduino_uno'  # Change to your actual port
arduino = None
serial_lock = Lock()

def setup_arduino():
    """Initialize or reconnect to Arduino"""
    global arduino
    try:
        with serial_lock:
            if arduino:
                arduino.close()
            arduino = serial.Serial(ARDUINO_PORT, 9600, timeout=1)
            time.sleep(2)  # Allow for Arduino reset
            print("✅ Arduino connected!")
            return True
    except serial.SerialException as e:
        print(f"❌ Arduino connection failed: {str(e)}")
        arduino = None
        return False

def check_arduino():
    """Auto-reconnect mechanism"""
    if not arduino or not arduino.is_open:
        print("⚠ Attempting Arduino reconnection...")
        return setup_arduino()
    return True

# Initial connection attempt
setup_arduino()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Robot Controller</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
            font-family: Arial, sans-serif;
        }
        .controls {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 15px;
            justify-content: center;
            margin: 50px auto;
            max-width: 330px;
        }
        .key {
            border: 3px solid #333;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            background: linear-gradient(145deg, #e6e6e6, #ffffff);
            transition: all 0.1s ease;
            user-select: none;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        }
        .key.active {
            background: linear-gradient(145deg, #4CAF50, #45a049);
            color: white;
            transform: scale(0.92);
            box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        }
        #w { 
            grid-column: 2; 
            grid-row: 1;
        }
        #a { 
            grid-column: 1; 
            grid-row: 2;
        }
        #s { 
            grid-column: 2; 
            grid-row: 2;
        }
        #d { 
            grid-column: 3; 
            grid-row: 2;
        }
        .status {
            text-align: center;
            margin: 20px;
            font-size: 18px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="status">Use WASD keys or click buttons to control the robot</div>
    <div class="controls">
        <div class="key" id="w">W</div>
		<div></div>
        <div class="key" id="a">A</div>
        <div class="key" id="s">S</div>
        <div class="key" id="d">D</div>
    </div>

    <script>
    const keys = {w: false, a: false, s: false, d: false};
    
    function handleKey(key, isPressed) {
        const element = document.getElementById(key);
        element.classList.toggle('active', isPressed);
        fetch(`/${key}/${isPressed ? 'press' : 'release'}`)
            .catch(err => console.log('Command failed:', err));
    }

    // Mouse events
    document.querySelectorAll('.key').forEach(btn => {
        btn.addEventListener('mousedown', () => handleKey(btn.id, true));
        btn.addEventListener('mouseup', () => handleKey(btn.id, false));
        btn.addEventListener('mouseleave', () => {
            if (keys[btn.id]) handleKey(btn.id, false);
        });
    });

    // Keyboard events
    document.addEventListener('keydown', (e) => {
        const key = e.key.toLowerCase();
        if (['w','a','s','d'].includes(key) && !keys[key]) {
            keys[key] = true;
            handleKey(key, true);
        }
    });

    document.addEventListener('keyup', (e) => {
        const key = e.key.toLowerCase();
        if (['w','a','s','d'].includes(key)) {
            keys[key] = false;
            handleKey(key, false);
        }
    });

    // Prevent context menu on long press
    document.addEventListener('contextmenu', (e) => e.preventDefault());
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/<key>/<action>')
def handle_key(key, action):
    if key in ['w', 'a', 's', 'd'] and action in ['press', 'release']:
        if check_arduino() and arduino.is_open:
            command = f"{key}_{action}\n"
            try:
                with serial_lock:
                    arduino.write(command.encode())
                print(f"📤 Sent: {command.strip()}")
                return jsonify(success=True, command=command.strip())
            except Exception as e:
                print(f"❌ Send failed: {str(e)}")
                return jsonify(success=False, error=str(e)), 500
    return jsonify(success=False, error="Invalid command"), 400

if __name__ == '__main__':
    try:
        print("🚀 Starting Flask server on http://0.0.0.0:5000")
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    finally:
        if arduino and arduino.is_open:
            arduino.close()
            print("🔌 Arduino connection closed")
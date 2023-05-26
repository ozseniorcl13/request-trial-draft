from flask import Flask
from observer import observer
import threading

app = Flask(__name__)

@app.route('/')
def api():
    print("API is running")
    return "API is running"

@app.route('/stop', methods=['POST'])
def stop():
    mensage = "Stoping training..."
    observer.stop_training = True
    
    print("Training stoped!!!")
    print("acc=99.99")
    return mensage

def run_api():
    app.run(host='0.0.0.0', port=5000)

def start_api():
    api_thread = threading.Thread(target=run_api)
    api_thread.start()

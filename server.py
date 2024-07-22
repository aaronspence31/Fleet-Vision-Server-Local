from flask import Flask
from flask_cors import CORS
from routes.obd import obd
from routes.model import model
from routes.stream import stream, start_streams, face_queue, body_queue, BATCH_SIZE, QUEUE_SIZE, PREDICTION_THRESHOLD
import threading
import tcp_server

app = Flask(__name__)
app.register_blueprint(obd)
app.register_blueprint(model)

CORS(app) #for React app

if __name__ == "__main__":
    # start TCP and Flask server on separate threads
    # tcp_thread = threading.Thread(target=tcp_server.start_tcp_server)
    # tcp_thread.start()

    # Start the streams
    start_streams()

    app.run(debug=True)

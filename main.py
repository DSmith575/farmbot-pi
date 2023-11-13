from flask import Flask, render_template, Response
from camera import VideoCamera

pi_camera = VideoCamera(flip=False)  # flip pi camera

# Creating a flask instance
app = Flask(__name__)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html') # Render HTML template

# Function to continuously get frames from the piCam
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Route for video feed
@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to take a picture when button is pressed
@app.route('/picture')
def take_picture():
    pi_camera.take_picture() # capture and save a photo
    return "None"

# Run the Flask app if script is executed
# Change the host to ip address required, can also add in port=x for specified port number
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
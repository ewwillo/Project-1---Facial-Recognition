import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import serial #For communicating to ardiuno
import time
import atexit


import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
from tensorflow.keras.layers import DepthwiseConv2D

class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop("groups", None)  # Ignore 'groups' argument
        super().__init__(*args, **kwargs)

# Setup Arduino communication
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Allow Arduino to initialize

def send_command(command):
    """Send a command to the Arduino."""
    arduino.write(f"{command}\n".encode('utf-8'))  # Send the command with a newline
    time.sleep(0.5)  # Allow Arduino to process
    response = arduino.readline().decode('utf-8').strip()  # Read the response
    return response

# Define cleanup function to run on program exit
def cleanup():
    """Cleanup function to turn off LEDs and close Arduino connection."""
    print("Sending EXIT command to Arduino...")
    send_command("EXIT")  # Send EXIT to turn off all LEDs
    arduino.close()
    print("Arduino connection closed.")

# Register cleanup function to execute when program exits
atexit.register(cleanup)
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, **kwargs):
        kwargs.pop("groups", None)  # Ignore 'groups' argument
        super().__init__(*args, **kwargs)

# Load the model
model = load_model("C:/Users/eww27/Downloads/converted_keras/keras_model.h5", compile=False,custom_objects={"DepthwiseConv2D": CustomDepthwiseConv2D})

# Load the labels
class_names = open("C:/Users/eww27/Downloads/converted_keras/labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224, 224) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Convert to numpy array and preprocess
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1  # Normalize

    # Predict
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]  # Remove any extra whitespace/newlines
    confidence_score = prediction[0][index]

    # Print results
    print("Class:", class_name[2:], "Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

   # **Send command to Arduino based on prediction**
    if class_name == "0 Face\n":
        print("Green")
        send_command("GREEN\n")  # Turn on green LED

    elif class_name == "1 No Face\n":
        print("Red")
        send_command("RED\n")  # Turn on red LED

    # Listen for escape key to exit
    keyboard_input = cv2.waitKey(1)

    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
# Project-1---Facial-Recognition

## Dataset
This project uses one model trained using Teachable Machine:
1. Facial Recognition Model – Identifies whether the user's face is present.

## References
- [Teachable Machine](https://teachablemachine.withgoogle.com/)
- [PySerial Documentation](https://pyserial.readthedocs.io/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Arduino Documentation](https://docs.arduino.cc/)

## Project Steps

1. **Train your Model:**
- Facial Recognition Model
   - Go to [Teachable Machine](https://teachablemachine.withgoogle.com/).
   - Create a new image model with two classes:
   - Class 1: Your face (upload multiple pictures).
   - Class 2: Other (covered face, background)
   - Export the model in TensorFlow/Keras format.
  
2. **Upload Arduino Code:**
- Open the Arduino IDE and upload the code that recieves commands from Python to control on your LEDs.
- The code should:
  -Turn on the green LED when your face is detected.
  -Turn on the red LED when no face is detected.
     
3. **Set Up Python-Arduino Communication:**
- Install the required Python libraries using: pip install pyserial tensorflow opencv-python
   - Use Python to send serial signals to the Arduino:
   - When the model detects your face, Python sends a signal to turn on the green LED.
   - When no face is detected, Python sends a signal to turn on the red LED.

4. **Test the System:**
- Train and test your facial recognition model.
- Test the communication between Python and Arduino to ensure the LED control works based on facial recognition

5. **Refine the Model (if needed):**
- Adjust the facial recognition model’s sensitivity if required.
- Ensure that there are no errors in code

## Versions Used:
- **Python:** 3.13.2
- **TensorFlow:** 2.18
- **Keras:** Latest
- **OpenCV:** 4.11
- **PySerial:** 3.5
- **Arduino IDE:** Latest
- **Hardware:** Arduino Mega 2560

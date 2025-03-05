const int redPin = 4;
const int greenPin = 2;

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);

  // Ensure LEDs are off by default
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readStringUntil('\n'); // Read command
    msg.trim(); // Remove any extra spaces or newlines

    if (msg == "GREEN") {
      digitalWrite(greenPin, HIGH); // Turn green LED on
      digitalWrite(redPin, LOW); // Turn red LED off
      Serial.println("Green Light is on");
    }
    else if (msg == "RED") {
      digitalWrite(redPin, HIGH); // Turn red LED on
      digitalWrite(greenPin, LOW); // Turn green LED off
      Serial.println("Red Light is on");
    } 
   else if (msg == "EXIT") {
  // Turn off all LEDs
  digitalWrite(greenPin, LOW);
  digitalWrite(redPin, LOW);

  for (int i = 0; i < 5; i++) {
    digitalWrite(redPin, HIGH);
    delay(100);
    digitalWrite(redPin, LOW);
    delay(100);
  }
  Serial.println("Exiting...");
  while (true); // Stop the loop
}

    
  }
}
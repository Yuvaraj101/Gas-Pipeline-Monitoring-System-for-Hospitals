const int pirPin = 2;
const int ldrPin = 36;
const int ledPin = 5;
const int buzzerPin = 4;
const int ledBrightness = 255;  

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int pirValue = digitalRead(pirPin);
  int ldrValue = analogRead(ldrPin);
  int lightIntensity = map(ldrValue, 0, 4095, 0, 100);  

//the led will glow and the buzzer is triggered when motion is detected
  if (pirValue == HIGH) {
    digitalWrite(ledPin, ledBrightness);  
    digitalWrite(buzzerPin, HIGH);
    delay(500);
    digitalWrite(buzzerPin, LOW);
  } 
  //otherwise the led will glow depending on the intensity from the LDR sensor
  else {
    digitalWrite(ledPin, (lightIntensity * ledBrightness) / 100);  
  }

  Serial.print("Light Intensity: ");
  Serial.print(lightIntensity);
  Serial.println("%");
  delay(1000);
}

void setup() {
  // put your setup code here, to run once:

  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  SerialUSB.begin(9600);
  while (!SerialUSB) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


  Serial.println("Goodnight moon!");

}

void loop() {
  // put your main code here, to run repeatedly:
  
  if (SerialUSB.available()) {
    SerialUSB.println("Hello");
    SerialUSB.println(SerialUSB.read());
  }

}

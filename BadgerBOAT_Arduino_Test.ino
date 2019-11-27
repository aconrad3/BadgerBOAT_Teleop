int incomingByte = 0; // for incoming serial data
int dcVal = 190;
void setup() {
  // start serial port at 9600 bps:
  Serial.begin(115200);
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(9, OUTPUT);
  analogWrite(9, 187);
  while (!Serial) {
    ; // wait for serial port to connect.
  }

}

void loop() {
  char buffer[16];
   //if we get a command, turn the LED on or off:
   //if (Serial.available() > 0) {
    int size = Serial.readBytesUntil('\n', buffer, 12);
    Serial.println(buffer[0]);
    
    if (buffer[0] == 'W') {
      analogWrite(9, 254);
      //int size = Serial.readBytesUntil('\n', buffer, 12);

    }
    else if (buffer[0] == 'S') {
      analogWrite(9, 63);

    }
    else if (buffer[0] == 'A') {
      analogWrite(9, 220);
    }
    else if (buffer[0] == 'D') {
      analogWrite(9, 150);
    }else{
      analogWrite(9, 187);
    }



  

    
  }
//}

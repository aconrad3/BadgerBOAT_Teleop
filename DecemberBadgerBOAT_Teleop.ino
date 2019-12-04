int dcVal = 187;

void setup() 
{
  pinMode(13,OUTPUT);  
  pinMode(9, OUTPUT);
  analogWrite(9, dcVal);
  Serial.begin(115200);
  
}

void loop() 
{
  if(Serial.available() > 0)
  {
    char inputChar = Serial.read();
    //Serial.print(inputChar);
    if(inputChar == 's')
    {
      //Serial.print("S detect!");
      analogWrite(9, 63);
    }
    else if(inputChar == 'a'){
      //Serial.print("A detect!");
      analogWrite(9, 220);
    }
    else if(inputChar == 'w'){
      //Serial.print("W detect!");
      analogWrite(9, 254);
    }
    else if(inputChar == 'd'){
     // Serial.print("D detect!");
       analogWrite(9, 150);
    }else{
      analogWrite(9, 187);
    }
  }  

    else
    {
      digitalWrite(13,LOW);
    }
}

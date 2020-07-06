char serialData;
int pin = 10;

void setup() {
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if(Serial.available() > 0){
    serialData = Serial.read();
    Serial.print(serialData);

    if(serialData == '1')
    {
      digitalWrite(pin, HIGH);
    }
    else if (serialData == '0')
    {
      digitalWrite(pin, LOW);
    }
 }
}

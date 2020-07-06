char serialData;

// Motor A
 
int enA = 3;
int in1 = 7;
int in2 = 6;
 
// Motor B
 
int enB = 2;
int in3 = 5;
int in4 = 4;

void setup() {

  // Set all the motor control pins to outputs

  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  Serial.begin(9600);
 
}

void move()
 
{
 
  // This function will run the motors in both directions at a fixed speed
 
  // Turn on motor A
 
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
 
  // Set speed to 200 out of possible range 0~255
 
  analogWrite(enA, 100);
 
  // Turn on motor B
 
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
 
  // Set speed to 200 out of possible range 0~255
 
  analogWrite(enB, 100);

}

void stop()

{

 
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);  
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

}


void loop()

{

  if(Serial.available() > 0)
  {
    serialData = Serial.read();
    Serial.print(serialData);

    if(serialData == '1')
    {
      move();
    }
    else if (serialData == '0')
    {
      stop();
    }
 }
 
}

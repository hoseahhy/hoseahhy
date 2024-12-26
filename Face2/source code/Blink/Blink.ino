/*
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
*/

char serialData;
int LedPin = 13;

void setup() 
{
  pinMode(LedPin, OUTPUT);  
  Serial.begin(9600);
}

void loop() 
{
  if(Serial.available() > 0)
  {
    serialData = Serial.read();
    Serial.print(serialData);

    if(serialData == '1')
      digitalWrite(LedPin, HIGH);
    else if(serialData == '0')
      digitalWrite(LedPin, LOW);
  }
}
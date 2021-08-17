/*
Analog 49E Hall Effect sensor test

Basic code for reading the analog output of the 49E hall effect sensor. 
Sensor is connected to A0, but can be any analog input pin.
*/
const int AnalogPin = A0;
const float GAUSS_PER_STEP = 2.57;  // Sensor outputs approx 1.9mV / Gauss.  
                                    // ADC step is about 4.89mV / Step for 5V operation. 
float rawValue = 0.0;               // Raw ADC Reading
float gaussValue = 0.0;
float zeroLevel = 0; //515.0;  // Adjust value as needed to get zero rawValue output with no magnetic field.
const float threshold = 0.4;
const float pi = 3.1415;
const float tyrelength = 0.2;
int count = 0;
//===============================================================================
//  Initialization
//===============================================================================

void calibration()
{
  delay(2000);
  zeroLevel = analogRead(AnalogPin);
  delay(2000);
}

float total_length(int& counts)
{
  return counts*tyrelength;
}
void setup() 
{ 
  pinMode (AnalogPin, INPUT);
  Serial.begin(9600);         // Set comm speed for debug window messages
  calibration();
}

//===============================================================================
//  Main
//===============================================================================
void loop() 
{
  
  rawValue = analogRead (AnalogPin) - zeroLevel;  // Output normalized to '0' with no field present
  Serial.print ("Reading Raw: ");
  Serial.println (rawValue);

  if (abs(rawValue) > threshold){
    count = count + 1;
  }
  // Reading positive relative to the South Pole, the North Pole negative
  //gaussValue = rawValue * GAUSS_PER_STEP;
  //Serial.print ("Reading in Gauss: ");
  //Serial.println (gaussValue);
  Serial.print("Counts: ");
  Serial.println(count);
  Serial.print("total m: ");
  Serial.println(total_length(count));
  delay (200);
}

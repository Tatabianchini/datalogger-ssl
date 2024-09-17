#include <SimpleFOC.h>

// REMEMBER TO CHECK GPIO NUM
MagneticSensorPWM sensor = MagneticSensorPWM(GPIO_NUM_15, 2, 922);
void doPWM(){sensor.handlePWM();}

void setup() {
  // monitoring port
  Serial.begin(115200);
  
  // initialise encoder hardware
  sensor.init();
  // hardware interrupt enable
  sensor.enableInterrupt(doPWM);

  Serial.println("Encoder ready");
  _delay(1000);
}

void loop() {
  // IMPORTANT
  // read sensor and update the internal variables
  sensor.update();
  // display the angle and the angular velocity to the terminal
  Serial.print(sensor.getAngle());
  Serial.print("\t");
  Serial.println(sensor.getVelocity());
}

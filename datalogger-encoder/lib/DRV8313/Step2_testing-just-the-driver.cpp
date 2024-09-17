#include <SimpleFOC.h>
// BLDC driver instance
BLDCDriver3PWM driver = BLDCDriver3PWM(GPIO_NUM_19, GPIO_NUM_18, GPIO_NUM_5, GPIO_NUM_17);


void setup() {
  // pwm frequency to be used [Hz]
  driver.pwm_frequency = 20000;
  // power supply voltage [V]
  driver.voltage_power_supply = 12;
  // Max DC voltage allowed - default voltage_power_supply
  driver.voltage_limit = 12;

  // driver init
  driver.init();

  // enable driver
  driver.enable();

  _delay(1000);
}

void loop() {
    // setting pwm (A: 3V, B: 1V, C: 5V)
    // When measuring the voltage on each phase with a multimeter you should get these values
    driver.setPwm(3,1,5);
}


#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
#define SERVO_MIN  150
#define SERVO_RANGE 450 // This is the 'maximum' pulse length count (out of 4096)
#define SERVO_FREQ 50 // Analog servos run at ~50 Hz updates

#define DATA_RANGE 0xfe

void setup() {
  Serial.begin(9600);
  Serial.println("I AWAKEN");

  pwm.begin();
  /*
   * In theory the internal oscillator (clock) is 25MHz but it really isn't
   * that precise. You can 'calibrate' this by tweaking this number until
   * you get the PWM update frequency you're expecting!
   * The int.osc. for the PCA9685 chip is a range between about 23-27MHz and
   * is used for calculating things like writeMicroseconds()
   * Analog servos run at ~50 Hz updates, It is importaint to use an
   * oscilloscope in setting the int.osc frequency for the I2C PCA9685 chip.
   * 1) Attach the oscilloscope to one of the PWM signal pins and ground on
   *    the I2C PCA9685 chip you are setting the value for.
   * 2) Adjust setOscillatorFrequency() until the PWM update frequency is the
   *    expected value (50Hz for most ESCs)
   * Setting the value here is specific to each individual I2C PCA9685 chip and
   * affects the calculations for the PWM update frequency. 
   * Failure to correctly set the int.osc value will cause unexpected PWM results
   */
  pwm.setOscillatorFrequency(27000000 * 0.93);
  pwm.setPWMFreq(SERVO_FREQ);  // Analog servos run at ~50 Hz updates

  delay(10);
  for(int i = 0; i < 8; i++) {
    pwm.setPWM(i, 0, SERVO_RANGE / 2 + SERVO_MIN);
  }
}

void setMotor(){
  if (Serial.available() == 0) {
    return;
  }

  String in = Serial.readStringUntil(0xff);
  if (in.length() != 2) {
    // invalid message
    Serial.println("invalid message");
    return;
  }

  int index = in[0];
  int val = in[1];
  val = val * SERVO_RANGE / DATA_RANGE + SERVO_MIN;
  
  pwm.setPWM(index, 0, val);
}

void loop(){
  setMotor();
}


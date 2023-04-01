/* referred to:
 * https://arduinogetstarted.com/tutorials/arduino-neopixel-led-strip
 * and https://adafruit.github.io/Adafruit_NeoPixel/html/class_adafruit___neo_pixel.html
 * for setting up neopixel
 *
 * https://docs.arduino.cc/built-in-examples/digital/toneMelody
 * for speaker
 * 
 * https://docs.arduino.cc/learn/electronics/servo-motors
 * for servo
 */

//#include <Adafruit_NeoPixel.h>
#include <Adafruit_DotStar.h>
#include <SPI.h>
#include <Servo.h>

#define DELAY_INTERVAL 2000

// //NEOPIXEL
#define NUM_PIXELS 72
#define PIN_DATA_NEO_PIXEL 13
#define PIN_CLK_NEO_PIXEL 11

//SPEAKER
#define PIN_PIEZO 3
#define NOTE_CS2 69
#define NOTE_C4  262
#define NOTE_E4  330
#define NOTE_G4  392

#define NOTE_NUM 3
#define NOTE_DUR (1000/8)
#define NOTE_PAUSE (NOTE_DUR * 1.30)

// SERVO
#define PIN_SERVO_MAIN 10
#define PIN_SERVO_TRASH 9
#define PIN_SERVO_RECY 6

#define ANGLE_CENTER 90
#define ANGLE_RIGHT 0
#define ANGLE_LEFT 180
#define ANGLE_DIFF 40

// //ULTRASOUND DISTANCE SENSORS
// #define PIN_UDS_TRASH 5
// #define PIN_UDS_RECY 3
// #define DIS_THRESHOLD 5


//**using strip since singular neopixel component in tinkercad not lighting up
Adafruit_DotStar strip(NUM_PIXELS, DOTSTAR_BGR);
uint32_t green = strip.Color(0, 150, 0);
uint32_t red = strip.Color(150, 0, 0);

//setting up tones for buzzer
int correct_melody[] = {NOTE_C4, NOTE_E4, NOTE_G4};
int incorrect_melody[] = {NOTE_CS2, NOTE_CS2, NOTE_CS2};

//main servo
Servo servo_main;
//locks
Servo servo_trash;
Servo servo_recy;

//jetson model output == 0: false (trash)
//jetson model output == 1: true (recycling)
int model_output;


//init
void setup(){
  //init neopixel
  strip.begin();
  strip.show();
  
  //init servo
  servo_main.attach(PIN_SERVO_MAIN);
  servo_trash.attach(PIN_SERVO_TRASH);
  servo_recy.attach(PIN_SERVO_RECY);
  
  //center platform
  servo_main.write(ANGLE_CENTER);
  delay(DELAY_INTERVAL/2);

  // lock platform
  servo_trash.write(ANGLE_CENTER);
  servo_recy.write(ANGLE_CENTER);
  delay(DELAY_INTERVAL/2);
  //open serial communication
  Serial.begin(9600);
  //Serial.flush();
  //Serial.println("Setup...\n");
}

void loop(){
  //Serial.print("New Loop Iteration...\n");
  //for reading output from jetson
  //while (!Serial.available()){}
  if (Serial.available() > 0)
  {
    //Serial.print("New output from Jetson! \n");
    //char c = Serial.read();
    //Serial.print(c);
    //Serial.write(c);
    model_output = Serial.readString().toInt();//atoi(c);
    
    Serial.write(model_output);
    //Serial.flush();
    
    if (model_output == 1){
      //Serial.print("Correct, is recyclable!\n");
    
      //NEOPIXEL = green  
      strip.fill(green, 0, NUM_PIXELS);
      strip.setBrightness(10);
      strip.show();
    
      //PIEZO
      for (int i = 0; i < NOTE_NUM; i++){
        tone(PIN_PIEZO, correct_melody[i], NOTE_DUR); 
        delay(NOTE_PAUSE);
        noTone(PIN_PIEZO);
        }
        
      //SERVO LOCK RECY - unlock recycle
      servo_recy.write(ANGLE_RIGHT);
      delay(DELAY_INTERVAL/2);

      //SERVO MAIN
      servo_main.write(ANGLE_RIGHT + ANGLE_DIFF);
    
    }
    else if (model_output == 0){
      //Serial.print("Incorrect, is trash\n");

      //NEOPIXEL = red   
      strip.fill(red, 0, NUM_PIXELS);
      strip.setBrightness(10);
      strip.show();
      
      //PIEZO
      for (int i = 0; i < NOTE_NUM; i++){
        tone(PIN_PIEZO, incorrect_melody[i], NOTE_DUR); 
        delay(NOTE_PAUSE);
        noTone(PIN_PIEZO);
      }
            
      //SERVO LOCK TRASH - unlock trash
      servo_trash.write(ANGLE_LEFT);
      delay(DELAY_INTERVAL/2);

      //SERVO MAIN
      servo_main.write(ANGLE_LEFT - ANGLE_DIFF);
    }
    else{
      Serial.write("incorrect");
    }

    delay(DELAY_INTERVAL);
    strip.clear();
    strip.show();
    delay(DELAY_INTERVAL/2);
    
    // set platform back to center
    servo_main.write(ANGLE_CENTER);
    delay(DELAY_INTERVAL/2);
    
    //lock trash and recycle
    servo_trash.write(ANGLE_CENTER);
    servo_recy.write(ANGLE_CENTER);
    
    delay(DELAY_INTERVAL);
    model_output = NULL; 
    while(Serial.available() > 0) {
      Serial.read();
    } 
    
  }  
}
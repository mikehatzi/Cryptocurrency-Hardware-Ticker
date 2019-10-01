#include <Wire.h>
#include "FastLED.h"
#define NUM_LEDS 100
#define DATA_PIN 5
#define SLAVE_ADDRESS 0x04

CRGB leds[NUM_LEDS];
int number[2] = {0, 0};
int state = 0;
bool pause = true;

int dispNum = 0;
int currentPosition[4] = {0, 0, 0, 0};
int prevPosition[4] = {0, 0, 0, 0};

void setup()
{
  delay(100);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(200);

  for (int i = 0; i < NUM_LEDS; i++)
    leds[i] = 0x000000;
  
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  Serial.println("Ready!");
  ETH();
  FastLED.show();
}

void loop()
{
  if (pause == false)
  {
    Serial.println("I MADE IT TO DEBUG POINT 1");
    deconstruct();
    assemble();
    pause = true;
  }
}

void receiveData(int byteCount)
{
  while(Wire.available())
  {
    if (state == 0)
    {
      number[0] = Wire.read();
      Serial.print("first byte: ");
      Serial.println(number[0]);
      state = 1;
    }
    else
    {
      number[1] = Wire.read();
      Serial.print("second byte: ");
      Serial.println(number[1]);
      pause = false;
      state = 0;
      parseData();
    }
  }
}

void sendData()
{
  Wire.write("You have requested something?");
}

void parseData()
{
  number[1] = number[1] << 8;
  dispNum = number[0] + number[1];
  Serial.print("The full number sent is: ");
  Serial.println(dispNum);
}

void deconstruct()
{
  int factor;
  if (dispNum >= 1000)
    factor = -1;
  else
  {
    factor = 0;
    currentPosition[0] = -1;
  }
  //Serial.println("I MADE IT TO DEBUG POINT 2");
  Serial.print("dispNum = ");
  Serial.println(dispNum);
  Serial.print("factor = ");
  Serial.println(factor);
  for (int i = 3; i > factor; i--)
  {
    currentPosition[i] = dispNum % 10;
    dispNum /= 10;
  }
}

void assemble()
{
  if (currentPosition[0] != prevPosition[0])
    construct(currentPosition[0], 29, 0x00FF00);
  if (currentPosition[1] != prevPosition[1])
    construct(currentPosition[1], 27, 0x0000FF);
  if (currentPosition[2] != prevPosition[2])
    construct(currentPosition[2], 24, 0x00FF00);
  if (currentPosition[3] != prevPosition[3])
    construct(currentPosition[3], 21, 0x0000FF);
    
  for (int i = 0; i < 4; i++)
    prevPosition[i] = currentPosition[i];
}

void construct(int value, int offset, int color)
{
  leds[offset + 21] = 0;
  leds[offset + 20] = 0;
  leds[offset + 19] = 0;
  leds[offset + 11] = 0;
  leds[offset + 10] = 0;   
  leds[offset + 9] = 0;
  leds[offset + 1] = 0;
  leds[offset] = 0;
  leds[offset - 1] = 0;
  leds[offset - 9] = 0;
  leds[offset - 10] = 0;
  leds[offset - 11] = 0;
  leds[offset - 19] = 0;
  leds[offset - 20] = 0;
  leds[offset - 21] = 0;
  
  switch(value)
  {
    case 0:
        leds[offset + 21] = color;
        leds[offset + 20] = color;
        leds[offset + 19] = color;
        leds[offset + 11] = color;
        leds[offset + 9] = color;
        leds[offset + 1] = color;
        leds[offset - 1] = color;
        leds[offset - 9] = color;
        leds[offset - 11] = color;
        leds[offset - 19] = color;
        leds[offset - 20] = color;
        leds[offset - 21] = color;
        break;
        
    case 1:
        leds[offset + 20] = color;
        leds[offset + 10] = color;    
        leds[offset] = color;
        leds[offset - 10] = color;
        leds[offset - 20] = color;
        break;

    case 2:
        leds[offset + 21] = color;
        leds[offset + 20] = color;
        leds[offset + 19] = color;   
        leds[offset + 9] = color;
        leds[offset + 1] = color;
        leds[offset] = color;
        leds[offset - 1] = color;
        leds[offset - 9] = color;
        leds[offset - 19] = color;
        leds[offset - 20] = color;
        leds[offset - 21] = color;
        break;

    case 3:
        leds[offset + 21] = color;
        leds[offset + 20] = color;
        leds[offset + 19] = color;   
        leds[offset + 9] = color;
        leds[offset + 1] = color;
        leds[offset] = color;
        leds[offset - 1] = color;
        leds[offset - 11] = color;
        leds[offset - 19] = color;
        leds[offset - 20] = color;
        leds[offset - 21] = color;
        break;

    case 4:
        leds[offset + 21] = color;
        leds[offset + 19] = color;
        leds[offset + 11] = color;    
        leds[offset + 9] = color;
        leds[offset + 1] = color;
        leds[offset] = color;
        leds[offset - 1] = color;
        leds[offset - 11] = color;
        leds[offset - 21] = color;
        break;

    case 5:
        leds[offset + 21] = color;
        leds[offset + 20] = color;
        leds[offset + 19] = color;
        leds[offset + 11] = color;
        leds[offset + 1] = color;
        leds[offset] = color;
        leds[offset - 1] = color;
        leds[offset - 11] = color;
        leds[offset - 19] = color;
        leds[offset - 20] = color;
        leds[offset - 21] = color;
        break;

    case 6:
        leds[offset + 21] = color;
        leds[offset + 20] = color;
        leds[offset + 19] = color;
        leds[offset + 11] = color;
        leds[offset + 1] = color;
        leds[offset] = color;
        leds[offset - 1] = color;
        leds[offset - 9] = color;
        leds[offset - 11] = color;
        leds[offset - 19] = color;
        leds[offset - 20] = color;
        leds[offset - 21] = color;
        break;

    case 7:
        leds[offset + 21] = color;
        leds[offset + 20] = color;
        leds[offset + 19] = color;   
        leds[offset + 9] = color;
        leds[offset - 1] = color;
        leds[offset - 11] = color;
        leds[offset - 21] = color;
        break;

    case 8:
        leds[offset + 21] = color;
        leds[offset + 20] = color;
        leds[offset + 19] = color;
        leds[offset + 11] = color;    
        leds[offset + 9] = color;
        leds[offset + 1] = color;
        leds[offset] = color;
        leds[offset - 1] = color;
        leds[offset - 9] = color;
        leds[offset - 11] = color;
        leds[offset - 19] = color;
        leds[offset - 20] = color;
        leds[offset - 21] = color;
        break;
        
    case 9:
        leds[offset + 21] = color;
        leds[offset + 20] = color;
        leds[offset + 19] = color;
        leds[offset + 11] = color;
        leds[offset + 9] = color;
        leds[offset + 1] = color;
        leds[offset] = color;
        leds[offset - 1] = color;
        leds[offset - 11] = color;
        leds[offset - 21] = color;
        break;
        
    default:
        leds[offset] = 0xFF0000;
  }
  FastLED.show();
}

void ETH()
{
  leds[66] = 0xCD00FF;
  leds[67] = 0xCD00FF;
  leds[68] = 0xCD00FF;
  leds[78] = 0xCD00FF;   
  leds[86] = 0xCD00FF;
  leds[87] = 0xCD00FF;
  leds[88] = 0xCD00FF;
  leds[96] = 0xCD00FF;
  leds[97] = 0xCD00FF;
  leds[98] = 0xCD00FF;
  leds[64] = 0xFFA2E4;
  leds[74] = 0xFFA2E4;
  leds[84] = 0xFFA2E4;
  leds[93] = 0xFFA2E4;
  leds[94] = 0xFFA2E4;
  leds[95] = 0xFFA2E4;
  leds[60] = 0xCD00FF;
  leds[62] = 0xCD00FF;
  leds[70] = 0xCD00FF;
  leds[72] = 0xCD00FF;
  leds[80] = 0xCD00FF;
  leds[81] = 0xCD00FF;
  leds[82] = 0xCD00FF;
  leds[90] = 0xCD00FF;
  leds[92] = 0xCD00FF;
}

# Cryptocurrency-Hardware-Ticker

The purpose of this project is to take live cryptocurrency price data from the GDAX database and display it on an LED Matrix. The code in particular uses the currency "Ethereum" as an example. The hardware involved in this project includes a Raspberry Pi 3, an Arduino Uno, and a custom made 10x10 LED Matrix using WS2812b LEDs.

The code from GDAX should be imported and run on the Raspberry Pi.
The code from LED Matrix Control should be imported and run on the Arduino Uno.

Make an I2C connection between the Raspberry Pi and Arduino by performing the following connections:

Raspberry Pi GPIO/BCM 2 - Arduino A4
Raspberry Pi GPO/BCM 3 - Arduino A5

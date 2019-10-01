import smbus
import time
import gdax

public_client = gdax.PublicClient()
bus = smbus.SMBus(1)

address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
	return -1
	
while True:
	Ether = public_client.get_product_ticker(product_id='ETH-USD')
	price = Ether['price']
	print("The price of either is (decimal): ", price)
	price = int(float(price))
	print("The price of Ether is (integer): ", price)
	if not price:
		continue
		
	num1 = price & 255
	num2 = price >> 8
	
	print("Sending first part...")
	writeNumber(num1)
	time.sleep(1)
	
	print("Sending second part...")
	writeNumber(num2)
	time.sleep(1)

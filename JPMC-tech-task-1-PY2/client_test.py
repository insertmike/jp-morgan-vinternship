import unittest
from client import getDataPoint
from client import getRatio

class ClientTest(unittest.TestCase):
	def test_getDataPoint_calculatePrice(self):
		#""" ------------ Build ------------ """
		quotes = [
		{'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
		{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]	
		#""" ------------ Act && Assert ------------ """
		for quote in quotes:
			stock = quote['stock']
			bid_price = float(quote['top_bid']['price'])
			ask_price = float(quote['top_ask']['price'])
			price = ( bid_price + ask_price ) / 2
			self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price ))
    

	def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
		#""" ------------ Build ------------ """
		quotes = [
		{'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
		{'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
		]
		#""" ------------ Act && Assert ------------ """
		for quote in quotes:
			stock = quote['stock']
			bid_price = float(quote['top_bid']['price'])
			ask_price = float(quote['top_ask']['price'])
			price = ( bid_price + ask_price ) / 2
			self.assertEqual(getDataPoint(quote), (stock, bid_price, ask_price, price ))
    
	def test_getRatio_calculateRatioWithNonZeroNumbers(self):
		price_a = 121.2
		price_b = 119.2
		#""" ------------ Act && Assert ------------ """
		self.assertEqual(getRatio(price_a, price_b), ( price_a / price_b ) )
		
	def test_getRatio_calculateRatioWithZeroDenominator(self):
		#""" ------------ Build ------------ """
		price_a = 1
		price_b = 0
		#""" ------------ Act && Assert ------------ """
		self.assertEqual(getRatio(price_a, price_b), -1 )


if __name__ == '__main__':
	unittest.main()

import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))
      #self.asserEqual (      actual       ,                                                          expected                                                               )
  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_edgeCases(self):
    quotes = [
        {'top_ask': {'price': 0, 'size': 10}, 'timestamp': '2022-01-01 12:00:00', 'top_bid': {'price': 0, 'size': 5}, 'id': '0.123456789', 'stock': 'XYZ'},
        {'top_ask': {'price': 1e6, 'size': 3}, 'timestamp': '2022-01-01 12:00:00', 'top_bid': {'price': 1e6, 'size': 8}, 'id': '0.987654321', 'stock': 'PQR'},
        {'top_ask': {'price': 50.0, 'size': 7}, 'timestamp': '2022-01-01 12:00:00', 'top_bid': {'price': 49.99, 'size': 15}, 'id': '0.555555555', 'stock': 'ABC'}
    ]

    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))

if __name__ == '__main__':
    unittest.main()

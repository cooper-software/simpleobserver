import unittest
from mock import Mock
import simpleobserver

class TestSubject(unittest.TestCase):

	def test_invalid_event(self):
		"""Raises an error if attempting to add a listener to an unregistered event"""
		subject = simpleobserver.Subject()

		with self.assertRaises(AssertionError):
			subject('foo', None)


	def test_add_listener(self):
		"""Can add a listener to an allowed event"""
		foo_listener = Mock()
		bar_listener = Mock()
		subject = simpleobserver.Subject('foo', 'bar', 'baz')
		subject('foo', foo_listener)
		subject('bar', bar_listener)

		self.assertEqual(foo_listener.call_count, 0)
		self.assertEqual(bar_listener.call_count, 0)

		subject.fire('foo', 123, 456)
		foo_listener.assert_called_once_with(123, 456)
		self.assertEqual(bar_listener.call_count, 0)

		subject.fire('bar', 'skidoo', 23)
		foo_listener.assert_called_once_with(123, 456)
		bar_listener.assert_called_once_with('skidoo', 23)
		
		
if __name__ == "__main__":
	unittest.main()
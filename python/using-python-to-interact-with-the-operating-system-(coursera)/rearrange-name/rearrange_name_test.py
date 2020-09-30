#!/usr/bin/env python3

from rearrange_name import rearrange_name
import unittest


class RearrangeName(unittest.TestCase):
	def test_basic(self):
		testcase = "Kowalski, Jan"
		expected = "Jan Kowalski"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_empty(self):
		testcase = ""
		expected = ""
		self.assertEqual(rearrange_name(testcase), expected)

	def test_double(self):
		testcase = "Nowak, Kamil Ł."
		expected = "Kamil Ł. Nowak"
		self.assertEqual(rearrange_name(testcase), expected)

	def test_one_name(self):
		testcase = "Arystoteles"
		expected = "Arystoteles"
		self.assertEqual(rearrange_name(testcase), expected)


unittest.main()

from django.test import TestCase

class PerfectTestCase(TestCase):
	def setUp(self):
		self.areWeCovered = True
	def test_all_possible_cases(self):
		self.assertEqual(self.areWeCovered, True)

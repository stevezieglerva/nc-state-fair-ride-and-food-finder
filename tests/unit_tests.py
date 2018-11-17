import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from create_page import *



class TestMethods(unittest.TestCase):
	def test_read_csv_file__valid_filename__990_row_returned(self):
		# Arrange

		# Act
		data_filename = os.path.join("..", "data", "nc_state_fair_vendor_data.csv")
		result = read_csv_file(data_filename)

		# Assert
		self.assertGreater(len(result), 1)
		self.assertLess(len(result), 100)

	def test_read_template__valid_filename__string_has_html(self):
		# Arrange

		# Act
		template_filename = os.path.join("..", "template", "template.html")
		result = read_template(template_filename)

		# Assert
		self.assertTrue("<html>" in result)

	def test_create_page__valid_template_and_data__valid_populated_html(self):
		# Arrange
		template_filename = os.path.join("..", "template", "template.html")
		template = read_template(template_filename)
		data_filename = os.path.join("..", "data", "nc_state_fair_vendor_data.csv")
		data = read_csv_file(data_filename)
		print("test_create_page__valid_template_and_data__valid_populated_html")

		# Act
		result = create_page(template, data)

		# Assert
		self.assertTrue("<html>" in result)
		self.assertTrue("Davis Concessions" in result)

	def test_get_sorted_unique_column_values__valid_column_name__returns_values(self):
		# Arrange
		template_filename = os.path.join("..", "template", "template.html")
		template = read_template(template_filename)
		data_filename = os.path.join("results_sample.csv")
		data = read_csv_file(data_filename)

		# Act
		result = get_sorted_unique_column_values(data, "FOODTYPE")

		# Assert
		self.assertEqual(result, ['Confections', 'Fair Food', 'Ice Cream'] )

		

if __name__ == '__main__':
	unittest.main()		



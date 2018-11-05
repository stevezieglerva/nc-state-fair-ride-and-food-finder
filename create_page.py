
import csv


def read_csv_file(filename):
	results = []
	with open(filename, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		count = 0
		for row in csv_reader:
			count = count + 1
			results.append(row)
	return results


def get_unique_column_values(data, column_name):
	unique_list = {}
	for row in data:
		col_val = row[column_name]
		if col_val not in unique_list:
			unique_list[col_val] = 1
		else:
			unique_list[col_val] = unique_list[col_val] + 1		
	return unique_list


def read_template(filename):
	data = ""
	with open(filename, "r") as template_file:
		data = template_file.read()
	return data


def create_page(template, data):
	list_html = ""
	for row in data:
		print(row)
		list_html = list_html + row["CONTRACT"] + "<br/>\n"
	new_page = template.replace("<list-here/>", list_html)
	return new_page





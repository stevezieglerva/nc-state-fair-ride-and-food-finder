
import csv
import os
import datetime
import re


def read_csv_file(filename):
	results = []
	with open(filename, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		count = 0
		for row in csv_reader:
			count = count + 1
			if "FOODTYPE" in row:
				if row["FOODTYPE"] != "":
					results.append(row)
	return results


def get_sorted_unique_column_values(data, column_name):
	unique_list = {}
	for row in data:
		col_val = row[column_name]
		if col_val not in unique_list:
			unique_list[col_val] = 1
		else:
			unique_list[col_val] = unique_list[col_val] + 1		
	sorted_unique_list = sorted(unique_list.keys())	
	return sorted_unique_list

def get_sorted_unique_column_values_and_counts(data, column_name):
	unique_list = {}
	for row in data:
		col_val = row[column_name]
		if col_val not in unique_list:
			unique_list[col_val] = 1
		else:
			unique_list[col_val] = unique_list[col_val] + 1		
	sorted_unique_keys = sorted(unique_list.keys())	
	sorted_unique_list = {}
	for key in sorted_unique_keys:
		sorted_unique_list[key] = unique_list[key]
	return sorted_unique_list


def read_template(filename):
	data = ""
	with open(filename, "r") as template_file:
		data = template_file.read()
	return data


def create_page(template, data):
	responsive_filter_button_list_html = create_responsive_filter_button_list(data)
	list_html = create_vendor_list_html(data)
	new_page = template
	new_page = new_page.replace("<responsive-filter-buttons-here/>", responsive_filter_button_list_html)
	new_page = new_page.replace("<list-here/>", list_html)
	new_page = new_page.replace("<date-generated/>", datetime.datetime.now().isoformat())
	return new_page


def create_responsive_filter_button_list(data):
	foodtypes = get_sorted_unique_column_values(data, "FOODTYPE")
	button_template = "<a id='-id-' href='#' class='list-group-item filter-button'>-foodtype-</a>\n"
	button_list = ""
	for foodtype in foodtypes:
		new_button = button_template.replace("-foodtype-", foodtype)
		new_button = new_button.replace("-id-", "filter-" + create_id_from_text(foodtype))
		button_list = button_list + new_button
	return button_list


def create_id_from_text(text):
	id = text.lower()
	id = re.sub(r"[^a-zA-Z0-9]", "", id)
	return id


def create_vendor_list_html(data):
	list_template = """<li>
							<h2 id='-id-' class='vendor'>-CONTRACT-</h2>
							<p class='foodtype'>-FOODTYPE-</p>
							<p class='product'>-PRODUCT-</p>
							<p class='location'><a href='https://www.google.com/maps/dir/?api=1&destination=-y-,-x-'>Walk</a></p>
						</li>
						"""
	list_html = ""
	for row in data:
		new_item = list_template
		for field in ["CONTRACT", "FOODTYPE", "PRODUCT", "y", "x"]:
			field_value = ""
			if field in row:
				field_value = str(row[field])
			new_item = new_item.replace("-" + field + "-", field_value)
		new_item = new_item.replace("-id-", create_id_from_text(str(row["CONTRACT"])))
		list_html = list_html + new_item
	return list_html





def main():
	fair_data_filename = os.path.join(".", "data", "nc_state_fair_vendor_data.csv")
	html_template_filename = os.path.join(".", "template", "template.html")
	print("Data file: " + fair_data_filename)
	print("HTML template file: " + html_template_filename)

	fair_data = read_csv_file(fair_data_filename)
	print("Total fair data rows: " + str(len(fair_data)))
	html_template = read_template(html_template_filename)
	page_html = create_page(html_template, fair_data)

	results_filename = os.path.join(".", "site_results", "index.html")
	with open(results_filename, "w") as page_file:
		page_file.write(page_html)

	print()
	print("Count by FOODTYPE:")
	foodtypes = get_sorted_unique_column_values_and_counts(fair_data, "FOODTYPE")
	count = 0
	for key in sorted(foodtypes.keys()):
		count = count + foodtypes[key]
		print("\t" + key + ": " + str(foodtypes[key]))
	print("\t______")
	print("\tTotal: " + str(count))

if __name__ == '__main__':
	main()		



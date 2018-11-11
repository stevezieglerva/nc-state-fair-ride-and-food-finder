
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


def read_template(filename):
	data = ""
	with open(filename, "r") as template_file:
		data = template_file.read()
	return data


def create_page(template, data):
	list_html = create_vendor_list_html(data)
	new_page = template.replace("<list-here/>", list_html)
	return new_page


def create_vendor_list_html(data):
	list_template = """<li>
							<h2 class='vendor'>-CONTRACT-</h2>
							<p class='foodtype'>-FOODTYPE-</p>
							<p class='product'>-PRODUCT-</p>
						</li>
						"""
	list_html = ""
	for row in data:
		new_item = list_template
		for field in ["CONTRACT", "FOODTYPE", "PRODUCT"]:
			field_value = ""
			if field in row:
				field_value = str(row[field])
			new_item = new_item.replace("-" + field + "-", field_value)
		list_html = list_html + new_item
	return list_html


def main():
	fair_data = read_csv_file(".\\data\\nc_state_fair_vendor_data.csv")
	html_template = read_template(".\\template\\template.html")
	page_html = create_page(html_template, fair_data)

	with open("results.html", "w") as page_file:
		page_file.write(page_html)



if __name__ == '__main__':
	main()		



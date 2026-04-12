import csv

# thanks https://www.geeksforgeeks.org/python/working-csv-files-python/
# open csv and read it
with open("links.csv", mode="r") as links_file:
    csv_reader = csv.DictReader(links_file)
    links_data_list = []
    for row in csv_reader:
        links_data_list.append(row)

def get_url_for_id(link_id):
    with open("links.csv", mode="r") as links_file:
        csv_reader = csv.DictReader(links_file)
        for row in csv_reader:
            if row["link_id"] == link_id:
                return row["url"]
    return None

print(get_url_for_id("cbone"))
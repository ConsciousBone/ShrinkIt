from flask import Flask
import csv

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<p>Hello, World!</p>"

@app.route("/<link_id>")
def link_interstitial(link_id):
    # thanks https://www.geeksforgeeks.org/python/working-csv-files-python/
    # open csv and read it
    with open("links.csv", mode="r") as links_file:
        csv_reader = csv.DictReader(links_file)
        links_data_list = []
        for row in csv_reader:
            links_data_list.append(row)

    for data in links_data_list:
        print(data[1])

    return links_data_list

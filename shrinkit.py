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
        for row in csv_reader:
            if row["link_id"] == link_id:
                return row["url"]
    return None

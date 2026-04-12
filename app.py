from flask import Flask, render_template
import csv

app = Flask(__name__)

def url_for_link_id(link_id):
    # thanks https://www.geeksforgeeks.org/python/working-csv-files-python/
    # open csv and read it
    with open("links.csv", mode="r") as links_file:
        csv_reader = csv.DictReader(links_file)
        for row in csv_reader:
            if row["link_id"] == link_id:
                return row["url"]
    return ""


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/<link_id>")
def link_interstitial(link_id):
    return url_for_link_id(link_id)

if __name__ == "__main__":
    app.run()
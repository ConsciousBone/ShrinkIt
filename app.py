from flask import Flask, render_template, abort
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
    return None

@app.route("/")
def homepage():
    textaa = "some random text"
    return render_template("index.html", value = textaa)

@app.route("/<link_id>")
def link_interstitial(link_id):
    url = url_for_link_id(link_id)
    if url is None:
        abort(404)
    return render_template("redirect.html", url = url)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", error = error), 404

if __name__ == "__main__":
    app.run()
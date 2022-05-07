from flask import Flask, render_template, request, jsonify
from markupsafe import escape
from recipe_scrapers import scrape_me
import os

app = Flask(__name__)


@app.route("/")
def search():
    return render_template("search.html")


@app.route("/recipe/")
def recipe_url():
    url = escape(request.args.get("url"))
    recipe = scrape_me(url)
    response = {
        "title": recipe.title(),
        "ingredients": recipe.ingredients(),
        "instructions": recipe.instructions().split("\n"),
        "nutrients": recipe.nutrients(),
        "total_time": recipe.total_time(),
        "ratings": recipe.ratings(),
    }
    return jsonify(response)
    # return render_template("recipe.html", **response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

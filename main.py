from flask import Flask, render_template, request
#request goes to the web and requests for contents
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")

@app.route("/") #decorator of a function right below
def home():
  return render_template("home.html", name="nico")

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  indeed = extract_indeed_jobs(keyword)
  wwr = extract_wwr_jobs(keyword)
  jobs = indeed + wwr
  return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("0.0.0.0")
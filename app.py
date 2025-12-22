from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__name__)
FILE_NAME = "expenses.txt"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_expense():
    amount = request.form["amount"]
    category = request.form["category"]
    description = request.form["description"]
    date = datetime.date.today()

    with open(FILE_NAME, "a") as file:
        file.write(f"{date} | {category} | {amount} | {description}\n")

    return redirect("/view")

@app.route("/view")
def view_expenses():
    expenses = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                expenses.append(line.strip().split("|"))
    except:
        pass

    return render_template("view.html", expenses=expenses)

if __name__ == "__main__":
    app.run(debug=True)

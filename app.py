from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    note = db.Column(db.Text)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        amount = float(request.form["amount"])

        if amount <= 0:
            return redirect("/")

        expense = Expense(
            title=request.form["title"],
            amount=amount,
            category=request.form["category"],
            date=datetime.strptime(
                request.form["date"],
                "%Y-%m-%d"
            ).date(),
            note=request.form["note"]
        )

        db.session.add(expense)
        db.session.commit()

        return redirect("/")

    query = Expense.query
    search = request.args.get("search")

    if search:
        query = query.filter(
            Expense.title.contains(search)
        )

    category = request.args.get("category")

    if category:
        query = query.filter(
            Expense.category == category
        )

    from_date = request.args.get("from_date")

    if from_date:
        query = query.filter(
            Expense.date >= datetime.strptime(
                from_date,
                "%Y-%m-%d"
            ).date()
        )

    to_date = request.args.get("to_date")

    if to_date:
        query = query.filter(
            Expense.date <= datetime.strptime(
                to_date,
                "%Y-%m-%d"
            ).date()
        )

    expenses = query.order_by(
        Expense.date.desc()
    ).all()

    current_month = datetime.now().month
    current_year = datetime.now().year

    monthly_expenses = []

    for expense in expenses:
        if (
            expense.date.month == current_month
            and expense.date.year == current_year
            ):
            monthly_expenses.append(expense)
    total_spent = sum(
        expense.amount
        for expense in monthly_expenses
    )
    category_totals = {}

    for expense in monthly_expenses:

        category = expense.category

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += expense.amount

    return render_template(
        "index.html",
        expenses=expenses,
        total_spent=total_spent,
        category_totals=category_totals
    )

@app.route("/delete/<int:id>")
def delete(id):

    expense = Expense.query.get_or_404(id)

    db.session.delete(expense)
    db.session.commit()

    return redirect("/")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    expense = Expense.query.get_or_404(id)

    if request.method == "POST":

        expense.title = request.form["title"]
        amount = float(request.form["amount"])

        if amount <= 0:
            return redirect(f"/edit/{id}")

        expense.amount = amount
        expense.category = request.form["category"]

        expense.date = datetime.strptime(
            request.form["date"],
            "%Y-%m-%d"
        ).date()

        expense.note = request.form["note"]

        db.session.commit()

        return redirect("/")

    return render_template(
        "edit.html",
        expense=expense
    )

if __name__ == "__main__":
    app.run(debug=True)
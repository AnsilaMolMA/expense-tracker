# Personal Expense Tracker

A simple web application built using Flask and SQLite for tracking and managing personal expenses. The application allows users to add, view, edit, delete, and filter expenses, as well as view a monthly spending summary with category-wise breakdown.

---

## Features Implemented

### Expense Management
- Add a new expense
- View all expenses sorted by date (most recent first)
- Edit an existing expense
- Delete an expense

### Monthly Summary
- Display total spending for the current month
- Display category-wise spending breakdown for the current month

### Filtering
- Search expenses by title (partial text match)
- Filter expenses by category
- Filter expenses by date range (From Date / To Date)

### Validation
- Prevent adding expenses with non-positive amounts

---

## Technology Stack

### Backend
- Python
- Flask
- SQLAlchemy

### Frontend
- HTML
- Bootstrap 5

### Database
- SQLite

---

## Stack Choices and Tradeoffs

### Flask
Chosen because it is lightweight, easy to set up, and allows rapid development of small web applications.

### SQLite
Chosen because it requires no separate installation or configuration and is sufficient for a local single-user application.

### SQLAlchemy
Used to simplify database operations and model management instead of writing raw SQL queries.

### Bootstrap
Used to create a clean and responsive user interface quickly without spending time on custom styling.

### Tradeoffs
- SQLite is suitable for small applications but is not ideal for high-concurrency production environments.
- The application focuses on functionality and simplicity rather than advanced UI design.
- Data is stored locally and is intended for single-user usage.

---

## Project Structure

```text
expense-tracker/
│
├── app.py
├── requirements.txt
├── README.md
├── expenses.db
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── static/
```

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python app.py
```

### 3. Open in browser

```text
http://127.0.0.1:5000
```

---

## Completed Requirements

- Add expense
- View all expenses
- Edit expense
- Delete expense
- Monthly spending summary
- Category-wise spending breakdown
- Filter by title
- Filter by category
- Filter by date range
- SQLite database integration

---

## Skipped Features

The following were intentionally not implemented because they were not required by the challenge requirements:

- User authentication
- Multi-user support
- Deployment to a cloud platform
- Automated test suite
- Expense charts and analytics
- Export to CSV/Excel

---

## Known Rough Edges

- Validation is limited to basic checks (for example, positive amount validation).
- The application is designed for a single user.
- No pagination is implemented for large numbers of expenses.
- SQLite is used for simplicity and local execution rather than production-scale workloads.
- Delete operations rely on browser confirmation and do not support undo functionality.

---

## Future Improvements

- User authentication and authorization
- Expense charts and visual analytics
- Budget tracking and alerts
- Export expenses to CSV or Excel
- Recurring expense support
- REST API endpoints
- Multi-user support

---

## Author

Developed as part of a Software Engineer Practical Test using Flask, SQLite, HTML, and Bootstrap.
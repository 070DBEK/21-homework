# 21 Homework

This is a Django-based project designed for managing tasks (todos) with features such as searching, filtering, and sorting. It includes functionality for adding, updating, and deleting tasks, as well as categorizing them by priority and status.

## Features

- **Task Management:** Create, update, delete, and view tasks.
- **Filtering & Sorting:** Filter tasks by priority, status, and search by title. Sort tasks by due date, priority, or status.
- **Priorities:** Tasks can be set to "Low," "Medium," or "High" priority.
- **Status:** Tasks can be marked as "Active" or "Completed."
- **Due Date:** Assign and view due dates for tasks.

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.12 or higher
- Django 5.1.5
- Database (SQLite is used by default)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/070DBEK/21-homework.git
Navigate to the project directory:

bash
Копировать
Редактировать
cd 21-homework
Set up a virtual environment:

bash
Копировать
Редактировать
python -m venv venv
Activate the virtual environment:

Windows:
bash
Копировать
Редактировать
.\venv\Scripts\activate
Mac/Linux:
bash
Копировать
Редактировать
source venv/bin/activate
Install the dependencies:

bash
Копировать
Редактировать
pip install -r requirements.txt
Run migrations to set up the database:

bash
Копировать
Редактировать
python manage.py migrate
Create a superuser to access the admin interface (optional):

bash
Копировать
Редактировать
python manage.py createsuperuser
Start the development server:

bash
Копировать
Редактировать
python manage.py runserver
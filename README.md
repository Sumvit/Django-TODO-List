# Django-TODO-List

A simple Django web application for managing user-specific TODO tasks.  
Currently supports creating new tasks and viewing your task list.

---

## Features

- User-specific task lists (tasks are unique to each user)
- Add new tasks
- View all your tasks
- Clean and minimal interface

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/django-todo-app.git
cd django-todo-app
```
2. **Create and activate a virtual environment:**

```bash
python3 -m venv env
source env/bin/activate    # On Windows: `env\Scripts\activate`
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```
4. **Apply database migrations:**
```bash
python manage.py migrate
```
5. **Run the server:**
```bash
python manage.py runserver
```
6. **Open your browser at:**  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


**License**
This project is licensed under the MIT License.
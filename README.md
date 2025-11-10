### INF601 - Advanced Programming in Python
### David Sowles
### Mini Project 4

# Animal Blog

A Django-powered web application that allows users to create, view, and manage blog posts about animals.  
The app includes user authentication (login/register), Bootstrap styling, and a clean responsive layout.

---

## Description

The **Animal Blog** is a simple but full-featured web app built using the Django framework.  


---

## Getting Started

### Dependencies

- Python 3.12 or higher  
- Django 5.2  
- Bootstrap 5.3 (via CDN)  
- Works on Windows 10/11, macOS, or Linux

Install dependencies using:

```bash
pip install -r requirements.txt
```
(Do this after the steps in the Intalling section)

### Installing
- Create a project directory somewhere.
    - Make sure your terminal is located at this directory.
- Clone the repository:
```bash
git clone https://github.com/dsowles/miniProject4DavidSowles.git
cd animal_blog_project
```
- Create and activate a virtual environment.
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```
- Install Project Dependencies
```bash
pip install -r requirements.txt
```

- Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

- Create a superuser account (optional)
```bash
python manage.py createsuperuser
```

- Run the server
```bash
python manage.py runserver
```

### Executing the Program
- After installing, goto http://127.0.0.1:8000/
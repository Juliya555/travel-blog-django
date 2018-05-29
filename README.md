# Hello Travel Project
This is a travel blog about the world's best places to visit.
It is built on the **Django** Framework with SQLite to run in **Python 3**. Tested for Ubuntu Linux 16.04 LTS.

# Setup
1. Create virtual enviroment and activate it:
  ```
  python -m venv env_name
  source env_name/bin/activate
  ```
2. Clone the repository:
  ```
  git clone https://github.com/Juliya555/travel-blog-django.git
  ```
3. Install all requirements:
  ```
  pip install -r requirements.txt
  ```
4. Make database migrations:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
5. Create a user for admin pannel:
  ```
  python manage.py createsuperuser
  ```
6. Create a gmail account for communicating with your visitors.

# Run
1. Set environment variables and run the server:
  ```
  TRAVEL_HOST_USER=your.email@gmail.com TRAVEL_HOST_PASSWORD=your_password python manage.py runserver
  ```
2. Open http://127.0.0.1:8000 in your web browser to see the blog.
3. Open http://127.0.0.1:8000/admin in your web browser to see the admin pannel.

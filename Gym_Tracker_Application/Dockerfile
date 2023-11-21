FROM python

WORKDIR ./GymTracker

RUN pip install django
RUN pip install django-reset-migrations
RUN pip install django-widget-tweaks
RUN pip install Jinja2
RUN pip install psycopg2-binary
RUN pip install requests
RUN pip install Werkzeug==2.3.0
RUN pip install requests-oauthlib
RUN pip install django-crispy-forms
RUN pip install PyJWT
RUN pip install JWT
RUN apt update
RUN apt install nano

COPY . .

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
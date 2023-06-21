FROM python:3.11.3-slim-buster

# create directory for the app user
RUN mkdir -p /home/upwork-33841525

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/upwork-33841525
ENV APP_HOME=/home/upwork-33841525/app
RUN mkdir $APP_HOME

# install dependencies
RUN apt-get update
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --upgrade -r requirements.txt --ignore-installed

# copy project
COPY . $APP_HOME

WORKDIR $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

CMD ["gunicorn", "--conf", "config/gunicorn_conf.py", "--bind", "0.0.0.0:3000", "app:create_app(env='prod')"]
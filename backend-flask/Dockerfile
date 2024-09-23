FROM python:3.10-slim-buster

# Inside Container
# make a new folder inside container
WORKDIR /backend-flask

# Outside Container -> Inside Container
# this contains the required libraries to install to run the app
COPY requirements.txt requirements.txt

# Inside Container
# install the python libraries used for the app
RUN pip3 install -r requirements.txt

# Outside Container -> Inside Container
# . means eveything in the current directory
# first period : /backend-flask (outside containr)
# Second period : /backend-flask (inside the containr)
COPY . .

# Set Environment variables (Env Vars)
# Inside Cntaine and will remain set when the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD : Command
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

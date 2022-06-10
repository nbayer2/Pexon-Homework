# start by pulling the python image
FROM python:3.9-alpine
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
# switch working directory
WORKDIR /app

# set enviournment variables 
ENV FLASK_APP app.py
ENV FLASK_ENV development

# copy every content from the local file to the image
COPY . /app
# install the dependencies and packages in the requirements file
RUN pip3 install -r requirements.txt
# configure the container to run in an executed manner
CMD ["python", "app.py"]
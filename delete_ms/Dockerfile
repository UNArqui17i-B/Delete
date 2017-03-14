FROM python:2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Bundle app source
ADD . /code
WORKDIR /code

EXPOSE  4030
CMD ["python", "delete_app.py"]

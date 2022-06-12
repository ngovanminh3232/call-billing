FROM python:3.10.5

WORKDIR /app
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install -r ./requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
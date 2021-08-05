FROM python:3.8


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt


RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

COPY . /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]




FROM python:3.9

WORKDIR /code

RUN pip install "fastapi[standard]" pydantic

COPY ./app /code/app
COPY ./stockinfo.csv /code/stockinfo.csv

# Use port 8080
EXPOSE 8080

CMD ["fastapi", "run", "app/main.py", "--port", "8080", "--host", "0.0.0.0"]
FROM python:3

WORKDIR /code

COPY pyproject.toml .

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev --no-root

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
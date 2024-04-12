FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml ./

RUN pip install --upgrade pip "poetry==1.8.2"
RUN poetry config virtualenvs.create false --local
RUN poetry install

COPY mysite .

CMD ["gunicorn", "mysite.wsgi", "runserver"]

FROM python:3.9-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
ENV POKE_URL https://pokeapi.co/api/v2

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "main:app"]

FROM python:3.9-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "main:app"]
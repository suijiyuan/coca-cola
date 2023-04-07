FROM python:3.11.3-alpine

WORKDIR /coca-cola

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]
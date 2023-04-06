FROM python:alpine

WORKDIR /coca-cola

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
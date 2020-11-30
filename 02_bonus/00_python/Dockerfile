FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY financial.py /app

CMD ["./financial.py", "MSFT", "Total Revenue"]

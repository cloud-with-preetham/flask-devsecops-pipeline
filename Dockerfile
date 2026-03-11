FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade \
    "pip==25.0.1" \
    "wheel==0.46.2" \
 && pip install --no-cache-dir -r requirements.txt \
 && python -m pip uninstall --yes setuptools wheel

COPY . .

EXPOSE 80

CMD ["python", "app.py"]

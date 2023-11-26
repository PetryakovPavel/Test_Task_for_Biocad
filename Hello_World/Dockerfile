FROM python:3.9-slim
WORKDIR /app
RUN pip install gunicorn
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:32777", "web_project.wsgi"]

FROM python:3.8

RUN pip install flask flask-cors tweepy requests

COPY src/ app/
WORKDIR /app

ENV port=8080

ENTRYPOINT ["python"]
CMD ["app.py"]

# cloud run: https://flask-app-u63drvxcia-uc.a.run.app/

# gcloud builds submit --tag gcr.io/summative-290816/flask-app

# gcloud run deploy --image gcr.io/summative-290816/flask-app
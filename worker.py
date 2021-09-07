from celery import Celery

BROKER_URL = "redis://redis"  
BACKEND_URL = "redis://redis"  

app = Celery("worker", broker=BROKER_URL, backend=BACKEND_URL, include=["app.tasks"])

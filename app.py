from celery import Celery
import billiard, logging

app = Celery('app')
app.conf.broker_url = 'redis://:password@localhost:6380/0'


logger = billiard.log_to_stderr()
logger.setLevel(logging.DEBUG)

@app.task
def hello():
    return 'hello world'


app.send_task('app.hello')

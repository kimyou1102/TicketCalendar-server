from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import getTicketDatas

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    @scheduler.scheduled_job('cron', hour='12', minute='30', id='getTicketDatas')
    # @scheduler.scheduled_job('interval', seconds=  5, id='test')
    def auto_check():
        getTicketDatas()
        
    scheduler.start()
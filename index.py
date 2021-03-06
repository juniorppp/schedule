#https://apscheduler.readthedocs.io/en/3.x/userguide.html - Referencia
#https://superfastpython.com/threadpoolexecutor-in-python/

from lib.paginas import Paginas
from apscheduler.events import EVENT_JOB_ERROR
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
import pytz,time,random

def _process():
    dados = {'cpf' : '32504488858'}
    lista = ['https://google.com', 'https://terra.com.br', 'https://uol.com.br']

    pg = Paginas(dados)
    pg._sites(random.choice(lista))

executors = {
    'default': ThreadPoolExecutor(20),      
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    #DEFINE A QUANTIDADE DE INSTANCIAS QUE PODE TRABALHAR
    'max_instances': 1
}
    
scheduler = BackgroundScheduler(
    executors=executors, job_defaults=job_defaults,
    timezone=pytz.timezone('America/Sao_Paulo')
)

scheduler.add_job(_process, trigger='cron', second='5')
#scheduler.add_job(_process, trigger='cron', second='*/5')
#scheduler.add_job(_process, 'interval', minutes=1)

if __name__ == '__main__':  
    print('Start')
    scheduler.start()
    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        #Isso faz com que não espere a conclusão da execução
        #scheduler.shutdown(wait=False)
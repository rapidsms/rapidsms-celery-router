from celery import task

from rapidsms.router.blocking import BlockingRouter


@task()
def rapidsms_incoming_message(msg):
    """Simple Celery task to process message via BlockingRouter."""

    logger = rapidsms_incoming_message.get_logger()
    logger.debug('New incoming message: %s' % msg)
    router = BlockingRouter()
    try:
        router.start()
        router.incoming(msg)
        router.stop()
    except Exception, e:
        logger.exception(e)
    logger.debug('Complete')

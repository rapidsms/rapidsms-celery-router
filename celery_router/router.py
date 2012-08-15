from rapidsms.router.blocking import BlockingRouter

from celery_router.tasks import rapidsms_incoming_message


class CeleryRouter(BlockingRouter):
    """Skeleton router only used to execute Celery task."""

    def incoming(self, msg):
        eager = False
        backend_name = msg.connection.backend.name
        try:
            backend = self.backends[backend_name]
        except KeyError:
            backend = None
        if backend:
            eager = backend._config.get('celery_router.eager', False)
        if eager:
            self.debug('Executing in current process')
            rapidsms_incoming_message(msg)
        else:
            self.debug('Executing asynchronously')
            rapidsms_incoming_message.delay(msg)

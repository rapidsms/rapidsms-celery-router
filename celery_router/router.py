from rapidsms.router.blocking import BlockingRouter

from celery_router.tasks import rapidsms_handle_message


class CeleryRouter(BlockingRouter):
    """Skeleton router only used to execute the Celery task."""

    def _queue_message(self, msg, incoming):
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
            rapidsms_handle_message(msg, incoming)
        else:
            self.debug('Executing asynchronously')
            rapidsms_handle_message.delay(msg, incoming)

    def incoming(self, msg):
        self._queue_message(msg, incoming=True)

    def outgoing(self, msg):
        self._queue_message(msg, incoming=False)

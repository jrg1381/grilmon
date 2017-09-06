import os


class ScheduledShutdown:
    def __init__(self):
        self.marker = "marker"
        self.shutdown_scheduled = False

    @property
    def shutdown_scheduled(self):
        return self.shutdown_scheduled

    @shutdown_scheduled.getter
    def shutdown_scheduled(self):
        return os.path.exists(self.marker)

    @shutdown_scheduled.setter
    def shutdown_scheduled(self, is_scheduled):
        if is_scheduled:
            with open(self.marker, 'w'):
                pass
        else:
            try:
                os.remove(self.marker)
            except OSError:
                pass

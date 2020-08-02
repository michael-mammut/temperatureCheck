from datetime import datetime


class MeasureResult:

    def __init__(self, value, ambient):
        self.value = value
        self.ambient = ambient
        self.created_at = self.get_now()

    @staticmethod
    def get_now():
        return datetime.now()

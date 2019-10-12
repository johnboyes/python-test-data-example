from datetime import datetime


class InputRequest:
    def __init__(self):
        today = datetime.now()
        self.start_time = "{:%Y-%m-%d %H:%M}".format(today)
        self.end_time = "{:%Y-%m-%d}".format(today)

    def __str__(self):
        return f"Start time: {self.start_time} End time: {self.end_time}"


input_request = InputRequest()

print(input_request)

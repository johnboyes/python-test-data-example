from datetime import datetime


class InputRequest:
    def start_time(self):
        return "{:%Y-%m-%d %H:%M}".format(datetime(2001, 2, 3, 4, 5))

    def end_time(self):
        return "{:%Y-%m-%d}".format(datetime(2001, 2, 3, 4, 5))

    def __str__(self):
        return f"Start time: {self.start_time()} End time: {self.end_time()}"


input_request = InputRequest()

print(input_request)

from request_date_utils import request_date


class InputRequest:
    def __init__(self):
        self.start_time = request_date()
        self.end_time = request_date(format="{:%Y-%m-%d}", days=1)

    def __str__(self):
        return f"Start time: {self.start_time} End time: {self.end_time}"


input_request = InputRequest()

print(input_request)

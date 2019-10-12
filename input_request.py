from request_date_utils import request_date


class InputRequest:
    def __init__(self):
        self.start_time = request_date("{:%Y-%m-%d %H:%M}")
        self.end_time = request_date("{:%Y-%m-%d}", 1)

    def __str__(self):
        return f"Start time: {self.start_time} End time: {self.end_time}"


input_request = InputRequest()

print(input_request)

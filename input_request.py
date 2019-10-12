from datetime import datetime


class InputRequest:
    def __str__(self):
        return "Start time: {start_time} End time: {:%Y-%m-%d}".format(
            datetime(2001, 2, 3, 4, 5), start_time=datetime(2001, 2, 3, 4, 5)
        )


input_request = InputRequest()

print(input_request)

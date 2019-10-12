from datetime import datetime


class InputRequest:
    def __str__(self):
        return "This is an example input request. Start time: {:%Y-%m-%d %H:%M}".format(
            datetime(2001, 2, 3, 4, 5)
        )


input_request = InputRequest()

print(input_request)

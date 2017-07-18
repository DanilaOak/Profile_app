from datetime import datetime


class BenchmarkMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_start = datetime.now()
        response = self.get_response(request)
        response_time = datetime.now() - time_start
        with open('requests.log', 'a') as file:
            file.write("Request - {} Execution time - {}\n".format(response, response_time))
        return response

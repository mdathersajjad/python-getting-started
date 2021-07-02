class AddXFS(object):

    """Add an updated X-Forwarded-Server header to the upstream request."""

    def process_request(self, proxy, request, **kwargs):
        kwargs['headers']['X-Forwarded-Server'] = "tranquil-atoll-99599.herokuapp.com";

        return kwargs

    def process_response(self, proxy, request, upstream_response, response):
        print(response);
        return response;
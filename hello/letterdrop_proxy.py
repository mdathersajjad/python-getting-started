class AddXFS(object):

    """Add an updated X-Forwarded-Server header to the upstream request."""

    def process_request(self, proxy, request, **kwargs):
        kwargs['headers']['X-Forwarded-Server'] = "tranquil-atoll-99599.herokuapp.com";

        return kwargs

    def process_response(self, proxy, request, upstream_response, response):
        #print(response.content);
        print("Upstream response");
        print(upstream_response.content);
        #print(response.status_code);
        #print(upstream_response.status_code)
        return response;
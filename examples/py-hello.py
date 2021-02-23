#!/usr/bin/env python3
import os

Schema = (
    { "message": { "type": "string" } },
)

version = '0.1.0'
priority = 0

# This is an example plugin that add a header to the response

class Plugin(object):
    def __init__(self, config):
        self.config = config

    def access(self, kong):
        host, err = kong.request.get_header("host")
        if err:
            kong.log.err(err)
        message = "hello"
        if 'message' in self.config:
            message = self.config['message']
        kong.response.set_header("x-hello-from-python", "Python says %s to %s" % (message, host))
        kong.response.set_header("x-python-pid", str(os.getpid()))


# add below section to allow this plugin optionally be running in a dedicated process
if __name__ == "__main__":
    from kong_pdk.cli import start_dedicated_server
    start_dedicated_server("py-hello", Plugin, version, priority)
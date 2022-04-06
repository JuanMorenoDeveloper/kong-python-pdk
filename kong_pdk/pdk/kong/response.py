# AUTO GENERATED BASED ON Kong 2.7.x, DO NOT EDIT
# Original source path: kong/pdk/response.lua

from typing import TypeVar, Any, Union, List, Mapping, Tuple, Optional

number = TypeVar('number', int, float)
table = TypeVar('table', List[Any], Mapping[str, Any])
# XXX
cdata = Any
err = str


class response():


    @staticmethod
    def add_header(name: str, value: Any) -> None:
        """

            Adds a response header with the given value. Unlike
            `kong.response.set_header()`, this function does not remove any existing
            header with the same name. Instead, another header with the same name is
            added to the response. If no header with this name already exists on
            the response, then it is added with the given value, similarly to
            `kong.response.set_header().`

        Phases:
            rewrite, access, header_filter, response, admin_api

        Example:
            kong.response.add_header("Cache-Control", "no-cache")

            kong.response.add_header("Cache-Control", "no-store")

        :parameter name: The header name.
        :type name: str
        :parameter value: The header value.
        :type value: Any

        :return: throws an error on invalid input.

        :rtype: None
        """
        pass

    @staticmethod
    def clear_header(name: str) -> None:
        """

            Removes all occurrences of the specified header in the response sent to
            the client.

        Phases:
            rewrite, access, header_filter, response, admin_api

        Example:
            kong.response.set_header("X-Foo", "foo")

            kong.response.add_header("X-Foo", "bar")

            kong.response.clear_header("X-Foo")

            # from here onwards, no X-Foo headers will exist in the response

        :parameter name: The name of the header to be cleared
        :type name: str

        :return: throws an error on invalid input.

        :rtype: None
        """
        pass

    @staticmethod
    def error(status: number, message: Optional[str], headers: Optional[table]) -> None:
        """

            This function interrupts the current processing and produces an error
            response.
            It is recommended to use this function in conjunction with the `return`
            operator, to better reflect its meaning:
            ```lua
            return kong.response.error(500, "Error", {["Content-Type"] = "text/html"})
            ```
            1. The `status` argument sets the status code of the response that
            is seen by the client. The status code must an error code, that is,
            greater than 399.
            2. The optional `message` argument sets the message describing
            the error, which is written in the body.
            3. The optional `headers` argument can be a table specifying response
            headers to send. If specified, its behavior is similar to
            `kong.response.set_headers()`.
              This method sends the response formatted in JSON, XML, HTML or plaintext.
              The actual format is determined using one of the following options, in
              this order:
              - Manually specified in the `headers` argument using the `Content-Type`
              header.
              - Conforming to the `Accept` header from the request.
              - If there is no setting in the `Content-Type` or `Accept` header, the
              response defaults to JSON format. Also see the `Content-Length`
              header in the produced response for convenience.

        Phases:
            rewrite, access, admin_api, header_filter, (only, if, body`, is, nil)

        Example:
            return kong.response.error(403, "Access Forbidden", {

            ["Content-Type"] = "text/plain",

            ["WWW-Authenticate"] = "Basic"

            })

            # -

            return kong.response.error(403, "Access Forbidden")

            # -

            return kong.response.error(403)

        :parameter status: The status to be used (>399).
        :type status: number
        :parameter message: The error message to be used.
        :type message: str
        :parameter headers: The headers to be used.
        :type headers: table

        :return: throws an error on invalid input.

        :rtype: None
        """
        pass

    @staticmethod
    def exit(status: number, body: Optional[Any], headers: Optional[table]) -> None:
        """

            This function interrupts the current processing and produces a response.
            It is typical to see plugins using it to produce a response before Kong
            has a chance to proxy the request (e.g. an authentication plugin rejecting
            a request, or a caching plugin serving a cached response).
            It is recommended to use this function in conjunction with the `return`
            operator, to better reflect its meaning:
            ```lua
            return kong.response.exit(200, "Success")
            ```
            Calling `kong.response.exit()` interrupts the execution flow of
            plugins in the current phase. Subsequent phases will still be invoked.
            For example, if a plugin calls `kong.response.exit()` in the `access`
            phase, no other plugin is executed in that phase, but the
            `header_filter`, `body_filter`, and `log` phases are still executed,
            along with their plugins. Plugins should be programmed defensively
            against cases when a request is **not** proxied to the Service, but
            instead is produced by Kong itself.
            1. The first argument `status` sets the status code of the response that
            is seen by the client.
               In L4 proxy mode, the `status` code provided is primarily for logging
               and statistical purposes, and is not visible to the client directly.
               In this mode, only the following status codes are supported:
               * 200 - OK
               * 400 - Bad request
               * 403 - Forbidden
               * 500 - Internal server error
               * 502 - Bad gateway
               * 503 - Service unavailable
            2. The second, optional, `body` argument sets the response body. If it is
               a string, no special processing is done, and the body is sent
               as-is.  It is the caller's responsibility to set the appropriate
               `Content-Type` header via the third argument.
               As a convenience, `body` can be specified as a table. In that case,
               the `body` is JSON-encoded and has the `application/json` Content-Type
               header set.
               On gRPC, we cannot send the `body` with this function, so
               it sends `"body"` in the `grpc-message` header instead.
               * If the body is a table, it looks for the `message` field in the body,
               and uses that as a `grpc-message` header.
               * If you specify `application/grpc` in the `Content-Type` header, the
               body is sent without needing the `grpc-message` header.
               In L4 proxy mode, `body` can only be `nil` or a string. Automatic JSON
               encoding is not available. When `body` is provided, depending on the
               value of `status`, the following happens:
               * When `status` is 500, 502 or 503, then `body` is logged in the Kong
               error log file.
               * When the `status` is anything else, `body` is sent back to the L4 client.
            3. The third, optional, `headers` argument can be a table specifying
               response headers to send. If specified, its behavior is similar to
               `kong.response.set_headers()`. This argument is ignored in L4 proxy mode.
            Unless manually specified, this method automatically sets the
            `Content-Length` header in the produced response for convenience.

        Phases:
            preread, rewrite, access, admin_api, header_filter, (only, if, body`, is, nil)

        Example:
            return kong.response.exit(403, "Access Forbidden", {

            ["Content-Type"] = "text/plain",

            ["WWW-Authenticate"] = "Basic"

            })

            # -

            return kong.response.exit(403, [[{"message":"Access Forbidden"}]], {

            ["Content-Type"] = "application/json",

            ["WWW-Authenticate"] = "Basic"

            })

            # -

            return kong.response.exit(403, { message = "Access Forbidden" }, {

            ["WWW-Authenticate"] = "Basic"

            })

            # -

            # In L4 proxy mode

            return kong.response.exit(200, "Success")

        :parameter status: The status to be used.
        :type status: number
        :parameter body: The body to be used.
        :type body: Any
        :parameter headers: The headers to be used.
        :type headers: table

        :return: throws an error on invalid input.

        :rtype: None
        """
        pass

    @staticmethod
    def get_header(name: str) -> str:
        """

            Returns the value of the specified response header, as would be seen by
            the client once received.
            The list of headers returned by this function can consist of both response
            headers from the proxied Service _and_ headers added by Kong (e.g. via
            `kong.response.add_header()`).
            The return value is either a `string`, or can be `nil` if a header with
            `name` is not found in the response. If a header with the same name is
            present multiple times in the request, this function returns the value
            of the first occurrence of this header.

        Phases:
            header_filter, response, body_filter, log, admin_api

        Example:
            # Given a response with the following headers:

            # X-Custom-Header: bla

            # X-Another: foo bar

            # X-Another: baz

            kong.response.get_header("x-custom-header") # "bla"

            kong.response.get_header("X-Another")       # "foo bar"

            kong.response.get_header("X-None")          # nil

        :parameter name: The name of the header.
            Header names are case-insensitive and dashes (`-`) can be written as
            underscores (`_`). For example, the header `X-Custom-Header` can also be
            retrieved as `x_custom_header`.
        :type name: str

        :return: The value of the header.

        :rtype: str
        """
        pass

    @staticmethod
    def get_headers(max_headers: Optional[number]) -> Tuple[table, str]:
        """

            Returns a Lua table holding the response headers. Keys are header names.
            Values are either a string with the header value, or an array of strings
            if a header was sent multiple times. Header names in this table are
            case-insensitive and are normalized to lowercase, and dashes (`-`) can be
            written as underscores (`_`). For example, the header `X-Custom-Header` can
            also be retrieved as `x_custom_header`.
            A response initially has no headers. Headers are added when a plugin
            short-circuits the proxying by producing a header
            (e.g. an authentication plugin rejecting a request), or if the request has
            been proxied, and one of the latter execution phases is currently running.
            Unlike `kong.service.response.get_headers()`, this function returns *all*
            headers as the client would see them upon reception, including headers
            added by Kong itself.
            By default, this function returns up to **100** headers. The optional
            `max_headers` argument can be specified to customize this limit, but must
            be greater than **1** and equal to or less than **1000**.

        Phases:
            header_filter, response, body_filter, log, admin_api

        Example:
            # Given an response from the Service with the following headers:

            # X-Custom-Header: bla

            # X-Another: foo bar

            # X-Another: baz

            headers = kong.response.get_headers()

            headers.x_custom_header # "bla"

            headers.x_another[1]    # "foo bar"

            headers["X-Another"][2] # "baz"

        :parameter max_headers: Limits the number of headers parsed.
        :type max_headers: number

        :return: headers A table representation of the headers in the
            response.

        :rtype: table
        :return: err If more headers than `max_headers` were present,
            returns a string with the error `"truncated"`.

        :rtype: str
        """
        pass
    
    # this function's return type is modified mannually as body can be arbitrary binary string
    @staticmethod
    def get_raw_body() -> bytes:
        """

            Returns the full body when the last chunk has been read.
            Calling this function starts buffering the body in
            an internal request context variable, and sets the current
            chunk (`ngx.arg[1]`) to `nil` when the chunk is not the
            last one. When it reads the last chunk, the function returns the full
            buffered body.

        Phases:
            body_filter`

        Example:
            body = kong.response.get_raw_body()

            if body:

                body = transform(body)

            kong.response.set_raw_body(body)

        :return: body The full body when the last chunk has been read,
            otherwise returns `nil`.

        :rtype: str
        """
        pass

    @staticmethod
    def get_source() -> str:
        """

            This function helps determine where the current response originated
            from. Since Kong is a reverse proxy, it can short-circuit a request and
            produce a response of its own, or the response can come from the proxied
            Service.
            Returns a string with three possible values:
            * `"exit"` is returned when, at some point during the processing of the
              request, there has been a call to `kong.response.exit()`. This happens
              when the request was short-circuited by a plugin or by Kong
              itself (e.g. invalid credentials).
            * `"error"` is returned when an error has happened while processing the
              request. For example, a timeout while connecting to the upstream
              service.
            * `"service"` is returned when the response was originated by successfully
              contacting the proxied Service.

        Phases:
            header_filter, response, body_filter, log, admin_api

        Example:
            if kong.response.get_source() == "service":

                kong.log("The response comes from the Service")

            elseif kong.response.get_source() == "error":

                kong.log("There was an error while processing the request")

            elseif kong.response.get_source() == "exit":

                kong.log("There was an early exit while processing the request")

        :return: The source.

        :rtype: str
        """
        pass

    @staticmethod
    def get_status() -> number:
        """

            Returns the HTTP status code currently set for the downstream response (as
            a Lua number).
            If the request was proxied (as per `kong.response.get_source()`), the
            return value is the response from the Service (identical to
            `kong.service.response.get_status()`).
            If the request was _not_ proxied and the response was produced by Kong
            itself (i.e. via `kong.response.exit()`), the return value is
            returned as-is.

        Phases:
            header_filter, response, body_filter, log, admin_api

        Example:
            kong.response.get_status() # 200

        :return: status The HTTP status code currently set for the
            downstream response.

        :rtype: number
        """
        pass

    @staticmethod
    def set_header(name: str, value: Any) -> None:
        """

            Sets a response header with the given value. This function overrides any
            existing header with the same name.
            Note: Underscores in header names are automatically transformed into dashes
            by default. If you want to deactivate this behavior, set the
            `lua_transform_underscores_in_response_headers` Nginx config option to `off`.
            This setting can be set in the Kong Config file:
                nginx_http_lua_transform_underscores_in_response_headers = off
            Be aware that changing this setting might break any plugins that
            rely on the automatic underscore conversion.

        Phases:
            rewrite, access, header_filter, response, admin_api

        Example:
            kong.response.set_header("X-Foo", "value")

        :parameter name: The name of the header
        :type name: str
        :parameter value: The new value for the header.
        :type value: Any

        :return: throws an error on invalid input.

        :rtype: None
        """
        pass

    @staticmethod
    def set_headers(headers: table) -> None:
        """

            Sets the headers for the response. Unlike `kong.response.set_header()`,
            the `headers` argument must be a table in which each key is a string
            corresponding to a header's name, and each value is a string, or an
            array of strings.
            The resulting headers are produced in lexicographical order. The order of
            entries with the same name (when values are given as an array) is
            retained.
            This function overrides any existing header bearing the same name as those
            specified in the `headers` argument. Other headers remain unchanged.

        Phases:
            rewrite, access, header_filter, response, admin_api

        Example:
            kong.response.set_headers({

            ["Bla"] = "boo",

            ["X-Foo"] = "foo3",

            ["Cache-Control"] = { "no-store", "no-cache" }

            })

            # Will add the following headers to the response, in this order:

            # X-Bar: bar1

            # Bla: boo

            # Cache-Control: no-store

            # Cache-Control: no-cache

            # X-Foo: foo3

        :parameter headers: 
        :type headers: table

        :return: throws an error on invalid input.

        :rtype: None
        """
        pass

    @staticmethod
    def set_raw_body(body: str) -> None:
        """

            Sets the body of the response.
            The `body` argument must be a string and is not processed in any way.
            This function can't change the `Content-Length` header if one was
            added. If you decide to use this function, the `Content-Length` header
            should also be cleared, for example in the `header_filter` phase.

        Phases:
            body_filter`

        Example:
            kong.response.set_raw_body("Hello, world!")

            # or

            body = kong.response.get_raw_body()

            if body:

                body = transform(body)

            kong.response.set_raw_body(body)

        :parameter body: The raw body.
        :type body: str

        :return: throws an error on invalid inputs.

        :rtype: None
        """
        pass

    @staticmethod
    def set_status(status: number) -> None:
        """

            Allows changing the downstream response HTTP status code before sending it
            to the client.

        Phases:
            rewrite, access, header_filter, response, admin_api

        Example:
            kong.response.set_status(404)

        :parameter status: The new status.
        :type status: number

        :return: throws an error on invalid input.

        :rtype: None
        """
        pass

    pass
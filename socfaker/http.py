from .baseclass import BaseClass


class HTTP(BaseClass):

    """This class contains information related to HTTP data

    Returns:
        HTTP: Returns an object contianing properties related to HTTP data
    """
    
    _code_map = [
        {'code': '100', 'reason': 'Continue'}, 
        {'code': '101', 'reason': 'Switching Protocols'}, 
        {'code': '102', 'reason': 'Processing'},
        {'code': '200', 'reason': 'OK'}, 
        {'code': '201', 'reason': 'Created'}, 
        {'code': '202', 'reason': 'Accepted'},
        {'code': '203', 'reason': 'Non-authoritative Information'}, 
        {'code': '204', 'reason': 'No Content'}, 
        {'code': '205', 'reason': 'Reset Content'}, 
        {'code': '206', 'reason': 'Partial Content'}, 
        {'code': '207', 'reason': 'Multi-Status'}, 
        {'code': '208', 'reason': 'Already Reported'}, 
        {'code': '226', 'reason': 'IM Used'}, 
        {'code': '300', 'reason': 'Multiple Choices'}, 
        {'code': '301', 'reason': 'Moved Permanently'}, 
        {'code': '302', 'reason': 'Found'}, 
        {'code': '303', 'reason': 'See Other'}, 
        {'code': '304', 'reason': 'Not Modified'}, 
        {'code': '305', 'reason': 'Use Proxy'}, 
        {'code': '307', 'reason': 'Temporary Redirect'},
        {'code': '308', 'reason': 'Permanent Redirect'}, 
        {'code': '400', 'reason': 'Bad Request'}, 
        {'code': '401', 'reason': 'Unauthorized'}, 
        {'code': '402', 'reason': 'Payment Required'}, 
        {'code': '403', 'reason': 'Forbidden'}, 
        {'code': '404', 'reason': 'Not Found'}, 
        {'code': '405', 'reason': 'Method Not Allowed'}, 
        {'code': '406', 'reason': 'Not Acceptable'},
        {'code': '407', 'reason': 'Proxy Authentication Required'}, 
        {'code': '408', 'reason': 'Request Timeout'}, 
        {'code': '409', 'reason': 'Conflict'}, 
        {'code': '410', 'reason': 'Gone'}, 
        {'code': '411', 'reason': 'Length Required'}, 
        {'code': '412', 'reason': 'Precondition Failed'}, 
        {'code': '413', 'reason': 'Payload Too Large'}, 
        {'code': '414', 'reason': 'Request-URI Too Long'}, 
        {'code': '415', 'reason': 'Unsupported Media Type'}, 
        {'code': '416', 'reason': 'Requested Range Not Satisfiable'}, 
        {'code': '417', 'reason': 'Expectation Failed'}, 
        {'code': '418', 'reason': 'Im a teapot'}, 
        {'code': '421', 'reason': 'Misdirected Request'}, 
        {'code': '422', 'reason': 'Unprocessable Entity'}, 
        {'code': '423', 'reason': 'Locked'}, 
        {'code': '424', 'reason': 'Failed Dependency'}, 
        {'code': '426', 'reason': 'Upgrade Required'}, 
        {'code': '428', 'reason': 'Precondition Required'}, 
        {'code': '429', 'reason': 'Too Many Requests'}, 
        {'code': '431', 'reason': 'Request Header Fields Too Large'}, 
        {'code': '444', 'reason': 'Connection Closed Without Response'}, 
        {'code': '451', 'reason': 'Unavailable For Legal Reasons'}, 
        {'code': '499', 'reason': 'Client Closed Request'}, 
        {'code': '500', 'reason': 'Internal Server Error'}, 
        {'code': '501', 'reason': 'Not Implemented'}, 
        {'code': '502', 'reason': 'Bad Gateway'}, 
        {'code': '503', 'reason': 'Service Unavailable'}, 
        {'code': '504', 'reason': 'Gateway Timeout'}, 
        {'code': '505', 'reason': 'HTTP Version Not Supported'}, 
        {'code': '506', 'reason': 'Variant Also Negotiates'}, 
        {'code': '507', 'reason': 'Insufficient Storage'}, 
        {'code': '508', 'reason': 'Loop Detected'}, 
        {'code': '510', 'reason': 'Not Extended'}, 
        {'code': '511', 'reason': 'Network Authentication Required'}, 
        {'code': '599', 'reason': 'Network Connect Timeout Error'}
    ]

    @property
    def request(self):
        """A randomly generated request dictionary based on Elastic ECS format

        Returns:
            dict: A random request dictionary containing body, bytes, method and referrer information 
        """
        return {
            'body': {
                'bytes': self.bytes,
                'content': 'Hello World'
            },
            'bytes': self.bytes,
            'method': self.method,
            'referrer': self._faker.url()
        }

    @property
    def response(self):
        """A randomly generated response dictionary based on Elastic ECS format

        Returns:
            dict: A random response dictionary containing body, bytes, and status code information 
        """
        return {
            'body': {
                'bytes': self.bytes,
                'content': 'Hello World'
            },
            'bytes': self.bytes,
            'status_code': self.status_code
        }
    
    @property
    def status_code(self):
        """A randomly selected status_code for an HTTP request or response

        Returns:
            str: A randomly selected status code for an HTTP request or response
        """
        return self.random.choice(self._code_map)['code']

    @property
    def method(self):
        """A randomly selected method for an HTTP request or response

        Returns:
            str: A randomly selected method for an HTTP request or response
        """
        return self.random.choice(['get', 'post', 'put', 'patch', 'delete'])
        
    @property
    def bytes(self):
        """Random bytes for an HTTP request

        Returns:
            int: Random bytes for an HTTP request
        """
        return self.random.randint(1,5500)

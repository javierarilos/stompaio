from asyncore import dispatcher


class StompClient(dispatcher):
    """ StompClient handles your messageing to a STOMP 1.2 broker
    """

    def __init__(self, server='127.0.0.1', port=61614):
        dispatcher.__init__(self)
        self.server = server
        self.port = port
        self.buffer = bytes('eoeoeoeoeoee\n', 'ascii')
        self.times = 3

    def do_con(self, user='guest', password='guest'):
        print('>>> about to connect')
        self.create_socket()
        self.connect((self.server, self.port))
        print('>>> after connect')

    def handle_connect(self):
        print('>>> handle_connect')

    def handle_close(self):
        print('>>> handle_close')
        self.close()

    def handle_read(self):
        print('>>> handle_read')
        print(self.recv(8192))

    def writable(self):
        print(f'>>> writable {self.times > 0 and (len(self.buffer) > 0)}')
        return self.times > 0 and (len(self.buffer) > 0)

    def handle_write(self):
        print('>>> handle_write')
        sent = self.send(self.buffer)
        self.times -= 1


class Frame(object):

    @staticmethod
    def from_str(frame_str):
        command, _, rest = frame_str.partition('\n')
        headers_txt, _, body = rest.partition('\n\n')
        headers = {}
        for header_txt in headers_txt.split('\n'):
            header, _, value = header_txt.partition(':')
            headers[header] = value
        return Frame(command=command, headers=headers)

    def __init__(self, command, headers=None):
        self.command = command
        self.headers = headers

    def header(self, header):
        return self.headers.get(header, None)

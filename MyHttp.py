import http.client

class Page:

    def __init__(self, servername, path):
        '''This initialize function sets the servername and path'''
        self.set_target(servername, path)

    def set_target(self, servername, path):
        '''This is a utility function that will reset the servername and the path'''
        self.servername = servername
        self.path = path

    def __get_page(self):
        '''This is a private function that actually goes out and hets the response from the servwer'''

        server = http.client.HTTPConnection(self.servername)
        server.putrequest('GET', self.path)
        server.putheader('Accept', 'text/html')
        server.endheaders()

        return server.getresponse()

    def get_as_string(self):
        '''This function provides the webpage as a string'''
        page = ''
        reply = self.__get_page() #gets the page

        if reply.status != 200:
            page = 'Error sending request [0] [1]'.format(reply.status, reply.reason)
        else:
            data = reply.readlines()
            reply.close()
            for line in data:
                page += line.decode('utf-8')
        return page

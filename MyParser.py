'''
    Parse html from craiglist
'''
from html.parser import HTMLParser

class CIParser(HTMLParser):
    # parser state
    # these vriables store thr=e current state of the parser as it n=reads the file
    date = ''   # the date for the current listing
    title = ''  # the title of the current listing
    link = ''   #the link of the current listing
    collectFor = None #will use this to keep track of what kind of dat awe are currently
                      #collecting for. valid options are:
                    # 'date', 'title', and 'link'
    insideRow = False # this flag keeps track of whether we are inside a row
                        #rows have listing information

    #parser output
    results = '' #the parser's output will be stored here

    def handle_starttag(self, tag, attrs):
        '''This function gets called when the pader encounters a start tag'''
        if tag == 'a' and self.insideRow:
            self.collectFor = 'title'

        for key, value in attrs:

            if (self.collectFor == 'title'
                and key =='href'
                and not self.link): # and not self.link makes sure it doesnt overwrite a preexisting value
                self.link = value

            if key == 'class':
                if value == 'row':
                    self.insideRow = True
                if value == 'ban':
                    self.collectFor = 'date'
    def handle_endtag(self, tag):
        '''This function is called when the parser encounters an end tag'''
        if tag == 'p':
            self.insideRow = False

            # is there data to output?
            if self.title +self.link:
                self.results += "\nDate: \t{0}\nTitle:\t{1}\nlink:\t{2}\n".format(
                    self.date,
                    slef.title,
                    self.link)
                self.__reset_row()

    def handle_data(self, data):
        '''This function is called when the parser encounters data inside to tags'''
        if self.collectFor == 'date':
            self.date = data
        if self.collectFor == 'title' and not self.title:
            self.title = data
        self.collectFor = None #when we're done collecting the data reset this flag

    def __reset__row(self):
        '''This is a utility function to reset the parser's state after a row'''
        self.title = ''
        self.summary = ''
        self.collectFor = None
        self.insideRow = False

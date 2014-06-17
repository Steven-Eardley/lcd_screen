# A class to hold scrollback buffers
#
# Authors: Steven Eardley and Duncan Blair
# Copyright 2014

class scrollBuffer:
    def __init__(self, init_text=None):
        # Create the buffer list
        self.buffer = []
        
        if init_text:
            self.write(init_text)

    def write(self, line_text):
    # writes to the end of the buffer, in 16 char chunks
    # we use strip() to remove trailing spaces across lines
        chunks = [ line_text[i:i+16].strip() for i in range(0, len(line_text), 16) ]
        self.buffer += chunks

    def read_line(self, line_num):
    # reads a specific line from the buffer
        try:
            return self.buffer[line_num]
        except:
            return None

    def length(self):
    # returns the length of the buffer
        return len(self.buffer)

    def read(self, n_lines=2):
    # return the final two lines of the buffer
        return self.buffer[self.length() - n_lines:]

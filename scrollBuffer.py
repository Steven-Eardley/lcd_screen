# A class to hold scrollback buffers
#
# Authors: Steven Eardley and Duncan Blair
# Copyright 2014

class scrollBuffer:
    def __init__(self):
        # Create the buffer list
        self.buffer = ["", ""]

    def write(self, line_text):
    # writes to the end of the buffer
    #TODO: this should break the string into 16-char chunks
        self.buffer.append(line_text)

    def read_line(self, line_num):
    # reads a specific line from the buffer
        return self.buffer[line_num]

    def length(self)
    # returns the length of the buffer
        return len(self.buffer)

    def read(self)
    # this should return the last two lines

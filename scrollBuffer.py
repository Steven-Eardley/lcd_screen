# A class to hold scrollback buffers
#
# Authors: Steven Eardley and Duncan Blair

class scrollBuffer:
    def __init__(self, init_text=None):
        # Create the buffer list
        self.buffer = []
        
        if init_text:
            self.write(init_text)

    def write(self, line_text, clean_breaks=False):
    # writes to the end of the buffer, in 16 char chunks
    # we use strip() to remove trailing spaces across lines
        if clean_breaks:
            self.write_clean(line_text)
        else:
            self.write_simple(line_text)
            
    def write_clean(self, line_text):
    # breaks lines cleanly on word boundaries
        words = line_text.split()
	
        # first word is first chunk(s)
	w0 = words[0]
	chunks = [ w0[i:i+16] for i in range(0, len(w0), 16) ]
    
        # if the word fits in the last chunk, add there, else, form new chunk
	for w in words[1:]:
	    if len(chunks[-1]) + len(w) < 15:
	        chunks[-1] += " " + w
            else:
                chunks += [ w[i:i+16] for i in range(0, len(w), 16) ]
	
	self.buffer += chunks

    def write_simple(self, line_text):
    # writes to buffer, 16 chars at a time
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

    def read_all(self):
	return self.read(len(self.buffer))

    def clear(self):
	self.buffer = []


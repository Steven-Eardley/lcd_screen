# A class to hold scrollback buffers
#
# Authors: Steven Eardley and Duncan Blair

from itertools import tee, izip

class Buffer:
    """
    A Buffer stores the text to be displayed on the screen.
    """

    def __init__(self, init_text=None):
    # create the buffer list
        self.buffer = []

        if init_text:
            self.write(init_text)

    def write(self, line_text):
    # write to the buffer. Must be overridden in subclasses.
        pass

    def read(self):
    # read from the buffer. Must be overridden in subclasses.
        pass

    def read_line(self, line_num):
    # reads a specific line from the buffer
        try:
            return self.buffer[line_num]
        except IndexError:
            return None

    def length(self):
    # returns the length of the buffer
        return len(self.buffer)

    def read_last(self, n_lines=2):
    # return the final two (or more) lines of the buffer
        return self.buffer[self.length() - n_lines:]

    def read_all(self):
        return self.read_last(len(self.buffer))

    def clear(self):
        self.buffer = []


class ScrollBuffer(Buffer):
    """
    The ScrollBuffer ensures all text is on screen at all times, by breaking
    text into 16 character chunks. It can write cleanly, (trying to keep words
    whole) or dirtily.
    """

    # The list of available scroll windows
    window_list = []
    # The index of the window we're viewing
    window_index = 0

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
        self.buffer += [ w0[i:i+16] for i in range(0, len(w0), 16) ]
    
        # if the word fits in the last buffer segment, add there, else, form new chunk
        for w in words[1:]:
            if len(self.buffer[-1]) + len(w) < 15:
                self.buffer[-1] += " " + w
            else:
                self.buffer += [ w[i:i+16] for i in range(0, len(w), 16) ]

    def write_simple(self, line_text):
    # writes to buffer, 16 chars at a time
        self.buffer += [ line_text[i:i+16].strip() for i in range(0, len(line_text), 16) ]

    def scroll_up(self):
    # scroll towards the beginning of the buffer
        if self.window_index > 0:    
	    self.window_index -= 1

    def scroll_down(self):
    # scroll towards the end of the buffer
        if self.window_index < len(list(self.window_list)) - 1:
            self.window_index += 1

    def read(self):
    # read the current window on the buffer
        
        # Every time we read, update the scrolling windows (they may have changed).
        self.window_list = self.window(self.buffer)

	current_lines = []
        for i in list(self.window_list)[self.window_index]:
            current_lines.append(i)
        return current_lines

    @staticmethod
    def window(iterable, size=2):
        iters = tee(iterable, size)
        for i in xrange(1, size):
            for each in iters[i:]:
                next(each, None)
        return list(izip(*iters))

class MarqueeBuffer(Buffer):
    """
    The MarqueeBuffer stores each line of the buffer as-is, and relies on the screen
    to marquee when showing the text.
    """

    def write(self, line_text):
        self.buffer.append(line_text)

import sys


class IO(object):
    def __init__(self, stack):
        self.stack = stack

    def i_chr(self, heap):
        # read a line (input strips newline); push the character code (int)
        val = input()
        if val == "":
            # EOF or empty - push 0
            self.stack.push(0)
        else:
            # push the code of the first character
            self.stack.push(ord(val[0]))
        heap.set()

    def i_int(self, heap):
        num = None
        while type(num) is not int:
            try:
                num = int(input())
            except ValueError:
                pass
        self.stack.push(num)
        heap.set()

    def o_chr(self):
        char = chr(self.stack.pop())
        sys.stdout.buffer.write(char.encode("utf-8"))

    def o_int(self):
        integer = self.stack.pop()
        sys.stdout.buffer.write(str(integer).encode("utf-8"))

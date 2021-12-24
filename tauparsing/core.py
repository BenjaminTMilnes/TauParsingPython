

class Marker(object):
    def __init__(self):
        self.position = 0

    @property 
    def p(self):
        return self.position 

    @p.setter 
    def p(self, value):
        self.position = value 

    def copy(self):
        m = Marker()

        m.p = self.p 

        return m 


def cut(text, startIndex, length=1):
    a = startIndex 
    b = startIndex + length 
    return text[a:b]


class ParsingError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Parser(object):

    def _getWhiteSpace(self, inputText, marker):
        m = marker 
        start = m.p 

        for c in inputText[start:]:
            if c in " \t\n":
                m.p += 1
            else:
                break 

        end = m.p 

        if end == start:
            return None 

        t = inputText[start:end]

        return t 
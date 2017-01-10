class lexicon(object):

    def __init__(self):
        self.whole_char = {
        'north': 'direction',
        'south': 'direction', 
        'east': 'direction',
        'west': 'direction',
        
        'go': 'verb',
        'kill': 'verb', 
        'eat': 'verb', 
        
        'the': 'stop', 
        'in': 'stop', 
        'of': 'stop', 
        
        'bear': 'noun',
        'princess': 'noun',
        }

    def scan(self, stuff):
        words = stuff.split()
        my_result = []
        for n in range(0,len(words)):
            c = words[n]
            a = self.charac(c)
            my_result.append(a)
        return my_result

    def charac(self, c):
        if c in self.whole_char:
            b = self.whole_char[c]
            return b, c
        else:
            return self.int_test(c)

    def int_test(self, c):
        try:
            c = int(c)
            return ('number', c)
        except ValueError:
            return ('error', c)

lexicon = lexicon()
lexicon.scan('north south bear 32 asdfa')
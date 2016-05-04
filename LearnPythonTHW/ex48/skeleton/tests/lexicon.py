class lexicon(object):
    
    whole_words = [('direction', 'north'), ('direction', 'south'), ('direction', 'east'),
                    ('direction', 'west')]
    
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = self.sentence.split(' ')
        self.atr = []
        
        for word in self.words:
            for couple in whole_words:
                if word == couple[1]:
                    self.atr.update(couple)
                    
        return self.atr


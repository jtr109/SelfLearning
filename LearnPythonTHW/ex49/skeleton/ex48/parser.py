# -*- coding: utf-8 -*-

class ParserError(Exception):
    pass
    
    
class Sentence(object):
    
    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]
        
        
def peek(word_list):    # 若存在，读取第一位，返回词性
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None
        

def match(word_list, expecting):    # 弹出word_list首位，词性与期望比较，相同则返回该单词的tuple
    if word_list:
        word = word_list.pop(0)
        
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None
        
        
def skip(word_list, word_type):    # 若word_list首位词性与期待相同，删除单词，直至首位不同
    while peek(word_list) == word_type:
        match(word_list, word_type)
        
    
def parse_verb(word_list):
    skip(word_list, 'stop')
    
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")
        
        
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")
        
    
def parse_subject(word_list):    # 首个非stop单词，若为noun从word_list中弹出，原样返回，若为verb，返回('noun', 'player')
    skip(word_list, 'stop')
    next_word = peek(word_list)
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")
        
        
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    
    return Sentence(subj, verb, obj)
    
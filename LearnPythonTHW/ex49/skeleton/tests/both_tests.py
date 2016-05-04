from nose.tools import *
from ex48 import parser
from ex48 import lexicon


def test_simple():
    result = lexicon.scan("bear eat princess")
    x = parser.parse_sentence(result)
    assert_equal(x.subject, 'bear')
    assert_equal(x.verb, 'eat')
    assert_equal(x.object, 'princess')
    
    
def test_player_and_direction():
    result = lexicon.scan("go east")
    x = parser.parse_sentence(result)
    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'go')
    assert_equal(x.object, 'east')
    
    
def test_stop():
    result = lexicon.scan("the bear of it go in east")
    x = parser.parse_sentence(result)
    assert_equal(x.subject, 'bear')
    assert_equal(x.verb, 'go')
    assert_equal(x.object, 'east')

    
def test_error_subject():
    result = lexicon.scan("in east")
    x = parser.parse_sentence(result)
    '''
    assert_equal(x.subject, 'bear')
    assert_equal(x.verb, 'go')
    assert_equal(x.object, 'east')
    '''
    

def test_error_verb():
    result = lexicon.scan("the bear of it in east")
    x = parser.parse_sentence(result)
    '''
    assert_equal(x.subject, 'bear')
    assert_equal(x.verb, 'go')
    assert_equal(x.object, 'east')
    '''
    
    
def test_error_object():
    result = lexicon.scan("the bear of it go in ")
    x = parser.parse_sentence(result)
    '''
    assert_equal(x.subject, 'bear')
    assert_equal(x.verb, 'go')
    assert_equal(x.object, 'east')
    '''
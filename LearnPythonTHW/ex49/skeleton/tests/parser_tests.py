from nose.tools import *
from ex48 import parser


def test_simple():
    x = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('noun', 'honey')])
    assert_equal(x.subject, 'bear')
    assert_equal(x.verb, 'eat')
    assert_equal(x.object, 'honey')
    
    
def test_player_and_direction():
    x = parser.parse_sentence([('verb', 'go'), ('direction', 'east')])
    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'go')
    assert_equal(x.object, 'east')
    
    
def test_stop():
    x = parser.parse_sentence([('stop', 'the'), ('noun', 'bear'), 
                        ('stop', 'that'), ('stop', 'it'), ('verb', 'go'), 
                        ('stop', 'to'), ('noun', 'east')])
    assert_equal(x.subject, 'bear')
    assert_equal(x.verb, 'go')
    assert_equal(x.object, 'east')

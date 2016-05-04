def scan(sentence):
    words = sentence.split()
    result = []
  
    stuff = {'direction':['north', 'south', 'east', 'west','down', 'up', 'left', 'right', 'back'],
            'verb':['go', 'stop', 'kill', 'eat'],
            'stop':['the', 'in', 'of', 'from', 'at', 'it'],
            'noun':['door', 'bear', 'princess', 'cabinet']}

    for word in words:
        if is_number(result, word):
            continue
        elif is_in_stuff(stuff, result, word):
            continue
        else:
            couple = ('error', word)
            result.append(couple)

    return result

    
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
    
    
def is_number(result, word):
    number = convert_number(word)
    if number != None :
        word = number
        couple = ('number', word)
        result.append(couple)
        return True
    else:
        return False

        
def is_in_stuff(stuff, result, word):
    in_stuff = False
    for key in stuff.keys():
        for value in stuff[key]:
            if word == value:
                couple = (key, word)
                result.append(couple)
                in_stuff = True
                break
        if in_stuff:
            break    
    if in_stuff:
        return True
    else:
        return False
        
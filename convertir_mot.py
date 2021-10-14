def mot_derive(motEntrant, terminaison):
    if motEntrant[-1] == 'e' and motEntrant[-2] != 'i':
        motEntrant = motEntrant[:-1]
    if motEntrant[-1] == 'e' and motEntrant[-2] == 'i':
        motEntrant = motEntrant[:-2]
    motDerive = motEntrant + terminaison
    return motDerive

def get_number_last_char(motEntrant):

    if motEntrant[-1] == 'e' and motEntrant[-2] != 'i':
        return 1
    elif motEntrant[-1] == 'e' and motEntrant[-2] == 'i':
        return 2
    elif motEntrant[-1] == 'r' and motEntrant[-2] == 'e':
        return 2
    else:
        return -1


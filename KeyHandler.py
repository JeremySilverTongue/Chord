class KeyHandler:

    current_keys_down = set()
    chord = set()
    building_chord = True
    word = ""

ef onKeyPress(event):

    if building_chord:
        chord.add(event.char)
    current_keys_down.add(event.char)
    showWord()
    # showCurrentKeysDown()


   # text.delete(1.0, tk.END)
    #text.insert('end', 'You pressed %s\n' % (event.char, ))

# def showCurrentKeysDown():
#     text.delete(1.0, tk.END)
#     for key in current_keys_down:
#         text.insert('end', key)

def showWord():
    text.delete(1.0, tk.END)
    text.insert('end', word)



def onKeyRelease(event):
    building_chord = False
    current_keys_down.remove(event.char)
    if len(current_keys_down) == 0:
        print "Chord finished", chord
        if frozenset(chord) in MAPPING:
            global word
            print "You did a recognized chord!", MAPPING[frozenset(chord)]
            word += MAPPING[frozenset(chord)]
        chord.clear()
        building_chord = True
    showWord()

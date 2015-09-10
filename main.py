import Tkinter as tk

import ChordMappingParser
import ChordDecoder
import Fingers

KEYS_MAPPING = {
    "7" : Fingers.INDEX,
    "8" : Fingers.MIDDLE,
    "9" : Fingers.RING,
    "0" : Fingers.PINKY,
    "b" : Fingers.THUMB1,
    "n" : Fingers.THUMB2,
}

chord_mapping = ChordMappingParser.parse_mapping_CSV("mapping.csv")

decoder = ChordDecoder.ChordDecoder(KEYS_MAPPING, chord_mapping)



current_keys_down = set()
chord = set()
building_chord = True
word = ""

def onKeyPress(event):
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
        decoded = decoder.decode_chord(chord)
        # print "Chord finished", decoded, chord
        global word
        word += decoded
        chord.clear()
        building_chord = True
    showWord()







root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))

text.pack()
root.bind('<KeyPress>', onKeyPress)
root.bind("<KeyRelease>", onKeyRelease)
root.mainloop()

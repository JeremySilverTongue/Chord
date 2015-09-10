class ChordDecoder(object):
    """docstring for ChordDecoder"""

    key_mapping = {}
    chord_mapping = {}

    def __init__(self, key_mapping, chord_mapping):
        super(ChordDecoder, self).__init__()
        self.key_mapping = key_mapping
        self.chord_mapping = chord_mapping
        print chord_mapping

    def decode_chord(self, keys):
        result = self.fingers_to_character(self.keys_to_fingers(keys))
        # print "Decoding:", keys, " as ", result

        return result


    def keys_to_fingers(self, keys):
        fingers = set()
        for key in keys:
            if key in self.key_mapping:
                fingers.add(self.key_mapping[key])
        return frozenset(fingers)

    def fingers_to_character(self,fingers):
        pretty_fingers = ", ".join(fingers)
        result = self.chord_mapping.get(fingers, "")
        print "Decoding: {} as {}".format(pretty_fingers, result)
        return self.chord_mapping.get(fingers, "")


def main():
    import Fingers
    decoder = ChordDecoder()




if __name__ == '__main__':
    main()






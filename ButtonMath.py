from scipy.special import binom


buttons = 3
rockers = 2





def enumerate_chords(buttons, rockers):
    for fingers in range(1, buttons + rockers + 1):
        print "{}: {}".format(fingers, chords_per_finger_count(buttons, rockers, fingers))

def chords_per_finger_count(buttons, rockers, fingers):
    # print "How many ways are there to put {fingers} fingers on {buttons} buttons and {rockers} rockers?".format(fingers = fingers, buttons = buttons, rockers = rockers)
    count = 0
    for fingers_on_buttons in range(fingers+1):
        fingers_on_rockers = fingers - fingers_on_buttons;
        if fingers_on_rockers <= rockers and fingers_on_buttons <= fingers_on_buttons:
            button_combinations = binom(buttons, fingers_on_buttons)
            # print "There are {} ways to put {} fingers on {} buttons".format(button_combinations, fingers_on_buttons, buttons)
            rocker_combinations =binom(rockers, fingers_on_rockers) * 2 ** (fingers_on_rockers)
            # print "There are {} ways to put {} fingers on {} rockers".format(rocker_combinations, fingers_on_rockers, rockers)
            count += button_combinations * rocker_combinations
            # print "If {fingers_on_buttons} are on the buttons and {fingers_on_rockers} are on the rockers, then there are {new_possibilities} ".format(fingers_on_buttons = fingers_on_buttons, fingers_on_rockers = fingers_on_rockers, new_possibilities = button_combinations * rocker_combinations)
    return count

enumerate_chords(buttons, rockers)

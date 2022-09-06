keysequences = []
keylog = []
output = []
# sequenceoutput = []

def Register(keypress_sequence, action_type):
    pairs = (keypress_sequence, action_type)
    keysequences.append(pairs)


def Keypress(char):
    keylog.append(char)
    string = ""

    for seq, act in keysequences:
        # for index in seq:
        #     if char == index:
        #         sequenceoutput.append(char)
            if string.join(keylog) == seq:
                out = act
                output.append(act)

    print(output)

Register("UDLR", "Run")
Register("DLRR", "Jump")
Register("UDL", "Fly")
Keypress("U")
Keypress("D")
Keypress("L")
Keypress("R")
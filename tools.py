#_____________________________Clear Screen__________________________________
def CLEAR_SCREEN():
    print ("\n" * 100)
    return

#_____________________________Print List__________________________________
def PRINT_LIST(display):
    first = ", ".join(display[0:(len(display)-1)])
    last = "".join(display[(len(display)-1):])
    print  "%s, and %s" % (first, last)
    return

#_____________________________Print Enumerated List__________________________________
def ENUM_LIST(display):
    print ' '.join('{}: {}'.format(*i) for i in enumerate(display, 1),)
    return
# -*- coding: utf-8 -*-
def preprocess_input(input):
    punctuations = u"/;,.!?”:()[]"
    output = input
    for punctuation in punctuations:
        output = output.replace(punctuation, u" %s " % punctuation)
    return output

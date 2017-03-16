# -*- coding: utf-8 -*-
import re


def preprocess_input(text):
    punctuations = u"/;,.!?”:()[]"
    output = text
    for punctuation in punctuations:
        output = output.replace(punctuation, u" %s " % punctuation)
    return output


def postprocess_output(text):
    def replace_method(match):
        match_item = match.group(1)
        match_item = match_item.replace(" ", "_")
        return match_item

    pattern = r"\[([^\]]*)\]"
    output = re.sub(pattern, replace_method, text)
    return output

# -*- coding: utf-8 -*-
import re

input = "[a b]"
input = "[a b] [c d e] [g] [h i j k]"


# pattern1 = r"\[(.*)\]"
# output1 = re.sub(pattern1, r"\1", input)

# pattern2 = r"\[([^\]]*)\]"
# output2 = re.sub(pattern2, r"\1", input)

def post_process_output(text):
    def replace_method(match):
        match_item = match.group()
        match_item = match_item[1:-1]
        match_item = match_item.replace(" ", "_")
        return match_item
    pattern = r"\[([^\]]*)\]"
    output = re.sub(pattern, replace_method, text)
    return output


def replace_method(match):
    match_item = match.group(1)
    match_item = match_item.replace(" ", "_")
    return match_item
pattern3 = r"\[([^\]]*)\]"
output3 = re.sub(pattern3, replace_method, input)

input2 = u"[Hà Nội] [mùa này] [vắng] [những] [cơn mưa]"
pattern3 = r"\[([^\]]*)\]"
output3 = re.sub(pattern3, replace_method, input2)
print 0

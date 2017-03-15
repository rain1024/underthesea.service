# -*- coding: utf-8 -*-
#!/usr/bin/python
from pyvi.pyvi import ViTokenizer, ViPosTagger

import sys, getopt
from os.path import exists


def main(argv):
    input_file = 'input.txt'
    output_file = 'output.txt'
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    if not exists(input_file):
        print "Cannot open", input_file
        return
    content = open(input_file, "r").read()
    content = content.decode("utf-8")
    output = ViTokenizer.tokenize(content)
    output = output.encode("utf-8")
    open(output_file, "w").write(output)


if __name__ == "__main__":
    main(sys.argv[1:])

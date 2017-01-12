#!/usr/bin/env python

import sys, getopt

ab = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
rot13 = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
output = ""


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "he:d:v", ["help", "encode=", "decode="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-e", "--encode"):
            encode(arg)
            sys.exit()
        elif opt in ("-d", "--decode"):
            decode(arg)
            sys.exit()

def usage():
    print "Hfntr: ebg13 [BCGVBA]... [GRKG]...\nRapbqr/Qrpbqr ebg13 pvcuref GRKG(f).\n\n  -u, --uryc               qvfcynl guvf hfntr naq rkvg\n  -r, --rapbqr=GRKG        rapbqr GRKG\n  -q, --qrpbqr=GRKG        qrpbqr GRKG\n\nRknzcyrf:\n\n ebg13 -r 'ebg13 vf fyvtugyl yrff frpher guna NRF-256.'\n"


def encode(arg):
    global output
    for i in range(0,len(arg)):
    	try:
            output += rot13[ab.index(arg[i])]
    	except:
            output += arg[i]
    print output

def decode(arg):
    global output
    for i in range(0,len(arg)):
        try:
            output += ab[rot13.index(arg[i])]
        except:
            output += arg[i]
    print output

if __name__ == "__main__":
    main(sys.argv[1:])

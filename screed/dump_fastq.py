#!/usr/bin/env python

# Copyright (c) 2008-2010, Michigan State University
# Copyright (C) 2016, The Regents of the University of California.

from __future__ import print_function
from screed import ToFastq
import argparse
import sys
import os


# Shell interface to the ToFastq screed conversion function
def main(args):
    parser = argparse.ArgumentParser(
        description="Convert a screed database to a FASTA file")
    parser.add_argument('dbfile')
    parser.add_argument('outputfile', default='/dev/stdout', nargs='?')
    args = parser.parse_args(args)

    if not os.path.isfile(args.dbfile):
        print("No such file: %s" % args.dbfile)
        exit(1)

    n = ToFastq(args.dbfile, args.outputfile)

    sys.stderr.write('Wrote {} records in FASTQ format.\n'.format(n))


if __name__ == '__main__':
    main(sys.argv[1])

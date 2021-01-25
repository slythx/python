#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b', metavar='[BRAND]',
        help='to specify brand (default: ANSWERS)')
parser.add_argument('-e', metavar='[ENVIRONMENT]', 
        help='to specify environment (default: STAGING)')
parser.add_argument('-usid', metavar='[user_segment_id]', required=True,
        help='Signed-in User segment id of articles')
args = parser.parse_args()
print(args.b)

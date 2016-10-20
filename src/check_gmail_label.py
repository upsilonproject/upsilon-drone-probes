#!/usr/bin/env python

import sys
import imaplib
import email
import datetime
from argparse import ArgumentParser
from upsilon.serviceHelpers import exit

parser = ArgumentParser()
parser.add_argument('--email', required = True)
parser.add_argument('--keyring', default = None)
args = parser.parse_args()

if args.keyring == "kwallet":
    from PyKDE4 import KWallet

import keyring

imap = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    imap.login(args.email, keyring.get_password("system", "xconspirisist@gmail.com"))
except imaplib.IMAP4.error as e:
    exit(message = "failed to login: " + str(e))

rv, mailboxes = imap.list()

if rv == 'OK':
    print mailboxes


imap.logout()

#rv, data = imap.select

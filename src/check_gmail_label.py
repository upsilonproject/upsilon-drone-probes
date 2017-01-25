#!/usr/bin/python

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import argparse

from upsilon import serviceHelpers

parser = argparse.ArgumentParser(parents=[tools.argparser])
parser.add_argument('labels', nargs = '*', default = []);
parser.add_argument('--csv', action = 'store_true');
parser.add_argument('--metricsTotal', action = 'store_true');
parser.add_argument('--countCritical', default = 30)
parser.add_argument('--countWarning', default = 5)
args = parser.parse_args();

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.metadata'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if args:
            credentials = tools.run_flow(flow, store, args)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def getKarma(karma):
    if karma > args.countCritical: 
        return "BAD"

    if karma > args.countWarning:
        return "WARNING"

    return "GOOD"

def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    if len(args.labels) == 0:
        results = service.users().labels().list(userId='me').execute()

        labels = results.get('labels', [])
    else:
        labels = args.labels

    print(labels)

    metadata = serviceHelpers.clsmetadata()

    if not labels:
        print('No labels found.')
    else:
      print('Labels:')
      for label in labels:
        label_info = service.users().labels().get(id = label, userId = 'me').execute()

        if args.csv:
            print(label_info['name'], ",", label_info['threadsTotal'], ",", label_info['threadsUnread'])
        else:
            print(label_info['name'], label_info['threadsUnread'], '/', label_info['threadsTotal'])

        if args.metricsTotal: 
            metric = metadata.addMetric(label_info['id'] + '_total', label_info['threadsTotal'], getKarma(label_info['threadsTotal']))
            metric['caption'] = label_info['name'] + ' Total'

    serviceHelpers.exitOk(metadata);


if __name__ == '__main__':
    main()

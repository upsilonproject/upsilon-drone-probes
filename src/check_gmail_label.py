#!/usr/bin/python

from __future__ import print_function
import httplib2
import os
import json

from googleapiclient import discovery, http
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import time
from datetime import datetime
import time

import argparse

from upsilon import serviceHelpers

parser = argparse.ArgumentParser(parents=[tools.argparser])
parser.add_argument('labels', nargs = '*', default = []);
parser.add_argument('--csv', action = 'store_true');
parser.add_argument('--metricsTotal', action = 'store_true');
parser.add_argument('--evalMessages', action = 'store_true');
parser.add_argument('--countCritical', default = 30)
parser.add_argument('--countWarning', default = 5)
parser.add_argument('--clientSecretFile', default = 'client_secrets.json')
args = parser.parse_args();

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.metadata'
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
        flow = client.flow_from_clientsecrets(args.clientSecretFile, SCOPES)
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

def onMessage(req, resp, err):
    global evaledThreads
    evaledThreads.append(resp)

evaledThreads = []

def evalMessages(service, label):
    fetchLabelIds = [label['id']]

    print("evalMessages, fetch label IDs:", fetchLabelIds)

    response = service.users().threads().list(userId = 'me', labelIds = fetchLabelIds).execute()
    threads = []

    if "threads" in response:
        threads.extend(response['threads'])

    while "nextPageToken" in response:
        page_token = response['nextPageToken']
        response = service.users().threads().list(userId = 'me', labelIds = fetchLabelIds, pageToken = page_token).execute()
        threads.extend(response['threads'])
        print("getting more messages:" + str(len(threads)))

    batch = service.new_batch_http_request();

    for thread in threads:
        batch.add(service.users().threads().get(userId = 'me', id = thread['id'], format = "minimal"), callback=onMessage)

    global evaledThreads
    evaledThreads = []

    batch.execute();

    print("finished eval messages")

    timestamps = []
    for thread in evaledThreads:
        latestTimestamp = 0

        if thread == None or thread['messages'] == None:
            continue;

        for message in thread['messages']:
            if message['internalDate'] > latestTimestamp:
                latestTimestamp = int(message['internalDate']) / 1000

        timestamps.append(datetime.fromtimestamp(latestTimestamp))

    return timestamps

def addMetricsForTimestamps(metadata, labelName, threadTimestamps):
    now = datetime.today()

    lastWeek = []
    lastMonth = []
    older = []

    for timestamp in threadTimestamps:
        diff = now - timestamp

        if diff.days < 7:
            lastWeek.append(timestamp)
        if diff.days < 30:
            lastMonth.append(timestamp)
        else:
            older.append(timestamp)

    metadata.addMetric(labelName + ' in the last week', len(lastWeek), 'UNKNOWN')
    metadata.addMetric(labelName + ' in the last month', len(lastMonth), 'UNKNOWN')
    metadata.addMetric(labelName + '_older', len(older), 'UNKNOWN')
    print("added metrics")

def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    if len(args.labels) == 0:
        results = service.users().labels().list(userId='me').execute()

        labels = results.get('labels', [])
    else:
        labels = []

        for label in args.labels:
            labels.append({'id': label})

    metadata = serviceHelpers.clsmetadata()

    if not labels:
        print('No labels found.')
        return

    for label in labels:
        label_info = service.users().labels().get(id = label['id'], userId = 'me').execute()

        if args.csv:
            print(label_info['name'], ",", label_info['threadsUnread'], ",", label_info['threadsTotal'])
        else:
            print(label_info['name'], label_info['threadsUnread'], '/', label_info['threadsTotal'])

        if args.metricsTotal: 
            metric = metadata.addMetric(label_info['id'] + '_total', label_info['threadsTotal'], getKarma(label_info['threadsTotal']))
            metric['caption'] = label_info['name'] + ' Total'

        if args.evalMessages:
            threadTimestamps = evalMessages(service, label);

            addMetricsForTimestamps(metadata, label_info['name'], threadTimestamps)

    serviceHelpers.exitOk(metadata);


if __name__ == '__main__':
    main()

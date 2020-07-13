import email
import imaplib
import re
import time
from datetime import date
import pyautogui as pg
from imap_tools import MailBox, Q

def get_credentials(file):
	inFile = open(file, 'r')
	data = []
	for line in inFile:
		data.append(line.rstrip())
	return data


def access_mail(username, password, server):
	mail = imaplib.IMAP4_SSL(server)
	mail.login(username, password)
	return mail


def decode_messages(response):
	if isinstance(response, tuple):
		global message, mail_content
		message = email.message_from_bytes(response[1])
		mail_content = message['content']
		if message.is_multipart():
			mail_content = ''
			for part in message.get_payload():
				if part.get_content_type() == 'text/plain':
					mail_content += part.get_payload()
		else:
			mail_content = message.get_payload()


def find_url(text):
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s(" \
            r")<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])) "
	url = re.findall(regex, text)
	return [x[0] for x in url]


def find_attendance_messages(mail, password, server, argument, request):
	mail = access_mail(mail, password, server)
	mail.select('inbox')
	# parse all the messages as a list of bytes
	#if flag != '':
	#	status, data = mail.search(None, flag, argument, request)
	#else:
	status, data = mail.search(None, 'FROM', 'rperlowitz@ermurrowhs.org', argument, request)
	# list to store and split the bytes
	mail_ids = []
	for block in data:
		mail_ids += block.split()

	for i in mail_ids:
		status, data = mail.fetch(i, 'RFC822')
		for response_part in data:
			decode_messages(response_part)

		#if mailDate == today:
		print(f"From: {message['from']}")
		# print(f'Subject: {mail_subject}')
		# print(f'Date: {mail_date}')
		return find_url(mail_content)
		# return mail_data['content']


# MAIN
'''
UPDATES:
    6/1/20
    Add a hot-key in pyautogui('winleft')
    Add commands :
        write 'chrome\n' 
        try to find the input fields through inspection.
        if not use the hard codding through mouse, and pg.position()
        place the values in the fields using the data from the variables.
'''
before = time.time()
PATH = 'C:/Users/megan/Desktop/attendance/attendance.txt'

ADDRESSES = ['rperlowitz@ermurrowhs.org', ]

EMAIL = 'nfarukhzoda6058@ermurrowhs.org'
PASSWORD = '242306058'
SERVER = 'imap.gmail.com'
today = date.today().strftime('%b %#d %Y')
get_credentials(PATH)
# Doesn't properly work
print(find_attendance_messages(EMAIL, PASSWORD, SERVER, 'TEXT', 'Attendance'))
# print(find_attendance_messages(EMAIL, PASSWORD, SERVER, 'FROM', 'no-reply+681bde2b@classroom.google.com', False))
# print(find_attendance_messages(EMAIL, PASSWORD, SERVER, 'FROM', "'rperlowitz@ermurrowhs.org'", 'UNSEEN'))
after = time.time()
print(after - before)

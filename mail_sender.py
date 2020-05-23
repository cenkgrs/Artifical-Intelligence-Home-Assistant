import smtplib
import imaplib
import email
import config
import random
import speech_recognition as sr
import answers
import pyttsx3
from datetime import datetime
import time

imaplib._MAXLINE = 1000000

SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993


# Runs when Oracle speaks
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english+f3')
    engine.say(text)
    engine.runAndWait()


'''r = sr.Recognizer()
r.energy_threshold = 4000
source = sr.Microphone()'''


def listen():
    command = ""
    with sr.Microphone(sample_rate=12000) as source:
        os.system('play -nq -t alsa synth {} sine {}'.format(0.15,
                                                             500))  # 1 = duration, 440 = frequency -> this sounds a beep

        audio = r.record(source, duration=4)
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + ' \n')
    except sr.UnknownValueError:
        # speak("Did not get that sir")
        print("Google Speech Recognition could not understand audio")
        listen()
    except sr.RequestError as e:
        print("Sorry, the service is down; {0}".format(e))
        listen()
    return command


def send_mail(subject, msg, to_email):
    try:
        print(subject, msg, to_email)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, to_email, message)
        server.quit()

        return True
    except Exception as e:
        return False


def get_mail_info():
    subject = listen()
    speak("And the message is ?")
    msg = listen()
    speak('''Can you select a contact from the list below sir ?
            1 is cenkgrs@gmail.com
            2 is joonjazzar15@gmail.com
            3 is cenk@digitaltrade.com.tr''')

    case = listen()

    to_email = config.mail_contact.get(case, "Invalid number")

    speak(random.choice(answers.complete_a))

    status = send_mail(subject, msg, to_email)

    if status:
        speak("Email sended successfully boss")
    else:
        speak("Email failed to sent")


def read_email_from_gmail():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(config.EMAIL_ADDRESS, config.PASSWORD)
    mail.select('inbox')

    type, data = mail.search(f'DATE:{datetime()}', '(All)')

    mails_ids = data[0]
    mails_ids = mails_ids.split()
    mails_ids.sort(reverse=True)

    mails_id_list = mails_ids[:10]

    for i in mails_id_list:
        # the fetch function fetch the email given its id
        status, data = mail.fetch(i, '(RFC822)')
    for response_part in data:
        # so if its a tuple...
        print(response_part)
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])
            mail_from = message['from']
            mail_subject = message['subject']

            if message.is_multipart():
                mail_content = ''

                for part in message.get_payload():
                    # if the content type is text/plain
                    # we extract it
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:
                mail_content = message.get_payload()

            print(f'From: {mail_from}')
            print(f'Subject: {mail_subject}')
            print(f'Content: {mail_content}')


def check_new_email():
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(config.EMAIL_ADDRESS, config.PASSWORD)
    mail.list()

    latest_email_uid = ''

    while True:
        mail.select("Inbox", readonly=True)
        result, data = mail.uid('search', None, "ALL")  # search and return uids instead
        ids = data[0]  # data is a list.+
        id_list = ids.split()  # ids is a space separated string

        if data[0].split()[-1] == latest_email_uid:
            time.sleep(120)  # put your value here, be sure that this value is sufficient ( see @tripleee comment below)
        else:
            result, data = mail.uid('fetch', latest_email_uid,
                                    '(RFC822)')  # fetch the email headers and body (RFC822) for the given ID
            raw_email = data[0][1]
            latest_email_uid == data[0].split()[-1]
            time.sleep(120)  # put your value here, be sure that this value is sufficient ( see @tripleee comment below)




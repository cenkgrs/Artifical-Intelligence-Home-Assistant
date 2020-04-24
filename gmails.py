import email
import imaplib
import ctypes
import getpass
mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
unm = "cenkgrs@gmail.com"
pwd = getpass.getpass("Plese input your password : ")

mail.login(unm, pwd)
mail.select("INBOX")


def loop():
    mail.select("INBOX")
    n = 0  # Unseen messages
    (retcode, messages) = mail.search(None, '(UNSEEN)')

    if retcode == 'OK':
        for num in messages[0].split():
            n = n + 1
            print(n)
            typ, data = mail.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance( response_part, tuple):
                    original = email.message_from_string(response_part[1])
                    print(original['From'])
                    data = original['Subject']
                    print(data)
                    typ, data = mail.store(num, '+FLAGS', '\\Seen')

    print(n)


if __name__ == '__main__':
    try:
        while True:
            loop()
    finally:
        print("Thanks")
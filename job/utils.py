from drymail import SMTPMailer, Message


def notify(email, text):
    client = SMTPMailer(host='smtp.yandex.ru', port='465', user='md5-light@yandex.ru', password='12345qwe', ssl=True)
    message = Message(subject='It\'s all done', sender=('Flask server', 'md5-light@yandex.ru'),
                      receivers=[('', email)], text=text)

    client.send(message)

from abc import ABC, abstractmethod


class Email:
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.format_content()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


class IContent:
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def format_content(self):
        pass


class MyContent(IContent):
    def format_content(self):
        return f'My {self.content}'


class HTMLContent(IContent):
    def format_content(self):
        return f'<content>{self.content}</content>'


class JSONContent(IContent):
    def format_content(self):
        return ':{\n' + self.content + "\n}"


email = Email("IM")
email.set_sender("qmal")
email.set_receiver("james")
content = JSONContent("Hello, there!")
email.set_content(content)
print(email)

from abc import ABC, abstractmethod


class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.conversations = []

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info

    def get_contact_info(self):
        return self._contact_info

    def create_conversation(self, users):
        conversation = Conversation(users)
        self.conversations.append(conversation)
        for user in users:
            if user != self:
                user.conversations.append(conversation)
        return conversation

    def send_message(self, conversation, content):
        message = TextMessage(self, conversation, content)
        conversation.add_message(message)

    def receive_message(self, message):
        print(f"{message.sender.name}: {message.content}")


class Conversation:
    def __init__(self, users):
        self.users = list(set(users))
        self.messages = []

    def add_message(self, message):
        if message not in self.messages:
            self.messages.append(message)
            for user in self.users:
                if user != message.sender:
                    user.receive_message(message)


class Message(ABC):
    def __init__(self, sender, conversation, content):
        self.sender = sender
        self.conversation = conversation
        self.content = content

    @abstractmethod
    def send(self):
        pass


class TextMessage(Message):
    def send(self):
        self.conversation.add_message(self)


class MultimediaMessage(Message):
    def __init__(self, sender, conversation, content, media):
        super().__init__(sender, conversation, content)
        self.media = media

    def send(self):
        self.conversation.add_message(self)


user1 = User("Alice", "alice@example.com")
user2 = User("Bob", "bob@example.com")
user3 = User("Charlie", "charlie@example.com")

conversation1 = user1.create_conversation([user2, user3])
user1.send_message(conversation1, "Hi everyone!")
user2.send_message(conversation1, "Hey Alice and Charlie!")
user3.send_message(conversation1, "What's up?")

conversation2 = user2.create_conversation([user1])
user2.send_message(conversation2, "How's it going?")
user1.send_message(conversation2, "Not bad, thanks!")

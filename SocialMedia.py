from abc import ABC, abstractmethod


class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info


class Post:
    def __init__(self, user, content, timestamp):
        self.user = user
        self.content = content
        self.timestamp = timestamp
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)


class Comment:
    def __init__(self, user, content, timestamp):
        self.user = user
        self.content = content
        self.timestamp = timestamp


class SocialMedia(ABC):
    @abstractmethod
    def create_post(self, user, content):
        pass

    @abstractmethod
    def share_post(self, post):
        pass

    @abstractmethod
    def add_comment(self, post, user, content):
        pass

    @abstractmethod
    def interact_with_user(self, user1, user2):
        pass


class TextPost(Post):
    pass


class PhotoPost(Post):
    pass


class Facebook(SocialMedia):
    def __init__(self):
        self.users = []
        self.posts = []

    def create_post(self, user, content):
        post = TextPost(user, content, datetime.now())
        self.posts.append(post)
        return post

    def share_post(self, post):
        print("{} shared a post by {} on Facebook.".format(user.name, post.user.name))

    def add_comment(self, post, user, content):
        comment = Comment(user, content, datetime.now())
        post.add_comment(comment)
        return comment

    def interact_with_user(self, user1, user2):
        print("{} sent a friend request to {} on Facebook.".format(user1.name, user2.name))


# Create some users
user1 = User("John Doe", "john.doe@example.com")
user2 = User("Jane Doe", "jane.doe@example.com")

# Create a Facebook account and add the users
facebook = Facebook()
facebook.users.append(user1)
facebook.users.append(user2)

# John creates a post
post1 = facebook.create_post(user1, "Hello, world!")

# Jane shares John's post
facebook.share_post(post1)

# Jane comments on John's post
comment1 = facebook.add_comment(post1, user2, "Hi, John!")

# John interacts with Jane
facebook.interact_with_user(user1, user2)

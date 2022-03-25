class SocialMedia:
    def __init__(self):
        self.name = None

    def give_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Instagram(SocialMedia):
    def __init__(self):
        self.give_name("Instagram")
        self.user = []
        self.password = []
        self.post = [[None for _ in range(150)] for _ in range(50)]

    def sign_up(self):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        self.user.append(username)
        self.password.append(password)

    def check(self, username_, password_):
        for counter in range(len(self.user)):
            if username_ == self.user[counter] and password_ == self.password[counter]:
                return True

    def give_user_num(self, username_):
        for counter in range(len(self.user)):
            if username_ == self.user[counter]:
                return counter
        return -1

    def give_post_num(self, username_):
        num = self.give_user_num(username_)
        for counter2 in range(50):
            if self.post[num][counter2] is None:
                return counter2
        return -1

    def publish_new_post(self):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        if self.check(username, password):
            post = input("You can write down your post : ")
            if len(post) < 2200:
                row = self.give_user_num(username)
                column = self.give_post_num(username)
                self.post[row][column] = post
            else:
                print("your post is too long!")
        else:
            print("your username or password is wrong!")

    def get_posts(self):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        if self.check(username, password):
            for counter in range(self.give_post_num(username)):
                print(self.post[self.give_user_num(username)][counter])
        else:
            print("your username or password is wrong!")


class Twitter(SocialMedia):
    def __init__(self):
        self.give_name("Twitter")
        self.user = []
        self.password = []
        self.post = [[None for _ in range(150)] for _ in range(50)]

    def sign_up(self):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        self.user.append(username)
        self.password.append(password)

    def check(self, username_, password_):
        for counter in range(len(self.user)):
            if username_ == self.user[counter] and password_ == self.password[counter]:
                return True

    def give_user_num(self, username_):
        for counter in range(len(self.user)):
            if username_ == self.user[counter]:
                return counter
        return -1

    def give_post_num(self, username_):
        num = self.give_user_num(username_)
        for counter2 in range(50):
            if self.post[num][counter2] is None:
                return counter2
        return -1

    def create_new_tweet(self):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        if self.check(username, password):
            post = input("You can write down your post : ")
            if len(post) < 280:
                row = self.give_user_num(username)
                column = self.give_post_num(username)
                self.post[row][column] = post
            else:
                print("your post is too long!")
        else:
            print("your username or password is wrong!")

    def get_tweets(self):
        username = input("Please enter your username : ")
        password = input("Please enter your password : ")
        if self.check(username, password):
            for counter in range(self.give_post_num(username)):
                print(self.post[self.give_user_num(username)][counter])
        else:
            print("your username or password is wrong!")


if __name__ == '__main__':
    Insta = Instagram()
    Twit = Twitter()
    command = ""
    command2 = ""
    command3 = ""
    while command != "3":
        print("Please write command!")
        print("1 to Open Instagram")
        print("2 to Open Twitter")
        print("3 to Exit")
        print()
        print()
        print()
        command = input()
        if command == "1":
            while command2 != "5":
                print("Please write command!")
                print("1 to publish new post")
                print("2 to get posts")
                print("3 to get app name")
                print("4 to sign up")
                print("5 to Exit")
                print()
                command2 = input()
                if command2 == "1":
                    Insta.publish_new_post()
                if command2 == "2":
                    Insta.get_posts()
                if command2 == "3":
                    print(Insta.get_name())
                if command2 == "4":
                    Insta.sign_up()
                if command2 == "5":
                    command2 = "0"
                    break
        if command == "2":
            while command3 != "5":
                print("Please write command!")
                print("1 to create new tweet")
                print("2 to get tweets")
                print("3 to get app name")
                print("4 to sign up")
                print("5 to Exit")
                print()
                command3 = input()
                if command3 == "1":
                    Twit.create_new_tweet()
                if command3 == "2":
                    Twit.get_tweets()
                if command3 == "3":
                    print(Twit.get_name())
                if command3 == "4":
                    Twit.sign_up()
                if command3 == "5":
                    command3 = "0"
                    break
    
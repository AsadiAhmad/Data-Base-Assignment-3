class SocialMedia:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Instagram:
    instance1 = SocialMedia("Instagram")

class Twitter:
    instance2 = SocialMedia("Twitter")


if __name__ == '__main__':
    print()
    
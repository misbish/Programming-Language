class Hello:
    def __init__(self):
        pass

    def display(self):
        self.is_not_used()
        print("Hello World")

    def is_not_used(self):
        pass


if __name__ == '__main__':
    hello = Hello()
    hello.display()

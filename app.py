print("Middle branch")
print("hello python!!")



def greet(name):
    if name.strip() == "":
        return "Hello, stranger 👋"
    return f"Hello, {name}! Welcome to Git collaboration."

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))


import random
import string

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def password_generate(self):
        try:
            words = input("Enter some words: ")
            word_list = words.split()
            if len(word_list) < 2:
                raise ValueError("Please enter at least two words")
            chosen = random.choice(word_list)
            special_char = random.choice("!@#$%^&*")
            number = str(random.randint(10, 99))
            upper_letter = random.choice(string.ascii_uppercase)
            password = chosen + special_char + number + upper_letter
            return password
        except Exception as e:
            print("Error:", e)
            return None


user_id = int(input("Enter ID: "))
name = input("Enter name: ")
obj = User(user_id, name)
final_password = obj.password_generate()

if final_password:
    print("\nUSER DETAILS")
    print(f"ID: {user_id}")
    print(f"Name: {name}")
    print(f"Generated Password: {final_password}")

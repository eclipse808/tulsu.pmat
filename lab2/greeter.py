#!/usr/bin/env python3
import sys

def is_valid_name(name):
	return name and name[0].isupper() and name.isalpha()

def greet_list(names_file, error_file):
    with open(names_file, 'r') as f:
        names = f.readlines()
        
    error_messages = []
    for name in names:
        name = name.strip()
        if not is_valid_name(name):
            error_messages.append(f"Ошибка: {name} - недопустимое имя.\n")
            continue
        print(f"Nice to see you, {name}!")
    
    if error_messages:
        with open(error_file, 'w') as f:
            f.writelines(error_messages)

def greet_user():
    try:
        while True:
            name = input("Hey, what's your name?\n")
            if is_valid_name(name):
                print(f"Nice to see you, {name}!")
            else:
                print("Недопустимое имя, попробуйте снова.")
    except KeyboardInterrupt:
        print("\nGoodbye!")

def main():
    if len(sys.argv) == 3:
        names_file = sys.argv[1]
        error_file = sys.argv[2]
        greet_list(names_file, error_file)
    else:
        greet_user()

if __name__ == "__main__":
    main()

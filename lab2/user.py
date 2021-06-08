from helpers.user import is_signed_in, sign_out, sign_in, sign_up
from helpers.message import create_message, get_inbox_messages
from helpers.redis import redis_connection

def start_menu() -> int:
    print("\nMAIN MENU", 15 * "-", ">")
    print("0. Exit.")
    print("1. Sign up.")
    print("2. Sign in.\n")
    return int(input("Enter the number of action: "))

def main():
    while True:
        action = start_menu()

        if action == 0:
            print("Goodbye, have a good day :)")
            break

        elif action == 1:
            username = input("Enter username: ")
            user_id = sign_up(username)
            if is_signed_in(user_id):
                user(user_id)

        elif action == 2:
            username = input("Enter username: ")
            user_id = sign_in(username)
            if is_signed_in(user_id):
                user(user_id)

        else:
            print("Choose only available [0-2] actions :)")

def user_menu() -> int:
    print("\nUSER MENU", 15 * "-", ">")
    print("0. Log out.")
    print("1. Inbox messages.")
    print("2. Send message.")
    print("3. Statistics.\n")
    return int(input("Enter the number of action: "))

def user(user_id):
    while True:
        action = user_menu()

        if action == 0:
            sign_out(user_id)
            break

        elif action == 1:
            get_inbox_messages(user_id)

        elif action == 2:
            message = input("Enter message: ")
            recipient = input("Enter username of the receiver: ")
            if create_message(user_id, message, recipient):
                print(f"Sent your message to {recipient}")

        elif action == 3:
            keys = ["in_queue", "checking", "blocked", "sent", "delivered"]
            user = redis_connection.hmget(f"user{user_id}", keys)
            for i in range(5):
                print(f"{keys[i]}: {user[i]}")

        else:
            print("Choose only available [0-3] actions :)")

if __name__ == '__main__':
    main()
from helpers.neo4 import neo4j

def neo4j_menu() -> int:
    print("\nNEO4J MENU", 15 * "-", ">")
    print("0. Exit.")
    print("1. List of tagged messages.")
    print("2. Relations.")
    print("3. Find the shortest way between two users.")
    print("4. Spam.")
    print("5. List of tagged messages without relations.\n")
    return int(input("Enter the number of action: "))

def main():
    while True:
        action = neo4j_menu()

        if action == 0:
            print("Goodbye, have a good day :)")
            break

        elif action == 1:
            tags = input("Enter tags separated by comma [family, private, work]: ")
            users_with_tagged_messages = neo4j.get_users_with_tagged_messages(tags)
            print(f"Users: ")
            iter = 1
            for user in users_with_tagged_messages:
                print(f"{iter}. {user}")
                iter += 1

        elif action == 2:
            n = int(input("Enter length of relations: "))
            users_with_n_relations = neo4j.get_users_with_n_long_relations(n)
            print(f"Users: ")
            iter = 1
            for user in users_with_n_relations:
                print(f"{iter}. {user}")
                iter += 1

        elif action == 3:
            username1 = input("Enter username of the first user: ")
            username2 = input("Enter username of the second user: ")
            way = neo4j.shortest_way_between_users(username1, username2)
            text = ""
            for step in way:
                text += f"{step} >> "
            print(text[:-3])

        elif action == 4:
            spammers = neo4j.get_users_which_have_only_spam_conversation()
            print(f"Users: ")
            iter = 1
            for user in spammers:
                print(f"{iter}. {user}")
                iter += 1

        elif action == 5:
            tags = input("Enter tags separated by comma [family, private, work]: ")
            unrelated_users = neo4j.get_unrelated_users_with_tagged_messages(tags)
            print(f"Users: ")
            iter = 1
            for user in unrelated_users:
                print(f"{iter}. {user}")
                iter += 1

        else:
            print("Choose only available [0-5] actions :)")
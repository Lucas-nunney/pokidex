import csv

def print_pokemon(username, password, userdata):
    for row in userdata:
        if row[0] == username and row[1] == password:
            pokemon = [p for p in row[2:] if p]  # Filter out empty strings
            print(f"{username}'s Pokemon: {', '.join(pokemon)}")
            return
    print("Username or password not found.")

def main():
    with open('userdata.csv', newline='') as csvfile:
        userdata = list(csv.reader(csvfile))
        username = 'a'
        password = 'a'
        print_pokemon(username, password, userdata)

if __name__ == "__main__":
    main()
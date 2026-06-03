watchlist = []
watched = []

def add():
    movie = input("Movie: ")
    watchlist.append(movie)
    print(f"Added {movie} to watchlist")

def seen():
    movie = input("Movie you watched: ")
    if movie in watchlist:
        watchlist.remove(movie)
        watched.append(movie)
        print(f"Moved {movie} to watched")
    else:
        print("That movie isnt in the watchlist yet.")

def show():
    for x, y in enumerate(watchlist):
        print(f"To watch: {1 + x} {y}")
    for x, y in enumerate(watched):
        print(f"Watched: {1 + x} {y}")
    

print("Movie Watchlist\n")

while True:
    command = input("Command (add/watched/show/quit): ")
    if command == "add":
        add()
    elif command == "watched":
        seen()
    elif command == "show":
        show()
    elif command == "quit":
        break
    else:
        print("Invalid output!")
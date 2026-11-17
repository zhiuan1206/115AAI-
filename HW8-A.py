
n = int(input())
songs = input().split()

q = int(input())

for i in range(q):
    command = input().split()

    if command[0] == "ADD":
        songs.append(command[1])

    elif command[0] == "REMOVE":
        if command[1] in songs:
            songs.remove(command[1])

    elif command[0] == "REVERSE":
        songs.reverse()

print(len(songs))

if len(songs) == 0:
    print("EMPTY")
else:
    print(" ".join(songs))

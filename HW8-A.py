
n = int(input())

# 讀取初始歌曲清單
if n > 0:
    songs = input().split()
else:
    songs = []

q = int(input())

# 依序執行指令
for _ in range(q):
    command = input().split()

    if command[0] == "ADD":
        songs.append(command[1])

    elif command[0] == "REMOVE":
        name = command[1]
        if name in songs:
            songs.remove(name)

    elif command[0] == "REVERSE":
        songs.reverse()

# 輸出最後的歌曲數量
print(len(songs))

# 輸出最後的播放清單
if len(songs) == 0:
    print("EMPTY")
else:
    print(" ".join(songs))

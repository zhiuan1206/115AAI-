S = int(input())

hours = S // 3600
rem_seconds = S % 3600
minutes = rem_seconds // 60
seconds = rem_seconds % 60

print(f"{hours} {minutes} {seconds}")
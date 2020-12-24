n = int(input())
cmds = [input().lower().split() for _ in range(n)]

x, y = 0, 0

for cmd in cmds:
    direction = cmd[0]
    movement = int(cmd[1])
    if direction == 'север':
        y += movement
    elif direction == 'юг':
        y -= movement
    elif direction == 'запад':
        x -= movement
    elif direction == 'восток':
        x += movement

print(x, y)
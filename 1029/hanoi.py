def move(disk, src, tar, tmp):
    if disk == 1: #원판이 1개라면
        print("Move disk :", disk, 'from', src, 'to', tar)
    else:
        move(disk-1, src, tmp, tar)
        print("Move disk :", disk, 'from', src, 'to', tar)
        move(disk-1, tmp, tar, src)
        print("Move disk :", disk, 'from', src, 'to', tar)

move(3, 'A','B','C')
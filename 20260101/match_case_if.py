for no in range(10, 21):
    match no:
        case _ if no % 3 == 0 and no % 5 == 0:
            print(f"{no}は3の倍数かつ5の倍数")
        case _ if no % 3 == 0:
            print(f"{no}は3の倍数")
        case _ if no % 5 == 0:
            print(f"{no}は5の倍数")

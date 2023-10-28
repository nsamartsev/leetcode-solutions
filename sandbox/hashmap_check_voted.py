def check_voted(name):
    if voted.get(name):
        print("Kick them out! Name:", name)
    else:
        voted[name] = True
        print("Let them vote. Name:", name)


voted = {}
check_voted("tom")
check_voted("mike")
check_voted("tom")

voted = {}


def check_voter(name):
    # 散列表投票 避免重复，同一姓名，投票两次
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


check_voter("tom")
check_voter("mike")
check_voter("mike")

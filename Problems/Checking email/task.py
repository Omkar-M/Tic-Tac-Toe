def check_email(string):
    test1 = " " in string
    test2 = "@" in string
    test3 = (string.rfind(".")) > (string.find("@"))
    test4 = "@." in string
    sum_ = test1 + test2 + test3 + test4
    # print(test1, test2, test3, test4)
    # print(sum_)
    return sum_ == 2

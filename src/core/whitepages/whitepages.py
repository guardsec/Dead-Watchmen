class info:
    def __init__(self):

        FN = input("First Name: ")
        LN = input("Last Name: ")
        CSA = input("City/State/Area code: ")

        print("https://www.whitepages.com/name/" + FN + "-" + LN + "/" + CSA + "?fs=1&l=" + CSA + "&q=" + FN + "+" + LN)





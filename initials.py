def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """

    initials = [name[0] for name in fullname.upper().split()]
    return ''.join(initials)

def main():
    nameFromUser = input("What is your full name?")
    answer = "The initials of '%s' are %s" % (nameFromUser, get_initials(nameFromUser))
    print(answer)

if __name__ == '__main__':
    main()
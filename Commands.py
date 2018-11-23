from TASchedulingApp import TASchedulingApp

app = TASchedulingApp()


class CommandHandler():

    def __init__(self):
        pass

    @staticmethod
    def command(args):
        if args[0] == "Login":
            if app.login(args[1], args[2]):
                return "Logged In"
            else:
                return "Could not login"
        elif args[0] == "CreateAccount":
            if app.createAccount(args[1], args[2], int(args[3])):
                return "Created New Account"
            else:
                return "Could Not Create New Account"
        else:
            return "Error"

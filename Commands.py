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
            return "Error"

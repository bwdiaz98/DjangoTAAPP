from TASchedulingApp import TASchedulingApp
from DjangoTAApp.models import User, Courses, Labs

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
        elif args[0] == "Logout":
            if app.logout():
                return "Logged Out"
            else:
                return "Could Not Logout"
        elif args[0] == "CreateAccount":
            if app.createAccount(args[1], args[2], int(args[3])):
                return "Created New Account"
            else:
                return "Could Not Create New Account"
        elif args[0] == "EditAccount":
            if app.editAccount(args[1], args[2], args[3], int(args[4])):
                return "Edited Account"
            else:
                return "Could Not Edit Account"
        elif args[0] == "CreateCourse":
            if app.createCourse(args[1], args[2], args[3]):
                return "Created New Course"
            else:
                return "Could Not Create New Course"
        elif args[0] == "CreateLab":
            if app.createLab(int(args[1]), int(args[2]), args[3]):
                return "Created New Lab"
            else:
                return "Could Not Create New Lab"
        elif args[0] == "DeleteAccount":
            if app.deleteAccount(args[1]):
                return "Deleted Account"
            else:
                return "Could Not Delete Account"
        elif args[0] == "DisplayAccounts":
            users = list(User.objects.all())
            out = ""
            for user in users:
                out += "(" + user.username + ", " + user.password + ", " + str(user.clearance) + ")"
            return out
        elif args[0] == "DisplayCourses":
            courses = list(Courses.objects.all())
            out = ""
            for course in courses:
                out += "(" + str(course.courseID) + ", " + course.coursename + ", " + course.professor + ")"
            return out
        elif args[0] == "DisplayLabs":
            labs = list(Labs.objects.all())
            out = ""
            for lab in labs:
                out += "(" + str(lab.LabID) + ", " + str(lab.courseID) + ", " + lab.tausername + ")"
            return out
        else:
            return "Error"

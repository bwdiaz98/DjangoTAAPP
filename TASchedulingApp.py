from User import User
from Course import Course
from DjangoTAApp.models import User, Courses, Labs

class TASchedulingApp:
    LoggedInUser = None
    def __init__(self):
        self.LoggedInUser = None

    def login(self, sUsername, sPassword):
        users = list(User.objects.filter(username=sUsername))
        for user in users:
            if user.password == sPassword:
                self.LoggedInUser = User(sUsername, sPassword, user.clearance)
                return True
        return False

    def logout(self):
        self.LoggedInUser = None
        return True

    def createAccount(self,sUsername,sPassword,iClearance):

        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3 and "," not in sUsername and "," not in sPassword and isinstance(iClearance, int):
            users = list(User.objects.filter(username=sUsername))
            if len(users) > 0:
                return False
            else:
                user = User(username=sUsername, password=sPassword, clearance=iClearance)
                user.save()
                return True

    def editAccount(self, sUsername, sNewUsername, sPassword, iClearance):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            users = list(User.objects.filter(username=sUsername))
            if len(users) == 1:
                User.objects.filter(username=sUsername).delete()
                u1 = User(username=sNewUsername, password=sPassword, clearance=iClearance)
                u1.save()
                return True
            else:
                return False
        else:
            return False

    def createCourse(self, uniqId, coursename, professor):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 2:
            courses = list(Courses.objects.filter(courseID=uniqId))
            if len(courses) > 0:
                return False
            else:
                course = Courses(courseID=uniqId, coursename=coursename, professor=professor)
                course.save()
                return True
        else:
            return False

    def createLab(self, iLabID, iCourseId, sTA):
        if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
            labs = list(Labs.objects.filter(LabID=iLabID))
            if len(labs) > 0:
                return False
            else:
                lab = Labs(LabID=iLabID, courseID=iCourseId, tausername=sTA)
                lab.save()
                return True
        else:
            return False


    def deleteAccount(self, sUsername):
        if len(list(User.objects.filter(username=sUsername))) > 0:
            User.objects.filter(username=sUsername).delete()
            return True
        else:
            return False


from User import User
from Course import Course
from DjangoTAApp.models import User,Courses,Labs

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

  def createAccount(self,sUsername,sPassword,iClearance):

    if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3 and "," not in sUsername and "," not in sPassword and isinstance(iClearance, int):
        users = list(User.objects.filter(username=sUsername))
        if len(users) > 0:
            return False
        else:
            user = User(username=sUsername, password=sPassword, clearance=iClearance)
            user.save()
            return True
      
  def editAccount(self, tUsername, nUsername, nPassword, nClearance):
    if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3:
        file_object = open("Accounts.txt", "r+")
        lines = file_object.readlines()
        file_object.seek(0)
        for i in lines:
            if tUsername not in i:
                file_object.write(i)
            else:
                file_object.write(nUsername + "," + nPassword + "," + nClearance + "\n")
        file_object.truncate()
        file_object.close()
        print("Edited Account")
    else:
        print("Invalid command or insufficient access")

  def createCourses(self, uniqId, courseNumber, Professor):
    if self.LoggedInUser is not None and self.LoggedInUser.clearance < 2:
      course = Course(uniqId, courseNumber, Professor)
      file_object = open("Courses.txt", "a")
      file_object.write(uniqId + "," + courseNumber + "," + Professor + "\n")
      file_object.close()
      print("Created Course")
      return True
    else:
      print("Invalid command")
      return False

  def createLab(self,sTA,icourse,ilab):
    
    if self.LoggedInUser is not None and self.LoggedInUser.clearance < 3 :

      file_object = open("Labs.txt","a")
      file_object.write(ilab + "," + icourse + "," + sTA + "\n")
      file_object.close()
      print("Lab Created")

    else:

      print("Invalid command")

      
  def deleteAccount(self, sUsername):
    
    file_object = open("Accounts.txt", "r")
    usernames = file_object.readlines()
    file_object.close()
    file_object = open("Accounts.txt", "w")
    deleted = False
    for line in usernames:
      user = line.split(",")
      if(user[0]!=sUsername):
        file_object.write(line)
      else:
        deleted = True
    if(deleted == False):
        print("No account " + sUsername + " found")
        return "No account " + sUsername + " found"
    else:
        print("account " + sUsername + " deleted")
        return "account " + sUsername + " deleted"

class InvalidInput(Exception):
  def __init__(self,message):
    self.message = message


class Schl_mana_sys:

  @staticmethod
  def add_student():
    name= input()
    roll_num = input()
    marks = input()
    std_data =  f"{name},{roll_num},{marks}\n"
    with open("students.txt", "a") as f:
      f.write(std_data)

  @staticmethod
  def view_students():
    with open("students.txt","r") as f:
      print(f.read())

  @staticmethod
  def search_student():
      search_roll = input("Enter Student Roll Number:")
      found = False
      with open("students.txt", "r") as f:
        for line in f:
          if search_roll in line:
            print(line)
            found= True
            break;
      if not found:
        print("Student not found")


choice = int(input("Choose your option:\n1.Add student\n2.View Students\n3.Search student\n\n Enter 1,2 or 3 to choose your option\n"))
sms =  Schl_mana_sys()
try:
  if choice==1:
    sms.add_student()
  elif choice ==2:
    sms.view_students()
  elif choice ==3:
    sms.search_student()
  else:
    raise InvalidInput("Please check your input and start again the program.")
except InvalidInput as II:
  print("InvalidInput:",II.message)

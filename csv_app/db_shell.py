
import random
import string

from csv_app.models import Emplayees

# exec(open('myscript.py').read())
# exec(open(r"C:\Users\Lenovo\Desktop\aniket\b6\Django\Csv\csv_app\db_shell.py").read())

des = ["Software Engineer" , "Sr. Software Engineer" , "Linux Administrator" , "Associate" , "CEO" , "Python Developer" , "Data Scientist"]

for emps in range(50):
    letter = string.ascii_lowercase
    emp_name = "".join(random.choice(letter) for i in range(10))

    letter = string.digits
    sal = "".join(random.choice(letter) for i in range(5))

    letter = string.ascii_uppercase
    comp_name = "".join(random.choice(letter) for i in range(10))


    design = random.choice(des)
    emp = Emplayees(name= emp_name , salary= sal , company= comp_name , designation= design)
    emp.save()


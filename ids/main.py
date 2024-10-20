#   Main file for project.
#   Authors: Eduardo de la Rosa
#            Ernesto
#            Cristián León
from faker import Faker

fake = Faker()

from students import Student

alumno = Student()

alumno.random_setter()
alumno.set_registration(123456)
alumno.print_to_file("random.txt")




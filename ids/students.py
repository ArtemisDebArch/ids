# Primero se importan las librerias faker y openpyxl#
from faker import Faker

from openpyxl import Workbook

# Se define el alias de Faker como fake#

fake = Faker()

# Se crea una clase 'Student' para trabajar con el concepto de un estudiante#


class Student:
    def __init__(self):
        self.name = ""
        self.registration = ""
        self.email = ""

# Función para definir su formato como str#
    def __str__(self) -> str:
        return f'{self.name}\n{self.registration}\n{self.email}\n'

# Se usa la libreria Faker para crear todos los atributos random
    def random_setter(self):
        self.name = fake.name()
        self.registration = fake.random_number(digits=6, fix_len=True)
        self.email = fake.email()

#   Setters para los atributos del alumno
    def set_name(self, name: str):
        self.name = name

    def set_registration(self, registration: int):
        if registration > 99999 & registration < 999999:    # This ensures the registration is a 6-digit + value
            self.registration = registration
        else:
            raise ValueError("A 6-digit positive value was expected")   # Error Message if value is not the one expected

    def set_email(self, email: str):
        self.email = email

    def set_all(self, name: str, reg: int, email: str):
        self.set_name(name)
        self.set_registration(reg)
        self.set_email(email)

# Funcion para imprimir los datos a un archivo
    def print_to_file(self, filename: str):  # Se pide como parametro el nombre del archivo
        file = open(filename, "a")   # Se abre el archivo en "append"
        file.write(self.__str__())  # Se imprime el método para imprimir la clase en el archivo
        file.close()

# Se definen propiedades para devolver los valores de los elementos de la clase
    @property
    def _name(self):
        return self.name

    def _email(self):
        return self.email

    def _registration(self):
        return self.registration

    def _name_length(self):
        return len(self.name)












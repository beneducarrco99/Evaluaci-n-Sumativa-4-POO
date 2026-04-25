from datetime import datetime

class Persona:
    def __init__(self, rut, nombre, apellidoP, apellidoM):
        self._rut = rut
        self._nombre = nombre
        self._apellidoP = apellidoP
        self._apellidoM = apellidoM
        self._fechaNac = datetime.now()

class Docente (Persona):
    def __init__(self, rut, nombre, apellidoP, apellidoM, asignatura):
        super().__init__(rut, nombre, apellidoP, apellidoM)
        self.__asignatura = asignatura

class Estudiante (Persona):
    def __init__(self, rut, nombre, apellidoP, apellidoM, carrera):
        super().__init__(rut, nombre, apellidoP, apellidoM)
        self.__carrera = carrera
        self.__regular = False
        self.__beneficio = False

class Curso:
    def __init__(self, departamento, profJefe, duracion, periodo, cantidadMatri):
        self.__departamento = departamento
        self.__profJefe = profJefe
        self.__duracion = duracion
        self.__posgrado = False
        self.__periodo = periodo
        self.__cantidadMatri = cantidadMatri

class Asignatura:
    def __init__(self, semestre, departamentoAsig, profesor):
        self.__semestre = semestre
        self.__departamentoAsig = departamentoAsig
        self.__profesor = profesor

class Arancel:
    def __init__(self, anio, valor, cuota):
        self.__anio = anio
        self.__valor = valor
        self.__cuota = cuota

class Beca:
    def __init__(self, nombreBec, cantFinan):
        self.__nombreBec = nombreBec
        self.__cantFinan = cantFinan
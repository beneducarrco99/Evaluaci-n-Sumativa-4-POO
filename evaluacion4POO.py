from datetime import datetime

class Persona:
    def __init__(self, rut, nombre, apellidoP, apellidoM):
        self._rut = rut
        self._nombre = nombre
        self._apellidoP = apellidoP
        self._apellidoM = apellidoM
        self._fechaNac = datetime.now()

    def logearUsuario(self):
        print("------ Iniciar sesión ------")
        self._rut = str(input("Ingrese RUT: "))
        self._nombre = str(input("Ingrese Nombre: "))


class Docente (Persona):
    def __init__(self, rut, nombre, apellidoP, apellidoM, asignatura):
        super().__init__(rut, nombre, apellidoP, apellidoM)
        self.__asignatura = asignatura
        self.__nota = 0
        self.__notasSemestre = 0
        self.__contador = 0

    def logearUsuario(self):
        print("°°°    Sección Docente   °°°")
        print("------ Iniciar sesión ------")
        self._rut = str(input("Ingrese RUT: "))
        self._nombre = str(input("Ingrese Nombre: "))
        print(f"Bienvenido profesor/a {self._nombre}")
        self.adjuntarMaterial()

    def adjuntarMaterial(self):
        self.__notasSemestre = int(input("Antes de comenzar actividades. ¿Cuántas notas ingresará este semestre? "))
        self.registrarCalificacion()

    def registrarCalificacion(self):
        while self.__contador < self.__notasSemestre:
            self.__nota = int(input("Ingrese nota: "))
            
            if not (1 <= self.__nota <= 7):
                print("La nota ingresada no es válida.")
                return
            
            self.__contador += 1
            self.__asignatura.almacenaNotas(self.__nota)
        
        print("Ya ingresó el número máximo de notas en este semestre.")


class Estudiante (Persona):
    def __init__(self, rut, nombre, apellidoP, apellidoM, carrera):
        super().__init__(rut, nombre, apellidoP, apellidoM)
        self.__carrera = carrera
        self.__regular = False
        self.__beneficio = False
        self.__inscribe = ""

    def logearUsuario(self):
        print("°°°    Sección Alumno   °°°")
        print("------ Iniciar sesión ------")
        self._rut = str(input("Ingrese RUT: "))
        self._nombre = str(input("Ingrese Nombre: "))
        print(f"Bienvenido alumno/a {self._nombre}")
        self.inscribirCurso()

    def inscribirCurso(self):
        self.__inscribe = str(input("Inscriba una carrera: "))
        self.__carrera.sumarMatri(self.__inscribe)


class Curso:
    def __init__(self, departamento, profJefe, duracion, periodo, cantidadMatri):
        self.__departamento = departamento
        self.__profJefe = profJefe
        self.__duracion = duracion
        self.__posgrado = False
        self.__periodo = periodo
        self.__cantidadMatri = cantidadMatri
        self.__nroMatri = 0

    def sumarMatri(self, cantidadMatri):
        self.__cantidadMatri = cantidadMatri
        self.__nroMatri += 1

        print(f"Para la carrera de {self.__cantidadMatri} hay un total de {self.__nroMatri} alumnos inscritos")


class Asignatura:
    def __init__(self, semestre, departamentoAsig, profesor, nota, notasSemestre):
        self.__semestre = semestre
        self.__departamentoAsig = departamentoAsig
        self.__profesor = profesor
        self.__nota = nota
        self.__notasSemestre = notasSemestre
        self.__promedio = 0
        self.__cantidadNotas = 0

    def almacenaNotas(self, nota):
        if (self.__cantidadNotas < self.__notasSemestre):
            self.__nota += nota
            self.__cantidadNotas = self.__cantidadNotas + 1
            self.__promedio = self.__nota / self.__cantidadNotas
    
    def promedioNotas(self):
        print(f"{self.__promedio}")

        if (self.__promedio >= 4):
            print(f"El alumno/a aprobó la asignatura con promedio {self.__promedio}")
        else:
            print(f"El alumno/a reprobó la asignatura con promedio {self.__promedio}")


class Arancel:
    def __init__(self, anio, valor, cuota):
        self.__anio = anio
        self.__valor = valor
        self.__cuota = cuota


class Beca:
    def __init__(self, nombreBec, cantFinan):
        self.__nombreBec = nombreBec
        self.__cantFinan = cantFinan


curso = Curso("", "", 0, "", "")
novato = Estudiante("", "", "", "", curso)
novato.logearUsuario()
ramo = Asignatura("", "", "", 0, 0)
profe = Docente("", "", "", "", ramo)
profe.logearUsuario()
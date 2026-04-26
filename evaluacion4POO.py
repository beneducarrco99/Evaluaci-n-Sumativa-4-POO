from datetime import datetime

# --------------------------------------------------------------------------------------------------------------------------

class Persona:
    def __init__(self, rut, nombre, apellidoP, apellidoM):
        self._rut = rut
        self._nombre = nombre
        self._apellidoP = apellidoP
        self._apellidoM = apellidoM
        self._fechaNac = datetime.now()


    def logearUsuario(self):                                                 # Logeo Default
        print("------ Iniciar sesión ------")
        self._rut = str(input("Ingrese RUT: "))
        self._nombre = str(input("Ingrese Nombre: "))


    def verCalificacion(self):
        pass


    def mensajear(self):
        pass

# --------------------------------------------------------------------------------------------------------------------------

class Docente (Persona):
    def __init__(self, rut, nombre, apellidoP, apellidoM, asignatura):
        super().__init__(rut, nombre, apellidoP, apellidoM)
        self.__asignatura = asignatura
        self.__nota = 0
        self.__notasSemestre = 0
        self.__contador = 0


    def logearUsuario(self):                                                 # Logeo Docente
        print("--------------------------------------------------------------------------------------------------------------")
        print("°°°    Sección Docente   °°°")
        print("------ Iniciar sesión ------")
        self._rut = str(input("Ingrese RUT: "))
        self._nombre = str(input("Ingrese Nombre: "))
        print(f"Bienvenido profesor/a {self._nombre}")
        self.adjuntarMaterial()


    def adjuntarMaterial(self):   # Acá Docente inicia la asignatura del semeste. Puede estipular la cantidad de evaluaciones por ejemplo.
        print("--------------------------------------------------------------------------------------------------------------")
        self.__notasSemestre = int(input("Antes de comenzar actividades. ¿Cuántas notas ingresará este semestre? "))
        self.registrarCalificacion()


    def registrarCalificacion(self):   # Acá Docente ingresará las notas de los Estudiantes.
        print("--------------------------------------------------------------------------------------------------------------")
        while self.__contador < self.__notasSemestre:
            self.__nota = int(input("Ingrese nota: "))
            
            if not (1 <= self.__nota <= 7):
                print("La nota ingresada no es válida.")
                return
            
            self.__contador += 1
            self.__asignatura.compartirInfo(self.__nota, self.__notasSemestre) # Llamamos a la instancia de Asignatura y a su método de información
        print("Ya ingresó el número máximo de notas en este semestre.")
        
        self.__asignatura.promedioNotas()   # Llamamos a la instancia de Asignatura y a su método de promedio

# --------------------------------------------------------------------------------------------------------------------------

class Estudiante (Persona):
    def __init__(self, rut, nombre, apellidoP, apellidoM, carrera):
        super().__init__(rut, nombre, apellidoP, apellidoM)
        self.__carrera = carrera
        self.__regular = False
        self.__beneficio = False
        self.__inscribe = ""


    def logearUsuario(self):                                                 # Logeo Estudiante
        print("--------------------------------------------------------------------------------------------------------------")
        print("°°°    Sección Alumno   °°°")
        print("------ Iniciar sesión ------")
        self._rut = str(input("Ingrese RUT: "))
        self._nombre = str(input("Ingrese Nombre: "))
        print("--------------------------------------------------------------------------------------------------------------")
        print(f"Bienvenido alumno/a {self._nombre}")
        self.inscribirCurso()


    def inscribirCurso(self):   # Acá Estudiante inscribe un curso/carrera. Prototipo inicial con margen de mejora.
        self.__inscribe = str(input("Inscriba una carrera: "))
        self.__carrera.sumarMatri(self.__inscribe) # Llamamos a la instancia de Curso y a su método de matriculados.


    def visualizarMaterial(self):
        pass


    def desarrollarEvaluacion(self):
        pass


    def adjuntarEvaluacion(self):
        pass


    def solicitarBeneficio(self):
        pass

# --------------------------------------------------------------------------------------------------------------------------

class Curso:
    def __init__(self, departamento, profJefe, duracion, periodo, cantidadMatri):
        self.__departamento = departamento
        self.__profJefe = profJefe
        self.__duracion = duracion
        self.__posgrado = False
        self.__periodo = periodo
        self.__cantidadMatri = cantidadMatri
        self.__nroMatri = 0


    def asignarJefeCarr(self):
        pass
    
    
    def registrarPeriodo(self):
        pass


    def sumarMatri(self, cantidadMatri): # Registra carrera y suma matriculados. Prototipo inicial con margen de mejora.
        self.__cantidadMatri = cantidadMatri
        self.__nroMatri += 1

        print("--------------------------------------------------------------------------------------------------------------")
        print(f"Para la carrera de {self.__cantidadMatri} hay un total de {self.__nroMatri} alumnos inscritos")

# --------------------------------------------------------------------------------------------------------------------------

class Asignatura:
    def __init__(self, semestre, departamentoAsig, profesor, nota, notasSemestre):
        self.__semestre = semestre
        self.__departamentoAsig = departamentoAsig
        self.__profesor = profesor
        self.__nota = nota
        self.__notasSemestre = notasSemestre
        self.__promedio = 0
        self.__cantidadNotas = 0


    def asignarProfe(self):
        pass
    
    
    def compartirInfo(self, nota, notasSemestre):   # Prototipo inicial con margen de mejora de la información semestral de la asignatura, de momento solo gestiona notas.
        self.__notasSemestre = notasSemestre 
        self.__nota += nota
        self.__cantidadNotas = self.__cantidadNotas + 1
        self.__promedio = self.__nota / self.__cantidadNotas
    

    def promedioNotas(self):   # Muestra promedio de nota para el Estudiante
        print("--------------------------------------------------------------------------------------------------------------")
        print(f"{self.__promedio}")

        if (self.__promedio >= 4):
            print(f"El alumno/a aprobó la asignatura con promedio {self.__promedio}")
        else:
            print(f"El alumno/a reprobó la asignatura con promedio {self.__promedio}")
        
        print("--------------------------------------------------------------------------------------------------------------")

# --------------------------------------------------------------------------------------------------------------------------

class Arancel:
    def __init__(self, anio, valor, cuota):
        self.__anio = anio
        self.__valor = valor
        self.__cuota = cuota


    def calcularValorCuota(self):
        pass


    def mostrarCuota(self):
        pass

# --------------------------------------------------------------------------------------------------------------------------

class Beca:
    def __init__(self, nombreBec, cantFinan):
        self.__nombreBec = nombreBec
        self.__cantFinan = cantFinan


    def calcularRequisitos(self):
        pass

# --------------------------------------------------------------------------------------------------------------------------

curso = Curso("", "", 0, "", "")
novato = Estudiante("", "", "", "", curso)
novato.logearUsuario()
ramo = Asignatura(0, "", "", 0, 0)
profe = Docente("", "", "", "", ramo)
profe.logearUsuario()
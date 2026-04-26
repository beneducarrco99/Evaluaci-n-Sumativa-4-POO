Le doy la bienvenida a la tarea nro 4 y final de la asignatura Desarrollo Orientado a Objeto.
Benjammín Carrasco Concha.   20.022.665-8   23/04/2026

En esta sección, encontrará el prototipo inicial de un sistema computacional diseñado y desarrollado para universidades y sus procesos académicos y administrativos.

Diagrama de clases:

1. El desarrollo del diagrama comenzó definiendo las clases usuarios: clase Docente y clase Estudiante. Para optimizar la contaminación de atributos y métodos, creé una superclase llamada "Persona" que tomarará los datos compartidos entre ambos usuarios. También, definí sus relaciones de herencia, las relaciones están declaradas al final del código del diagrama.

2. Seguimos con la definición de las clases "Curso" y "Asignatura" para continuar con sus relaciones y aprovechamos de enlazar relaciones con las clases usuarios. Un Docente puede impartir más de una asignatura y puede enseñar en más de un curso, así como una asignatura, dependiendo del curso y período, puede ser impartida por más de un Docente.

3. Por último, definimos dos clases administrativas iniciales: clase Arancel y clase Beca. Pulimos y creamos las últimas relaciones y métodos.

Estructura código:

- El código es la primera versión del sistema y se experimenta con algunas funciones básicas e iniciales.
- Todas las clases están declaradas en el programa.
- Hay herencia entre la superclase Persona y sus subclases Docente y Estudiante.
- En la familia de clases que heredan, hay polimorfismo en el método logearUsuario().
- El encapsulamiento está diseñado a las necesidades que requiere cada clase.
- La separación entre clases está bien señalizada.
- Hay comentarios en las partes más complejas del código para guiar a los demás desarrolladores.

Instrucciones de ejecución:

1. Primero iniciarás sesión como estudiante e inscribirás un curso.
2. Luego, iniciarás sesión como docente y decidirás cuantas notas ingresarás.
3. Aún como docente, probarás el ingreso de notas y te retornará el promedio junto con el mensaje de aprobación o reprobación.

Tecnologías usadas:

- Visual Studio Code
- PlantUML en VS Code
- Lenguaje Python
- Controlador de versiones GIT
----------------------------------------------------------------------------------------------------------------------------------
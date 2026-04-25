Le doy la bienvenida a la tarea nro 4 y final de la asignatura Desarrollo Orientado a Objeto.
Benjammín Carrasco Concha.   20.022.665-8   23/04/2026

En esta sección, encontrará el prototipo inicial de un sistema computacional diseñado y desarrollado para universidades y sus procesos académicos y administrativos.

Diagrama de clases.

1. El desarrollo del diagrama comenzó definiendo las clases usuarios: clase Docente y clase Estudiante. Para optimizar la contaminación de atributos y métodos, creé una superclase llamada "Persona" que tomarará los datos compartidos entre ambos usuarios. También, definí sus relaciones de herencia, las relaciones están declaradas al final del código del diagrama.

2. Seguimos con la definición de las clases "Curso" y "Asignatura" para continuar con sus relaciones y aprovechamos de enlazar relaciones con las clases usuarios. Un Docente puede impartir más de una asignatura y puede enseñar en más de un curso, así como una asignatura, dependiendo del curso y período, puede ser impartida por más de un Docente.

3. Por último, definimos dos clases administrativas iniciales: clase Arancel y clase Beca. Pulimos y creamos las últimas relaciones y métodos.
# Actividad 2 - Programación en Python utilizando clases, atributos y métodos

## 📚 Información académica

- **Universidad:** Universidad Nacional de Colombia
- **Actividad:** Actividad 2 - Programación en Python utilizando clases, atributos y métodos
- **Estudiante:** Mateo Agudelo Chica
- **Docente:** Walter Hugo Arboleda Mazo
- **Asignatura:** Programación Orientada a Objetos
- **Semestre:** 2026-2S

---

## 📝 Ejercicios

| # | Descripción |
|---|-------------|
| **Ejercicio 2.1** | Modelar el concepto de una persona con sus datos básicos. |
| **Ejercicio 2.2** | Modelar el concepto de un planeta del sistema solar y calcular su densidad. |
| **Ejercicio 2.3** | Modelar el concepto de un automóvil con simulación de cambios de velocidad. |
| **Ejercicio 2.4** | Modelar figuras geométricas: círculo, rectángulo, cuadrado y triángulo rectángulo. |
| **Ejercicio 2.5** | Modelar una cuenta bancaria con funciones para consignar y retirar saldo. |


```mermaid
classDiagram
    class Persona {
        - nombre: str
        - apellido: str
        - numero_documento: str
        - anio_nacimiento: int
        + __init__(nombre: str, apellido: str, numero_documento: str, anio_nacimiento: int)
        + imprimir() void
    }

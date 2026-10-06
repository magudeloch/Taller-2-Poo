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
%%{init: {'theme': 'default'}}%%
classDiagram
    class TipoCombustible {
        <<Enumeration>>
        GASOLINA
        BIOETANOL
        DIESEL
        BIODIESEL
        GAS_NATURAL
    }
    
    class TipoAutomovil {
        <<Enumeration>>
        CARRO_CIUDAD
        SUBCOMPACTO
        COMPACTO
        FAMILIAR
        EJECUTIVO
        SUV
    }
    
    class Color {
        <<Enumeration>>
        BLANCO
        NEGRO
        ROJO
        NARANJA
        AMARILLO
        VERDE
        AZUL
        VIOLETA
    }

    class Automovil {
        - marca: str
        - modelo: int
        - motor: float
        - tipo_combustible: TipoCombustible
        - tipo_automovil: TipoAutomovil
        - numero_puertas: int
        - cantidad_asientos: int
        - velocidad_maxima: float
        - color: Color
        - velocidad_actual: float
        + __init__(marca, modelo, motor, tipo_combustible, tipo_automovil, numero_puertas, cantidad_asientos, velocidad_maxima, color, velocidad_actual)
        + get_marca() str
        + set_marca(marca: str) void
        + get_modelo() int
        + set_modelo(modelo: int) void
        + get_motor() float
        + set_motor(motor: float) void
        + get_tipo_combustible() TipoCombustible
        + set_tipo_combustible(tipo_combustible: TipoCombustible) void
        + get_tipo_automovil() TipoAutomovil
        + set_tipo_automovil(tipo_automovil: TipoAutomovil) void
        + get_numero_puertas() int
        + set_numero_puertas(numero_puertas: int) void
        + get_cantidad_asientos() int
        + set_cantidad_asientos(cantidad_asientos: int) void
        + get_velocidad_maxima() float
        + set_velocidad_maxima(velocidad_maxima: float) void
        + get_color() Color
        + set_color(color: Color) void
        + get_velocidad_actual() float
        + set_velocidad_actual(velocidad_actual: float) void
        + acelerar(incremento: float) void
        + desacelerar(decremento: float) void
        + frenar() void
        + calcular_tiempo_llegada(distancia_km: float) float
        + mostrar_atributos() void
    }
    
    Automovil --> TipoCombustible
    Automovil --> TipoAutomovil
    Automovil --> Color

# =========================
# archivo: herencia_persona_alumno.py
# =========================

class Persona:
    def __init__(self, nombre, direccion):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        self.nombre = nombre
        self.direccion = direccion

    def presentarse(self):
        return f"Me llamo {self.nombre} y vivo en {self.direccion}"


class Alumno(Persona):
    def __init__(self, nombre, direccion, matricula):
        # Llamada al constructor de la clase padre
        super().__init__(nombre, direccion)

        self.matricula = matricula

    def presentarse(self):
        # Uso de un método del padre con super()
        return f"{super().presentarse()} y soy alumno (matrícula {self.matricula})"


# =========================
# Pruebas
# =========================
if __name__ == "__main__":
    persona = Persona("Luis", "Calle Mayor 3")
    alumno = Alumno("Ana", "Calle Sol 5", "A123")

    print(persona.presentarse())
    print(alumno.presentarse())

    print("\nAtributos heredados:")
    print(alumno.nombre)
    print(alumno.direccion)
    print(alumno.matricula)

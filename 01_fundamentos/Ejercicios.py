class Equipo:

    # Constructor
    def __init__(self, nombre, ciudad, puntos_liga):
        self.nombre = nombre
        self.ciudad = ciudad
        self._puntos_liga = puntos_liga

    # Getter
    @property
    def puntos_liga(self):
        return self._puntos_liga

    # Setter
    @puntos_liga.setter
    def puntos_liga(self, valor):
        self._puntos_liga = valor

    # Método 1
    def ganar_partido(self):
        self._puntos_liga += 3
        print(f"{self.nombre} ganó. Puntos: {self._puntos_liga}")

    # Método 2
    def perder_partido(self):
        print(f"{self.nombre} perdió el partido.")

    # Método 3
    def mostrar_puntos(self):
        print(f"{self.nombre} tiene {self._puntos_liga} puntos en la temporada.")

    # toString
    def __str__(self):
        return f"{self.nombre} - {self.ciudad} - {self._puntos_liga} pts"


# Instanciar objetos
real_madrid = Equipo("Real Madrid", "Madrid", 100)
barcelona = Equipo("Barcelona", "Barcelona", 90)

# Usar métodos
real_madrid.ganar_partido()
real_madrid.perder_partido()
real_madrid.mostrar_puntos()

barcelona.ganar_partido()
barcelona.perder_partido()
barcelona.mostrar_puntos()

# Usar setter y getter
barcelona.puntos_liga = 70
print(f"Puntos actualizados del Barcelona: {barcelona.puntos_liga}")

# Usar toString
print(real_madrid)
print(barcelona)
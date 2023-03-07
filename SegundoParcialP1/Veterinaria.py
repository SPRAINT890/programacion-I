from exception.InformacionInvalida import InformacionInvalida
from exception.EntidadYaExiste import EntidadYaExiste

from entities.Animal import Animal
from entities.Doctor import Doctor
from entities.Gato import Gato
from entities.Perro import Perro
from entities.Vacuna import Vacuna

class Veterinaria:
    def __init__(self) -> None:
        self._doctores = []
        self._vacunas = []
        self._animales = []
    
    @property
    def doctores(self):
        return self._doctores
    
    @doctores.setter
    def doctores(self, doctores):
        self._doctores = doctores
    
    @property
    def vacunas(self):
        return self._vacunas
    
    @vacunas.setter
    def vacunas(self, vacunas):
        self._vacunas = vacunas
    
    @property
    def animales(self):
        return self._animales
    
    @animales.setter
    def animales(self, animales):
        self._animales = animales
    
    def encontrar_doctor(self, nombre_doctor):
        doctor = None
        for doctor_veterinaria in self._doctores:
            if doctor_veterinaria.nombre_completo == nombre_doctor:
                doctor = doctor_veterinaria
        return doctor
    
    def encontrar_gato(self, nombre_animal, colores):
        gato = None
        for gato_veterinaria in self._animales:
            if isinstance(gato_veterinaria, Gato):
                if gato_veterinaria.nombre == nombre_animal and gato_veterinaria.colores == colores:
                    gato = gato_veterinaria
        return gato
    
    def encontrar_perro(self, nombre_animal, raza):
        perro = None
        for perro_veterinaria in self._animales:
            if isinstance(perro_veterinaria, Perro):
                if perro_veterinaria.nombre == nombre_animal and perro_veterinaria.raza == raza:
                    perro = perro_veterinaria
        return perro
    
    def ya_existe_este_identificador(self, identificador):
        ret = False
        for vacuna_veterinaria in self._vacunas:
            if vacuna_veterinaria.identificador == identificador:
                ret = True
        return ret
    
    def registrar_animal_con_vacuna (self, nombre_animal, raza, colores, identificador,  fecha,  nombre_doctor,  edad_doctor):
        if nombre_animal is None or raza is None and colores is None or identificador is None or fecha is None or nombre_doctor is None or edad_doctor is None:
            raise InformacionInvalida("Algun dato es invalido")
        # compruebo que exista el doctor
        doctor_obj = self.encontrar_doctor(nombre_doctor)
        
        # creo el doctor si no esta registrado
        if doctor_obj is None:
            self._doctores.append(Doctor(nombre_doctor, edad_doctor, 0.0))
            doctor_obj = self.encontrar_doctor(nombre_doctor)
        
        # doctor_obj tiene el objeto
        
        vacuna_obj = Vacuna(identificador, fecha, False, doctor_obj)
        
        
        if self.ya_existe_este_identificador(identificador):
            raise EntidadYaExiste("Identificador duplicado")
        self._vacunas.append(vacuna_obj)
        if raza is None:
            animal_obj = self.encontrar_gato(nombre_animal, colores)
        else:
            animal_obj = self.encontrar_perro(nombre_animal, raza)
        
        if animal_obj is None:
            if colores is None:
                animal_obj = Perro(nombre_animal, True, raza)
            else:
                animal_obj = Gato(nombre_animal, True, colores)
            animal_obj.vacunas.append(vacuna_obj)
            self._animales.append(animal_obj)
        else:
            animal_obj.vacunas.append(vacuna_obj)
    
    def validar_vacunas_y_efectos_secundarios (self, raza, color, fecha_inicial, fecha_final):
        identificadores = []
        for perro in self._animales:
            if isinstance(perro, Perro):
                if perro.raza == raza:
                    if len(perro.vacunas) >= 3:
                        perro.esta_vacunado = True
                    else:
                        perro.esta_vacunado = False
                    for vacuna_perro in perro.vacunas:
                        if fecha_inicial < vacuna_perro.fecha and vacuna_perro.fecha < fecha_final:
                            vacuna_perro.efectos_secundarios = True
                            identificadores.append(vacuna_perro.identificador)
        for gato in self._animales:
            if isinstance(gato, Gato):
                if color in gato.colores:
                    if len(gato.vacunas) >= 2:
                        gato.esta_vacunado = True
                    else:
                        gato.esta_vacunado = False
                    for vacuna_gato in gato.vacunas:
                        if fecha_inicial < vacuna_gato.fecha and vacuna_gato.fecha < fecha_final:
                            vacuna_gato.efectos_secundarios = True
                            identificadores.append(vacuna_gato.identificador)
        for vacuna in self._vacunas:
            if vacuna.identificador in identificadores:
                vacuna.efecto_secundarios = True
        

if __name__ == '__main__':
    v1 = Veterinaria()
    
    # funcion 1
    v1.registrar_animal_con_vacuna("Ciro", "Bulldog Ingles", None, 1, 2022, "Gaspar Morales", 26)
    v1.registrar_animal_con_vacuna("Ciro", "Bulldog Ingles", None, 2, 2023, "Gaspar Morales", 26)
    # v1.registrar_animal_con_vacuna("Ciro", None, None, 3, 2023, "Gaspar Morales", 26)
    # v1.registrar_animal_con_vacuna("Ciro", "Bulldog Ingles", None, 2, 2023, "Gaspar Morales", 26)
    
    v1.registrar_animal_con_vacuna("Sammy", None, ["Blanco"], 3, 2022, "Felipe Dobrinhin", 40)
    v1.registrar_animal_con_vacuna("Sammy", None, ["Blanco"], 4, 2023, "Gaspar Morales", 40)
    # v1.registrar_animal_con_vacuna("Sammy", None, None, 5, 2022, "Felipe Dobrinhin", 40)
    # v1.registrar_animal_con_vacuna("Sammy", None, ["Blanco"], 4, 2023, "Gaspar Morales", 40)
    
    # funcion 2
    # v1.validar_vacunas_y_efectos_secundarios("Bulldog Ingles", "Blanco", 2020, 2024)
    # v1.validar_vacunas_y_efectos_secundarios("Labrador", "Blanco", 2020, 2024)
    # v1.validar_vacunas_y_efectos_secundarios("Bulldog Ingles", "verde radioactivo", 2020, 2024)
    v1.validar_vacunas_y_efectos_secundarios("Labrador", "verde radioactivo", 2020, 2024)

print("hola")
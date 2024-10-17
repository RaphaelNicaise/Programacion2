class Participante:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        """
        Inicializa un nuevo participante.

        :param nombre: Nombre del participante.
        :param edad: Edad del participante.
        :param nacionalidad: Nacionalidad del participante.
        """
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplinas = []

    def __str__(self):
        """
        Devuelve una representación en cadena del participante.

        :return: Cadena con el nombre, edad y nacionalidad del participante.
        """
        return f"Nombre: {self.__nombre} Edad: {self.__edad} Nacionalidad: {self.__nacionalidad}"
    
    def __repr__(self):
        """
        Devuelve una representación oficial del participante.

        :return: Cadena con el nombre del participante.
        """
        return f"({self.__nombre})"
    
    # Comandos
    def establecerNombre(self, nombre: str):
        """
        Establece el nombre del participante.

        :param nombre: Nuevo nombre del participante.
        """
        self.__nombre = nombre
        
    def establecerEdad(self, edad: int):
        """
        Establece la edad del participante.

        :param edad: Nueva edad del participante.
        """
        self.__edad = edad
        
    def establecerNacionalidad(self, nacionalidad: str):
        """
        Establece la nacionalidad del participante.

        :param nacionalidad: Nueva nacionalidad del participante.
        """
        self.__nacionalidad = nacionalidad
    
    def agregarDisciplina(self, disciplina: 'Disciplina'):
        """
        Agrega una disciplina al participante.

        :param disciplina: Disciplina a agregar.
        :raises ValueError: Si el objeto no es una instancia de Disciplina.
        """
        if not isinstance(disciplina, Disciplina):
            raise ValueError("Error al ingresar la disciplina")
        
        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)    
            disciplina.agregarParticipante(self)
            
    # Consultas
    def obtenerNombre(self) -> str:
        """
        Obtiene el nombre del participante.

        :return: Nombre del participante.
        """
        return self.__nombre

    def obtenerEdad(self) -> int:
        """
        Obtiene la edad del participante.

        :return: Edad del participante.
        """
        return self.__edad
    
    def obtenerNacionaldiad(self) -> str:
        """
        Obtiene la nacionalidad del participante.

        :return: Nacionalidad del participante.
        """
        return self.__nacionalidad
        
    def obtenerDisciplinas(self) -> list:
        """
        Obtiene la lista de disciplinas del participante.

        :return: Lista de disciplinas.
        """
        return self.__disciplinas
        
class Disciplina:
    def __init__(self, nombre: str, descripcion: str):
        """
        Inicializa una nueva disciplina.

        :param nombre: Nombre de la disciplina.
        :param descripcion: Descripción de la disciplina.
        """
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes = []
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la disciplina.

        :return: Cadena con el nombre, descripción y número de participantes de la disciplina.
        """
        return f'Disciplina: {self.__nombre} Descripcion: {self.__descripcion} Participantes: {len(self.__participantes)}'
    
    def __repr__(self):
        """
        Devuelve una representación oficial de la disciplina.

        :return: Cadena con el nombre y descripción de la disciplina.
        """
        return f'({self.__nombre},{self.__descripcion})'
    
    # Comandos
    def establecerNombre(self, nombre: str):
        """
        Establece el nombre de la disciplina.

        :param nombre: Nuevo nombre de la disciplina.
        """
        self.__nombre = nombre
        
    def establecerDescripcion(self, descripcion: str):
        """
        Establece la descripción de la disciplina.

        :param descripcion: Nueva descripción de la disciplina.
        """
        self.__descripcion = descripcion
    
    def agregarParticipante(self, participante: 'Participante'):
        """
        Agrega un participante a la disciplina.

        :param participante: Participante a agregar.
        """
        if participante not in self.__participantes:
            self.__participantes.append(participante)
    
    # Consultas
    def obtenerNombre(self) -> str:
        """
        Obtiene el nombre de la disciplina.

        :return: Nombre de la disciplina.
        """
        return self.__nombre

    def obtenerDescripcion(self) -> str:
        """
        Obtiene la descripción de la disciplina.

        :return: Descripción de la disciplina.
        """
        return self.__descripcion
    
    def obtenerParticipantes(self) -> list:
        """
        Obtiene la lista de participantes de la disciplina.

        :return: Lista de participantes.
        """
        return self.__participantes
    
class tester:
    @staticmethod
    def run():
        """
        Método de prueba para verificar el funcionamiento de las clases Participante y Disciplina.
        """
        futbol = Disciplina("Futbol", "11v11 Pelota Redonda")
        basket = Disciplina("Basket", "5v5 Pelota Redonda")
        rugby = Disciplina("Rugby", "15v15 Pelota Ovalada")
        participante_1 = Participante("Raphael", 19, "Frances")
        
        print(participante_1)
        print(participante_1.obtenerDisciplinas())
        
        print(participante_1.obtenerDisciplinas())
        print(futbol.obtenerParticipantes())
        
        participante_2 = Participante("Roman", 19, "Argentino")
        
        participante_2.agregarDisciplina(basket)
        participante_2.agregarDisciplina(futbol)
        participante_2.agregarDisciplina(basket)  # No lo agrega porque ya está en las disciplinas del participante
        print(participante_2.obtenerDisciplinas())
        print(futbol.obtenerParticipantes()[0])
        
        participante_1.agregarDisciplina(futbol)
        participante_1.agregarDisciplina(rugby)
        participante_1.agregarDisciplina(basket)
        
        print(participante_1.obtenerDisciplinas())
if __name__ == "__main__":
    tester.run()
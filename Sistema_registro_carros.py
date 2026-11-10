class Autos:
    def __init__(self, llantas, golpes, rayones, vidrio, num_placas, año_modelo, color):
        self.llantas = llantas
        self.golpes = golpes
        self.rayones = rayones
        self.vidrio = vidrio
        self.num_placas = num_placas
        self.año_modelo = año_modelo
        self.color = color


class Ford(Autos):
    modelos = ["Ford 2011", "ford 2015", "ford 2020"]

    def __init__(self, modelo, llantas, golpes, rayones, vidrio, num_placas, año_modelo, color):
        super().__init__(llantas, golpes, rayones, vidrio, num_placas, año_modelo, color)
        self.modelo = modelo if modelo in Ford.modelos else False


class Chevrolet(Autos):
    modelos = ["chevrolet 2012", "chevrolet 2016", "chevrolet 2021"]

    def __init__(self, modelo, llantas, golpes, rayones, vidrio, num_placas, año_modelo, color):
        super().__init__(llantas, golpes, rayones, vidrio, num_placas, año_modelo, color)
        self.modelo = modelo if modelo in Chevrolet.modelos else False


class Nissan(Autos):
    modelos = ["Nissan 2013", "Nissan 2017", "Nissan 2022"]

    def __init__(self, modelo, llantas, golpes, rayones, vidrio, num_placas, año_modelo, color):
        super().__init__(llantas, golpes, rayones, vidrio, num_placas, año_modelo, color)
        self.modelo = modelo if modelo in Nissan.modelos else False


class Toyota(Autos):
    modelos = ["Toyota 2014", "Toyota 2018", "Toyota 2023"]

    def __init__(self, modelo, llantas, golpes, rayones, vidrio, num_placas, año_modelo, color):
        super().__init__(llantas, golpes, rayones, vidrio, num_placas, año_modelo, color)
        self.modelo = modelo if modelo in Toyota.modelos else False


def menu():
    autos_creados = []

    while True:
        print("Menu")
        print("1. Crear Ford")
        print("2. Crear Chevrolet")
        print("3. Crear Nissan")
        print("4. Crear Toyota")
        print("5. Mostrar autos creados")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Modelos disponibles:", Ford.modelos)
            modelo = input("Elige modelo: ")
            auto = Ford(modelo,
                        int(input("Número de llantas: ")),
                        int(input("Número de golpes: ")),
                        int(input("Número de rayones: ")),
                        input("Vidrio en buen estado (si/no): ").lower() == "si",
                        input("Número de placas: "),
                        int(input("Año del modelo: ")),
                        input("Color: "))
            if auto.modelo is False:
                print("modelo no existe")
            else:
                autos_creados.append(auto)
                print(" Auto Ford creado correctamente")

        elif opcion == "2":
            print("Modelos disponibles:", Chevrolet.modelos)
            modelo = input("Elige modelo: ")
            auto = Chevrolet(modelo,
                             int(input("Numero de llantas: ")),
                             int(input("Numero de golpes: ")),
                             int(input("Numero de rayones: ")),
                             input("Vidrio en buen estado si o no: ").lower() == "si",
                             input("Numero de placas: "),
                             int(input("Año del modelo: ")),
                             input("Color: "))
            if auto.modelo is False:
                print("modelo no existe.")
            else:
                autos_creados.append(auto)
                print(" Auto Chevrolet creado correctamente")

        elif opcion == "3":
            print("Modelos disponibles:", Nissan.modelos)
            modelo = input("Elige modelo: ")
            auto = Nissan(modelo,
                          int(input("Numero de llantas: ")),
                          int(input("Numero de golpes: ")),
                          int(input("Numero de rayones: ")),
                          input("Vidrio en buen estado si o no: ").lower() == "si",
                          input("Numero de placas: "),
                          int(input("Año del modelo: ")),
                          input("Color: "))
            if auto.modelo is False:
                print("modelo no existe.")
            else:
                autos_creados.append(auto)
                print(" Auto Nissan registrado.")

        elif opcion == "4":
            print("Modelos disponibles:", Toyota.modelos)
            modelo = input("Elige modelo: ")
            auto = Toyota(modelo,
                          int(input("Numero de llantas: ")),
                          int(input("Numero de golpes: ")),
                          int(input("Numero de rayones: ")),
                          input("Vidrio en buen estado si o no: ").lower() == "si",
                          input("Numero de placas: "),
                          int(input("Año del modelo: ")),
                          input("Color: "))
            if auto.modelo is False:
                print("modelo no existe.")
            else:
                autos_creados.append(auto)
                print(" Auto Toyota creado correctamente")

        elif opcion == "5":
            print("\n--- AUTOS CREADOS ---")
            for a in autos_creados:
                print(f"{a.__class__.__name__} - {a.modelo}, Placas: {a.num_placas}, Color: {a.color}, Año: {a.año_modelo}")

        elif opcion == "6":
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

menu()
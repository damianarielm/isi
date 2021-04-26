clave  = "1234"
opcion = " "

while opcion != "0":
    print("1 - Empresas")
    print("2 - Clientes")
    print("0 - Salir")
    opcion = input("Ingrese una opcion: ")

    if opcion == "2":
        print("Programa en proceso.")

    if opcion == "1":
        intentos = 2
        while input("Ingrese la clave: ") != clave and intentos:
            intentos -= 1

        if intentos == 0:
            print("Clave incorrecta.")
            opcion = "0" # Sale del programa
        else:
            while opcion != "0":
                print("1 - Alta de empresas")
                print("0 - Volver al menu principal")
                opcion = input("Ingrese una opcion: ")

                if opcion == "1":
                    ba = ros = cba = 0
                    while cod_ciudad := input("Ingrese codigo de ciudad "
                                              "(enter para salir): "):

                        if cod_ciudad.lower() == "ba":
                            ba += 1
                            nombre_ciudad = "Buenos Aires"
                        if cod_ciudad.lower() == "ros":
                            ros += 1
                            nombre_ciudad = "Rosario"
                        if cod_ciudad.lower() == "cba":
                            cba += 1
                            nombre_ciudad = "Cordoba"

                        cod_empresa = input("Ingrese codigo de empresa: ")
                        nombre = input("Ingrese nombre de la empresa: ")
                        direccion = input("Ingrese direcion de la empresa: ")
                        mail = input("Ingrese mail de empresa: ")
                        telefono = input("Ingrese telefono de empresa: ")

                    if ba > ros and ba > cba:
                        print(f"La ciudad con mas empresas es Buenos Aires ({ba}).")
                    if ros > ba and ros > cba:
                        print(f"La ciudad con mas empresas es Rosario({ros}).")
                    if cba > ros and cba > ba:
                        print(f"La ciudad con mas empresas es Cordoba ({cba}).")

            opcion = " " # Vuelve al menu principal

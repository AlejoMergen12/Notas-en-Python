import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nOK!! Vamos a registrarte en el sistema..")
        
        nombre = input("Cual es tu Nombre? : ")
        apellidos = input("Cuales son tus Apellidos? : ")
        email = input("Introduce tu Email : ")
        password = input("Introduce tu Contraseña : ")
    
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")

        else:
            print("\nNo te registrate correctamente")

    def login(self):
        print("\nBien!! Identificate en el sistema... ")

        try:
            email = input("Introduce tu Email : ")
            password = input("Introduce tu Contraseña : ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)

        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print(f"login incorrecto!!")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar notas (mostrar)
        - Eliminar notas (eliminar)
        - salir (salir)
        """)

        accion = input("Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == 'salir':
            print(f"Ok {usuario[1]}, has luego")

            exit()

        return None


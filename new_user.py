import platform
import sys
import subprocess

class usuario_windows:
    def __init__(self):
        self.sistema = "Windows"

    def nuevo(self):
        # Parámetros para la creación de usuario
        usuario = "NuevoUsuario"
        
        orden = f'net user {usuario} {usuario} /add'
        subprocess.Popen(['powershell', '-Command', orden], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        print("Se ha creado un usuario en Windows")

class usuario_linux:
    def __init__(self):
        self.sistema = "Linux"

    def nuevo(self):
        print("Se ha creado un usuario en Linux")

class usuario_mac:
    def __init__(self):
        self.sistema = "MacOS"

    def nuevo(self):
        print("Se ha creado un usuario en MacOS")

sistema_operativo = platform.system()
if len(sys.argv) > 1:
    argumento = sys.argv[1]
    print ("Argumento aceptado, creando usuario...")
    print("El usuario a crear es: ", argumento)

    if sistema_operativo == "Windows":
            nuevo_usuario = usuario_windows()
            nuevo_usuario.nuevo()
    elif sistema_operativo == "Linux":
            print("es linux")
    elif sistema_operativo == "Darwin":
            print("es macOS")
    else:
            print("Sistema operativo no compatible")
else:
    print("No se proporcionaron argumentos.")

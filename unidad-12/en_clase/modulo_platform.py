

import platform

sistema_operativo = platform.system()

print(sistema_operativo)

version_sistema = platform.version()
print("Version del sistema: ", version_sistema)

print(platform.release())

architecture = platform.architecture()

print("Arquitectura del sistema: ", architecture)




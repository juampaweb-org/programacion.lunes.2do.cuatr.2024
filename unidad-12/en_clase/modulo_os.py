

import os


uname = os.uname()

sysname = uname.sysname
nodename = uname.nodename
release = uname.release
version = uname.version
machine = uname.machine

print("Sistema operativo: ", sysname)
print("Nombre del nodo: ", nodename)
print("Release del sistema: ", release)
print("Version del sistema: ", version)
print("Arquitectura del sistema: ", machine)


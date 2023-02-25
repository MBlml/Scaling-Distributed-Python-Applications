# Scaling-Distributed-Python-Applications
#### BARAJAS GOMEZ JUAN MANUEL | 216557005 | COMPUTACION TOLERANTE A FALLAS | 24/02/2023

### OBJETIVO:
Generar un programa donde se utilizaran hilos, procesos y demonios para el escalado de aplicaciones distribuidas en Python.

### DESARROLLO:
## Scaling Distributed Python Applications
La escalabilidad de las aplicaciones distribuidas en Python se refiere a la capacidad de la aplicación para manejar un mayor volumen de datos y tráfico sin disminuir el rendimiento. Para lograr una escalabilidad efectiva, es necesario utilizar técnicas como la división de carga de trabajo, la optimización de consultas de bases de datos, el uso de cachés y la implementación de técnicas de procesamiento paralelo. También es importante considerar la infraestructura de hardware y software utilizada y optimizar el uso de los recursos disponibles. Además, el monitoreo y la gestión del rendimiento son críticos para garantizar que la aplicación pueda manejar los aumentos en el tráfico y la carga de trabajo de manera efectiva.

## Hilos, procesos y demonios
Los hilos, procesos y demonios son técnicas de programación utilizadas para lograr la concurrencia y paralelismo en las aplicaciones de software. Los hilos son subprocesos de ejecución dentro de un proceso, que comparten la misma memoria y recursos de la CPU, y se utilizan para ejecutar tareas concurrentes y pequeñas. Los procesos, por otro lado, son instancias separadas del programa, que ejecutan en un entorno aislado y seguro, y son ideales para aprovechar la capacidad de múltiples núcleos. Los demonios son procesos en segundo plano, que se ejecutan continuamente sin interrupción, y son utilizados para tareas de mantenimiento y monitoreo en el sistema operativo. Cada técnica tiene sus propias ventajas y desventajas y debe ser utilizada adecuadamente según las necesidades específicas de la aplicación y del entorno de ejecución.

_Algunos ejemplos de sintaxis en Python para crear y administrar hilos, procesos y demonios son:_

### HILOS
```python
import threading

def worker():
    """Función que será ejecutada por el hilo"""
    print("Hilo trabajando")

# Crear un hilo
thread = threading.Thread(target=worker)

# Iniciar el hilo
thread.start()

# Esperar a que el hilo termine antes de continuar con el programa principal
thread.join()
```

### PROCESOS
```python
import multiprocessing

def worker():
    """Función que será ejecutada por el proceso"""
    print("Proceso trabajando")

# Crear un proceso
process = multiprocessing.Process(target=worker)

# Iniciar el proceso
process.start()

# Esperar a que el proceso termine antes de continuar con el programa principal
process.join()
```

### DEMONIOS
```python
import multiprocessing

def worker():
    """Función que será ejecutada por el demonio"""
    while True:
        print("Demonio trabajando")

# Crear un demonio
daemon = multiprocessing.Process(target=worker)

# Indicar que es un demonio
daemon.daemon = True

# Iniciar el demonio
daemon.start()

# El programa principal puede continuar ejecutándose mientras el demonio corre en segundo plano
```

### EJEMPLO EN PRACTICA:


##### _(El codigo se puede descargar en el archivo de la parte superior)_

```python
#Scaling Distributed en Python

import threading
import multiprocessing
import time
import os

# Definimos una función que ejecutará el hilo
def thread_function():
    print(f"Hilo: {threading.current_thread().name} iniciado")
    time.sleep(2)
    print(f"Hilo: {threading.current_thread().name} finalizado")

# Definimos una función que ejecutará el proceso
def process_function():
    print(f"Proceso: {os.getpid()} iniciado")
    time.sleep(2)
    print(f"Proceso: {os.getpid()} finalizado")

if __name__ == "__main__":
    # Creamos un hilo
    thread = threading.Thread(target=thread_function, name="Hilo1")
    thread.start()

    # Creamos un proceso
    process = multiprocessing.Process(target=process_function)
    process.start()

    # Creamos un demonio
    with open("daemon.log", "w") as f:
        f.write("Demonio iniciado\n")
    pid = os.fork()
    if pid == 0:
        # Estamos en el proceso hijo, que se convertirá en demonio
        os.setsid()
        with open(os.devnull, "w") as devnull:
            # Redirigimos la salida estándar y error a /dev/null
            os.dup2(devnull.fileno(), sys.stdout.fileno())
            os.dup2(devnull.fileno(), sys.stderr.fileno())
        # Ejecutamos un bucle infinito para que el proceso no termine
        while True:
            with open("daemon.log", "a") as f:
                f.write("Demonio vivo\n")
            time.sleep(1)
    else:
        # Estamos en el proceso padre, que finaliza
        print("Proceso padre finalizando")
```

![imagen](https://user-images.githubusercontent.com/101375005/221329899-0ea3e3fa-ec2a-4c57-96e5-f5c3f64c26f3.png)

### CONCLUSIÓN:
En conclusión, la escalabilidad de aplicaciones Python distribuidas se puede lograr mediante el uso de hilos, procesos y demonios.
Cada uno de estos enfoques ofrece ventajas y desventajas en términos de eficiencia, complejidad y control sobre el entorno de ejecución.

Los hilos son ideales para aplicaciones que tienen una gran cantidad de tareas pequeñas y no críticas que se pueden ejecutar de manera concurrente. 
Los procesos son más adecuados para aplicaciones que requieren un mayor aislamiento y seguridad, y que necesitan aprovechar mejor la capacidad de múltiples núcleos. 
Por último, los demonios son excelentes para tareas en segundo plano que deben ejecutarse de manera continua sin interrupción.

### REFERENCIAS:
_1.1.4 «APLICACIONES DISTRIBUIDAS». (2013, 9 marzo). «DESARROLLO DE APLICACIONES PARA AMBIENTES DISTRIBUIDOS». https://laurmolina7821.wordpress.com/1-1-4-aplicaciones-distribuidas/_ 

_Cómo se administran las instancias. (s. f.). Google Cloud. https://cloud.google.com/appengine/docs/legacy/standard/python/how-instances-are-managed?hl=es-419_

_Desarrollo de Sistemas Distribuidos. (s. f.). SG Buzz. https://sg.com.mx/revista/58/desarrollo-de-sistemas-distribuidos_


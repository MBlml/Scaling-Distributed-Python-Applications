#Scaling Distributed en Python

import threading
import multiprocessing
import time
import os
import sys

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
 
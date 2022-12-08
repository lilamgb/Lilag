# Lilag
pp5 intro prog

# refinando_codigo_22-0638

# INTRODUCCION 


En esta primer paso, refinaremos el codigo, limpiamos el codigo usando pylint, autopep8 y ponerlo en un repositorio de GitHub.

# REFACTORIZACION 

primero que todo creamos una funcion que convierte el archivo externo a una lista con open(), esta se guarda en una variable que se devuelve al usuario. La segunda funcion que utiliza la variable de la primera funcion como indicador, se suman todos los valores de la lista. La tercera funcion es la que imprime el resultado e utiliza las dos funciones anteriores.

# LIMPIEZA
Se utiliza pylint para obtener una puntuacion del trabajo y que se debe de arreglar. La solucion tendio a ser usar docstrings a las funciones. Luego se usa autopep8 y copiar el resultado.

# GESTION DE ERRORES

Control de errores
Los errores mas recurrentes fueron usar with open() para abrir el archivo con los costos, tambien algunos errores de adentacion.

Pruebas unitarias
Las pruebas fueron hechas con pytest. Primero para comprobar que la lista de costos era correcta y luego para confirmar que el costo total este correcto. La ultima prueba fue para que la funcion principal no devuelva a otro dato, tan solo el resultado de las funciones anteriores.

link de GitHub: https://github.com/lilamgb/Lilag.git

<img width="1440" alt="Screen Shot 2022-12-08 at 7 16 40 PM" src="https://user-images.githubusercontent.com/120058995/206587084-6c64de7d-d98a-41dc-8d6f-c923e1af4a85.png">

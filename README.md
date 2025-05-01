# Solución Evaluación Conocimientos Plataformas Big Data
Este repositorio de GitHub contiene la solución al proyecto diseñado para evaluar las habilidades técnicas en el ciclo de vida de un datawarehouse.

## Requisitos
- Docker
- VSCode
- Extensión VSCode Dev Containers
- IDE Base de datos (DBeaver)
- Navegador Web Moderno (Google Chrome, Microsoft Edge, Firefox)

## Proceso levantamiento proyecto
1. Abrir VSCode
2. Instalar extensión Dev Containers
3. Pulsar Ctrl + Shift + P
4. Escoger: "Dev Containers: Clone Repository in Named Container Volume" 
5. Colocar la URL de clonación de proyecto de Github (https://github.com/paulocrn/gd-test-bigdata.git)
6. Ingresar nombre del volumen, ejemplo: vsc-prueba

## Inicializar proyecto
Una vez que se haya levantado el dev containers, procedemos a levantar el jupyter con el siguiente comando:

- jupyter lab --allow-root

En consola se mostrara una url para abrir en el navegador, similar a:

- http://localhost:8888/lab?token=020cdb433de383556f61ba0273c4455cf031f98b4fe3f2ac
- http://127.0.0.1:8888/lab?token=020cdb433de383556f61ba0273c4455cf031f98b4fe3f2ac

Validar el puerto en que se abre la imagen, en VSCode en la ventana "PORTS" se puede revisar el puerto que se mapeo a su host local, por lo general, se levanta en el puerto 8888.

### Acceso a la base de datos postgres
El mismo contenedor de desarrollo incluye una base de datos PostgreSQL, el cuál puede ser accedido desde cualquier IDE Gestor de Base de datos (recomendado DBeaver), los parametros de acceso son:
- **Host:** localhost
- **Port:** 5432
- **User:** postgres
- **Pass:** postgres
- **Database:** postgres

## Estructura del proyecto
El proyecto maneja la siguiente estructura:

- - **/notebooks:** es aquí donde se encontrará todo lo necesario para la solución del test.
  - Cada Ejercicio consta de una carpeta, por lo que existen las carpeta Ejercicio 1, Ejercicio 2 y Ejercicio 3.
  - Existe un archivo de conexion para la base de datos (db_conexion.py)

## Pasos a Seguir Para Generar La Solución
- - **/Ejercicio 1:** Abrir la carpeta Ejercicio 1, dentro de esta carpeta se encuentran tres archivos que deben ser ejecutados de la siguiente forma:
  - Abrir el archivo 1-crear_tablas.ipynb y ejecutar todas las celdas en el orden planteado, al final mostrar el mensaje "Proceso de creación de tablas completado".
  - Abrir el archivo 2-generar-data-prueba.ipynb y ejecutar todas las celdas en el orden planteado, esto genera la data necesaria para insertar en las tablas, al finalizar crea una carpeta csv con los archivos para cada tabla.
  - Abrir el archivo 3-insertar_data_tablas.ipynb y ejecutar todas las celdas en el orden planteado, esto genera la inserción de la data previamente generada en las tablas del archivo 1, al finalizar mostrar la imagen del modelo ER.

- - **/Ejercicio 2:** Abrir la carpeta Ejercicio 2, dentro de esta carpeta se encuentran dos archivos que deben ser ejecutados de la siguiente forma:
  - Abrir el archivo crear_datawarehouse.ipynb y ejecutar todas las celdas en el orden planteado, al final mostrar el mensaje "Proceso de creación de tablas datawarehouse completado.".
  - Abrir el archivo poblar_datawarehouse.ipynb y ejecutar todas las celdas en el orden planteado, esto inserta la data necesaria dentro de nuestro datawarehouse.

- - **/Ejercicio 3:** Abrir la carpeta Ejercicio 3, dentro de esta carpeta se encuentran un archivo que deben ser ejecutados de la siguiente forma:
  - Abrir el archivo final.ipynb y ejecutar todas las celdas en el orden planteado, al final genera el reporte con la solución".

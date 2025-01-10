# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import zipfile
import os
import pandas as pd

def pregunta_01():
     
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """  
    # Definición de rutas necesarias
    ruta_zip = "files/input.zip"
    ruta_ext = "files"
    ruta_out = "files/output"
    ruta_datos = "files/input"
    
    # Función para extraer archivos del ZIP
    def extraer_archivo():
        try:
            if os.path.exists(ruta_ext) and os.listdir(ruta_ext):
                print(f"Los archivos ya se encuentran extraídos en: {ruta_ext}")
            else:
                with zipfile.ZipFile(ruta_zip, 'r') as archivo_zip:
                    archivo_zip.extractall(ruta_ext)
                    print(f"Archivos extraídos exitosamente en: {ruta_ext}")
        except FileNotFoundError:
            print("Error: archivo ZIP no encontrado.")
        except FileExistsError:
            print("Error: archivo ZIP no válido.")
    
    # Función para crear la carpeta de salida si no existe
    def crear_directorio_salida():
        os.makedirs(ruta_out, exist_ok=True)
        print(f"Directorio de salida creado o ya existente: {ruta_out}")
    
    # Función para procesar un directorio y recolectar datos
    def procesar_directorio(directorio):
        datos = []
        for categoria in ['positive', 'negative', 'neutral']:
            ruta_categoria = os.path.join(directorio, categoria)
            if os.path.exists(ruta_categoria):
                print(f"Processing category: {categoria}")
                for archivo in os.listdir(ruta_categoria):
                    ruta_archivo = os.path.join(ruta_categoria, archivo)
                    if os.path.isfile(ruta_archivo):
                        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_texto:
                            contenido = archivo_texto.read().strip()
                            datos.append({'phrase': contenido, 'target': categoria})
                            print(f"Processed file: {ruta_archivo}")
            else:
                print(f"Category directory does not exist: {ruta_categoria}")
        return datos
                            print(f"Processed file: {ruta_archivo}")
            else:
                print(f"Category directory does not exist: {ruta_categoria}")
        return datos
    
    # Función para crear y guardar los DataFrames
    def generar_dataframes():
        datos_entrenamiento = procesar_directorio(os.path.join(ruta_datos, 'train'))
        datos_prueba = procesar_directorio(os.path.join(ruta_datos, 'test'))
        
        pd.DataFrame(datos_entrenamiento).to_csv(os.path.join(ruta_out, 'train_dataset.csv'), index=False)
        pd.DataFrame(datos_prueba).to_csv(os.path.join(ruta_out, 'test_dataset.csv'), index=False)
    
    # Función principal que coordina las operaciones
    def ejecutar():
        extraer_archivo()
        crear_directorio_salida()
        generar_dataframes()
        print("Procesamiento de datos completado.")
    
    ejecutar()

pregunta_01()
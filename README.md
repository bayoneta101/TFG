# TFG - Estudio del Crecimiento de las Espinas Dendríticas del Cerebro Usando Morphing 3D

Autor: Marcos García Postigo
Tutor: Angel Merchán Pérez

### Estructura del repositorio
- Animacion - Blender: contiene los archivos .blend de Blender con los que se han animado las espinas dendríticas(ED).
- Complementos tfg memoria: archivos adicionales que se han usado para completar la memoria
- env: entorno virtual de python que contiene las librerias y permite cargarlas ejecutando el script .TFG\Scripts\activate 
- Pruebas: directorio que contiene pruebas tanto en Python como en Blender, en sus respectivos directorios
- Spines and SpApp v5 Hausdorff nonsynaptic etiquetas corr.xlsx: archivo excel que contiene informacion sobre todas las ED del proyecto.

### Resumen
Las espinas dendríticas (ED) son unas protuberancias que tienen las neuronas del cerebro. Son importantes porque sobre ellas se producen la mayoría de los contactos entre neuronas o sinapsis. Las ED son estructuras cambian de forma y tamaño continuamente. Disponemos de numerosas ED reconstruidas a partir de imágenes de microscopio electrónico. Estás ED se encuentran en diferentes momentos de su crecimiento. 
En este trabajo intentamos reproducir el crecimiento de las ED realizando morphing 3D entre espinas que se encuentran en distintos momentos de su desarrollo. El morphing 3D es una técnica de animación que trata de transformar suavemente un objeto 3D en otro diferente. Para realizarlo, hemos investigado y desarrollado técnicas de animación en Python y Blender para animar conjuntos de modelos 3D de las ED, seleccionados de distintas regiones y capas del cerebro. 
Como paso previo a la animación, los modelos 3D se diezman reduciendo su número de vértices para facilitar su manipulación y disminuir el tiempo de renderizado. Inicialmente este diezmado se realizaba en Python pero como no se obtuvieron los resultados esperados se decidió continuar con Blender únicamente.
Posteriormente se animan las espinas dendríticas generando las transiciones entre una y la inmediatamente siguiente en un conjunto dado y se repite hasta terminar con el conjunto de ED. Esta transición se ha creado usando varias técnicas que se han desarrollado a lo largo del Trabajo de Fin de grado. 
La primera técnica o técnica 1 se basa en ajustar uno de los modelos 3D a una copia de menor volumen del otro modelo para que quede escondida dentro del mismo y animar su crecimiento, generando la ilusión de que crece desde dentro del otro modelo 3D. Sin embargo, esta técnica no generaba animaciones lo suficientemente fluidas por lo que se revisó y mejoró.
La segunda técnica o técnica 2 es un proceso similar al anterior pero sin copia de ninguno de los modelos. En su lugar cada uno de los dos modelos trata de ajustarse al otro, de tal manera que mientras uno crece el otro decrece, consiguiendo un efecto más convincente que además requiere de menos trabajo para implementarse.
Seguidamente, se decidió aplicar un suavizado a los modelos de las espinas dendríticas como mejora visual, utilizando para ello las mallas obtenidas con la segunda técnica.
Por último se exponen todas las animaciones realizadas, tanto las finales como las animaciones que implementan las técnicas anteriores donde se puede apreciar la mejora según hemos conseguido más experiencia y conocimientos de animación.

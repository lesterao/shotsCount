# shotsCount
Script para contar acciones anotadas, shots anotados y tiempo total de anotaciones.

Se debe poner en el directiorio
VN\CV\SCV\YtBev\AnnotaShots

Ejecutar usando:
python info.py > salida.txt

El script genera un archivo con nombre
_xACTMxC&VNx&xNombreVideox_mp4.txt

xACT -> es el total de acciones en el fichero. 
VNx  -> es el directorio VN\CV\SCV\YtBev\AnnotaShots\VNx
xNombreVideox -> es reemplazado por el nombre del video

En salida.txt se encuentra un resumen de cada fichero y la suma de acciones y tiempo de todos los ficheros.

Se genera el ejecutable usando
python setup.py py2exe

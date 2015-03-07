# shotsCount
Script para contar acciones anotadas, shots anotados y tiempo total de anotaciones.

git clone https://github.com/lesterao/shotsCount.git

Generar el ejecutable usando
python setup.py py2exe

Poner el ejecutable en el directiorio
VN\CV\SCV\YtBev\AnnotaShots

Ejecutar usando:
info.exe > salida.txt

El script genera un archivo con nombre
CITEDI_xACTMxC&VNx&xNombreVideox_mp4.txt

La x en xACT -> es el total de acciones en el fichero. 
La x en VNx  -> es el directorio VN\CV\SCV\YtBev\AnnotaShots\VNx
xNombreVideox -> es reemplazado por el nombre del video

En salida.txt se encuentra un resumen de cada fichero y la suma total de acciones y tiempo total de anotacion de todos los ficheros.

Ejemplo del fichero de salida para VN1:
CITEDI_18ACTMxC&VN1&CV1&SCV1&YtBevRlXIGcaWwRc&MX&20090608_mp4
Frames Anotados Fichero: 17
Total Video Anotado Fichero: 00:03:57
Total Acciones Anotadas Fichero: 18

Ejemplo del fichero >salida.txt:
Fichero: .\VN1/ELAN_ACTANN_MxC&VN1&CV1&SCV1&YtBevRlXIGcaWwRc&MX&20090608_mp4.txt
Shots Anotados Fichero: 17
Total Video Anotado Fichero: 00:03:57
Total Acciones Anotadas Fichero: 18
-------------------------------------------
**************Totales***************
Total Video Anotado = 00:03:57
Total Shots Anotados= 17
Total De Acciones Anotadas= 18

Nota importante:
Se debe respetar los nombes de los ficheros .txt shots_ANN_ y _ACTANN_ ejemplo:
ELAN_8shots_ANN_Mx2qoiudfnasrwaer.mp4.txt
ELAN_ACTANN_Mx2qoiudfnasrwaer.mp4.txt
Recordar que el script busca primeramente el fichero de anotacion ANN, suma los tiempos y los shots. Luego busca el ACTANN y suma las acciones anotadas. Al finalizar crea el fichero de salida CITEDI_.
Si no se respeta el nombre de los .txt es posible que tenga este resultado en la salida:
Frames Anotados Fichero: -1
Total Video Anotado Fichero: 0
Total Acciones Anotadas Fichero: 18
Esto debido a que encuentra primero el fichero ACTANN.








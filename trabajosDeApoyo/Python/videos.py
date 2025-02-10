import pytube
import os
url_video = "https://www.youtube.com/watch?v=PXDlU0YDQ6U&list=RD3ZZEJSPf9Vw&index=12"
carpeta_destino = "Descargas/Videos.py"
Nombre_archivo = "LingerCranberries.mp3"
ruta_completa = os.path.join(carpeta_destino,Nombre_archivo)
yt = pytube.YouTube(url_video)
audio = yt.streams.filter(only_audio=True).first()
audio.download(output_path=carpeta_destino,filename=Nombre_archivo)
print("Audio descargado satisfactoriamente en la carpeta:", carpeta_destino)

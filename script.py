from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

url = "https://www.youtube.com/watch?v=_hHzhijt-Jk"
destino = Path("pasta_video")
destino.mkdir(exist_ok=True)

yt = YouTube(url, on_progress_callback=on_progress)
print(f"Título: {yt.title}\nDuração: {yt.length}s")

yt.streams.get_highest_resolution().download(output_path=destino)
print(f"Download concluído! Vídeo salvo em: {destino}")

import subprocess, os

directory: str = os.listdir()

for d in directory:
  if d.find('.html') != -1:
    print(f"<p><a href=\"{d}\">{d.removesuffix('.html')}</a></p>")

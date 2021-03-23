# aiformemories

Error: “ImportError: libGL.so.1: cannot open shared object file: No such file or directory” Code Answer’s
- Para eliminar este error se realizó lo siguiente:
- Creación de archivo packages.txt con dependencias debian para opencv:
    - freeglut3-dev
    - libgtk2.0-dev
- Se reemplazó en el archivo requirements el requerimiento de open-cv por: opencv-python--headless

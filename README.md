# Generador de Códigos QR con Logo en Python

Este script lee un archivo con enlaces (separados por líneas o comas), incrusta un logo central personalizado y genera imágenes QR en la resolución deseada dentro de una carpeta independiente.

---

## 💻 Guía de Instalación y Uso en Ubuntu

Sigue estos pasos desde la terminal de Ubuntu para preparar el entorno y ejecutar la aplicación.

### 1. Actualizar el sistema e instalar Python 3 y venv

Abre tu terminal (`Ctrl + Alt + T`) y asegúrate de tener instalados `python3`, `pip` y el módulo de entornos virtuales `python3-venv`:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

### 2. Estructura de archivos esperada

Coloca todos tus archivos dentro de una misma carpeta en tu sistema:

```text
mi_proyecto_qr/
├── [generador_qr.py](file:///home/jefaturafp2026/Documentos/Proyectos/generador_qr/generador_qr.py)
├── [links.txt](file:///home/jefaturafp2026/Documentos/Proyectos/generador_qr/links.txt)
├── logo.png
└── [requirements.txt](file:///home/jefaturafp2026/Documentos/Proyectos/generador_qr/requirements.txt)
```

### 3. Crear y activar el entorno virtual

Ubicado dentro de la carpeta de tu proyecto, crea el entorno virtual de Python:

```bash
python3 -m venv venv
```

Activa el entorno virtual:

```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

Con el entorno virtual activo, instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

### 5. Configurar los archivos de entrada

Asegúrate de tener preparados los siguientes archivos en la raíz del proyecto:

* **`links.txt`**: Archivo con las URLs separadas por comas o saltos de línea.
  
  Ejemplo de contenido:
  ```text
  https://www.google.com, https://www.python.org
  https://ubuntu.com
  https://github.com
  ```

* **`logo.png`**: Imagen del logo que se colocará en el centro del QR (preferiblemente en formato PNG transparente).

### 6. Ejecutar el script

Para generar los códigos QR, ejecuta:

```bash
python3 generador_qr.py
```

Al finalizar el proceso, el script creará automáticamente la carpeta `qrs_output/` con todas las imágenes en resolución 625x625 px por defecto.

---

## ⚙️ Cambiar las dimensiones de los QR

Si deseas modificar el tamaño por defecto (625x625 px), abre el archivo [generador_qr.py](file:///home/jefaturafp2026/Documentos/Proyectos/generador_qr/generador_qr.py) con tu editor preferido (por ejemplo, `nano`):

```bash
nano generador_qr.py
```

Busca las siguientes líneas al final del archivo (dentro del bloque `if __name__ == "__main__":`) y ajusta los valores a tu gusto:

```python
ANCHO_QR = 625  # Cambia por el ancho deseado en px
ALTO_QR = 625   # Cambia por el alto deseado en px
```

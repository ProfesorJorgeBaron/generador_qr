import os
import re
import qrcode
from PIL import Image

def cargar_enlaces(ruta_archivo):
    """Lee el archivo y extrae los enlaces separados por comas o saltos de línea."""
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo de enlaces: {ruta_archivo}")
    
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Separar tanto por comas como por saltos de línea
    enlaces_crudos = re.split(r'[,\n\r]+', contenido)
    
    # Limpiar espacios y filtrar líneas vacías
    enlaces = [link.strip() for link in enlaces_crudos if link.strip()]
    return enlaces

def generar_qr_con_logo(
    url, 
    ruta_logo, 
    ruta_salida, 
    ancho=625, 
    alto=625
):
    """Genera un QR para una URL dada con un logo centrado y dimensiones específicas."""
    # Instanciar el generador de QR
    # Usamos ERROR_CORRECT_H (alto) para que el QR sea legible a pesar de tener un logo encima
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Convertir QR a imagen PIL en modo RGBA
    imagen_qr = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

    # Redimensionar la imagen del QR al tamaño deseado por el usuario
    imagen_qr = imagen_qr.resize((ancho, alto), Image.Resampling.LANCZOS)

    # Si existe el logo, superponerlo en el centro
    if os.path.exists(ruta_logo):
        logo = Image.open(ruta_logo).convert('RGBA')

        # El logo no debe ser mayor al 25% del tamaño del QR para garantizar la lectura
        factor_escala = 0.22
        max_logo_ancho = int(ancho * factor_escala)
        max_logo_alto = int(alto * factor_escala)

        logo.thumbnail((max_logo_ancho, max_logo_alto), Image.Resampling.LANCZOS)

        # Calcular posición centrada
        pos_x = (ancho - logo.width) // 2
        pos_y = (alto - logo.height) // 2

        # Pegar logo respetando canal alfa (transparencia)
        imagen_qr.paste(logo, (pos_x, pos_y), logo)
    else:
        print(f"⚠️ Advertencia: No se encontró el logo en '{ruta_logo}'. Se generará el QR sin logo.")

    # Guardar como PNG
    imagen_qr.save(ruta_salida, format="PNG")

def procesar_qrs(
    archivo_links="links.txt", 
    nombre_logo="logo.png", 
    carpeta_salida="qrs_generados", 
    ancho=625, 
    alto=625
):
    """Función principal para coordinar la lectura y generación de los códigos QR."""
    # Crear carpeta de destino si no existe
    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)
        print(f"📁 Carpeta creada: '{carpeta_salida}'")

    # Cargar enlaces
    try:
        enlaces = cargar_enlaces(archivo_links)
    except Exception as e:
        print(f"❌ Error al leer el archivo de enlaces: {e}")
        return

    if not enlaces:
        print("⚠️ No se encontraron enlaces válidos en el archivo.")
        return

    print(f"🚀 Procesando {len(enlaces)} enlace(s) con resolución {ancho}x{alto}px...\n")

    for i, url in enumerate(enlaces, start=1):
        # Nombre de archivo limpio
        nombre_base = re.sub(r'[^a-zA-Z0-9]', '_', url.replace('https://', '').replace('http://', ''))[:30]
        nombre_imagen = f"qr_{i:02d}_{nombre_base}.png"
        ruta_guardado = os.path.join(carpeta_salida, nombre_imagen)

        generar_qr_con_logo(
            url=url,
            ruta_logo=nombre_logo,
            ruta_salida=ruta_guardado,
            ancho=ancho,
            alto=alto
        )
        print(f"  ✓ [{i}/{len(enlaces)}] Generado: {nombre_imagen} -> {url}")

    print(f"\n✨ ¡Proceso completado! Los códigos QR se guardaron en la carpeta '{carpeta_salida}'.")

if __name__ == "__main__":
    # --- CONFIGURACIÓN Y PARÁMETROS ---
    ARCHIVO_LINKS = "links.txt"   # Archivo de entrada con los enlaces
    LOGO_FILENAME = "logo.png"    # Nombre del archivo del logo en la raíz
    CARPETA_SALIDA = "qrs_output" # Carpeta donde se guardarán los resultados
    
    # Dimensiones configurables (por defecto 625x625)
    ANCHO_QR = 625
    ALTO_QR = 625

    # Ejecución
    procesar_qrs(
        archivo_links=ARCHIVO_LINKS,
        nombre_logo=LOGO_FILENAME,
        carpeta_salida=CARPETA_SALIDA,
        ancho=ANCHO_QR,
        alto=ALTO_QR
    )
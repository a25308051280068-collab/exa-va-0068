# christian Garcia Jimenez Nc=0068
print("christian Garcia Jimenez Nc=0068")
from pathlib import Path
import cv2

# 1. Definir las rutas de trabajo
carpeta_proyecto = Path(__file__).resolve().parent.parent

# Buscar en la carpeta "imagen-original-0068"
carpeta_original = carpeta_proyecto / "imagen-original-0068"

# Probar con cafetera_0068.jpg o cafetera_0068.webp
ruta_original = carpeta_original / "cafetera_0068.jpg"
if not ruta_original.exists():
    ruta_original = carpeta_original / "cafetera_0068.webp"

carpeta_resultados = carpeta_proyecto / "resultados-img-0068"
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img0068 = cv2.imread(str(ruta_original))

# Comprobar que la imagen se haya leído correctamente
if img0068 is None:
    raise FileNotFoundError(
        f"No se pudo leer la imagen: {ruta_original}"
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_0068 = cv2.rotate(
    img0068, cv2.ROTATE_90_CLOCKWISE
)

# 4. Rotar la imagen 45 grados
alto, ancho = img0068.shape[:2]

centro = (ancho // 2, alto // 2)

matriz_rotacion = cv2.getRotationMatrix2D(
    centro, 45, 1.0
)

img45_0068 = cv2.warpAffine(
    img0068,
    matriz_rotacion,
    (ancho, alto)
)

# 5. Redimensionar a 600 píxeles de ancho
# y 500 píxeles de alto
img600x500_0068 = cv2.resize(
    img0068, (600, 500)
)

# 6. Dibujar un rectángulo rojo de 100 x 200
# píxeles sobre una copia de la imagen original
img_rojo_0068 = img0068.copy()

x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200

cv2.rectangle(
    img_rojo_0068,
    (x1, y1),
    (x2, y2),
    (0, 0, 255),
    3
)

# 7. Mostrar las cinco imágenes con sus títulos
cv2.imshow("cafetera original 0068", img0068)

cv2.imshow("cafetera 90 0068", img90_0068)

cv2.imshow("cafetera 45 0068", img45_0068)

cv2.imshow(
    "cafetera 600x500 0068",
    img600x500_0068
)

cv2.imshow("cafetera rojo 0068", img_rojo_0068)

# 8. Guardar las cuatro imágenes procesadas
cv2.imwrite(
    str(carpeta_resultados / "cafetera1-0068.jpg"),
    img90_0068
)

cv2.imwrite(
    str(carpeta_resultados / "cafetera2-0068.jpg"),
    img45_0068
)

cv2.imwrite(
    str(carpeta_resultados / "cafetera3-0068.jpg"),
    img600x500_0068
)

cv2.imwrite(
    str(carpeta_resultados / "cafetera4-0068.jpg"),
    img_rojo_0068
)

# 9. Esperar una tecla y cerrar las ventanas
print("Imágenes procesadas y guardadas.")
print("Presiona una tecla en las ventanas para finalizar.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("christian Garcia Jimenez Nc=0068")
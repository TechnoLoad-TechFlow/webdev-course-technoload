# Guion Lección 7: Espaciado, bordes y centrado: diseño limpio en CSS

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 3
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-07/` y `completed-examples/lesson-07/`

---

## [00:00 - 00:40] Introducción
- **[En pantalla]**: Título: *"Lección 7: Espaciado, Bordes y Centrado"*.
- **[Narración en off]**:
  > "¡Hola! ¿Alguna vez notaste que en nuestras páginas todo aparece pegado a la izquierda y muy apretado? Hoy aprenderás el truco que usan todos los sitios web profesionales para verse ordenados: cómo funcionan las cajas en CSS."

## [00:40 - 01:55] La regla de la caja: `padding`, `border` y `margin`
- **[En pantalla]**: Diagrama de un cuadro con 3 capas:
  - Centro: **Contenido** (texto/imagen)
  - Capa verde interna: **`padding`** (espacio por dentro, como el relleno de un cojín)
  - Línea azul: **`border`** (el marco de la caja)
  - Capa naranja externa: **`margin`** (espacio por fuera para separarse de otros elementos)
- **[Narración en off]**:
  > "En CSS, cada elemento es una caja invisible. Y esa caja tiene tres espacios muy fáciles de distinguir. El **`padding`** es el espacio **por dentro**, entre el texto y el borde, como el relleno de una almohada. El **`border`** es la línea que rodea la caja. Y el **`margin`** es el espacio **por fuera**, que empuja y separa una caja de las demás."

## [01:55 - 03:45] Centrando y creando una tarjeta en JSFiddle
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-07/` (contiene un `<div class="caja">`). Escribir en CSS:
  ```css
  .caja {
    background-color: #ffffff;
    border: 2px solid #cbd5e1;
    border-radius: 12px;
    padding: 24px;
    margin: 30px auto;
    max-width: 400px;
    text-align: center;
  }
  ```
  Presionar **Run** antes y después de `padding` y `margin: 30px auto` para que el alumno vea el efecto visual de cada propiedad.
- **[En pantalla]**: Resaltado en `border-radius: 12px` (*"Esquinas redondeadas"*) y `margin: 30px auto` (*"Centra la caja horizontalmente"*).
- **[Narración en off]**:
  > "Veámoslo en JSFiddle. Tenemos un `div` con la clase `.caja`. Le ponemos fondo blanco y un borde gris de 2 píxeles. Con `border-radius: 12px` redondeamos las esquinas. Ahora mira qué pasa si agregamos `padding: 24px`: el texto respira y ya no choca con el borde. Si limitamos el ancho a `max-width: 400px` y ponemos `margin: 30px auto`, ¡la caja se centra sola en la pantalla! Por último, `text-align: center` centra el texto adentro."

## [03:45 - 04:30] Pausa interactiva
- **[En pantalla]**: Recuadro: *"Pausa el video — Cambia `border-radius` a `24px`, el color del borde a `#3b82f6` y el `padding` a `40px`"*.
- **[Narración en off]**:
  > "Pausa el video y juega con los números en JSFiddle. Prueba qué pasa cuando aumentas el `padding` a `40px` y redondeas más las esquinas con `border-radius: 24px`."

## [04:30 - 05:00] Cierre
- **[En pantalla]**: Resumen: `padding` (dentro) | `border` (marco) | `margin` (fuera) | `text-align: center`.
- **[Narración en off]**:
  > "¡Excelente! Con esto ya tienes todas las herramientas necesarias para construir un proyecto real. En las Lecciones 8 y 9 vamos a crear juntos tu propia **página de perfil personal** desde cero. ¡Vamos allá!"

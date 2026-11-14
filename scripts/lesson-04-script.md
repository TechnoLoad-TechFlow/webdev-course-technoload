# Guion Lección 4: Imágenes y listas: páginas más visuales y ordenadas

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 2
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-04/` y `completed-examples/lesson-04/`

---

## [00:00 - 00:35] Introducción
- **[En pantalla]**: Título: *"Lección 4: Imágenes (`<img>`) y Listas (`<ul>`, `<ol>`)"*.
- **[Narración en off]**:
  > "¡Hola! Hasta ahora nuestras páginas solo tienen texto y enlaces. Hoy vamos a hacer que se vean mucho más interesantes agregando **imágenes** y organizando información con **listas**, igual que en los menús y tops que ves en internet."

## [00:35 - 02:10] Etiqueta de imagen `<img>` (sin etiqueta de cierre)
- **[En pantalla]**: Código destacado:
  `<img src="https://..." alt="Descripción" width="250">`
  Nota en pantalla: *"`<img>` no lleva etiqueta de cierre `</img>`"*.
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-04/`, completar el atributo `src` y `alt` de la imagen de ejemplo y presionar **Run**.
- **[Narración en off]**:
  > "Para mostrar una foto usamos la etiqueta `<img>`. A diferencia de `<p>` o `<h1>`, `<img>` no envuelve texto, así que **no tiene etiqueta de cierre**. Necesita dos atributos clave: `src`, que es la dirección de la imagen, y `alt`, que es un texto breve que describe la foto por si no carga o para personas que usan lectores de pantalla. También podemos añadir `width="250"` para controlar su ancho en píxeles. Presionamos **Run** y ¡ahí aparece nuestra imagen!"

## [02:10 - 03:45] Listas con viñetas (`<ul>`) y listas numeradas (`<ol>`)
- **[Acción en JSFiddle]**: Escribir una lista `<ul>` de pasatiempos y una lista `<ol>` de pasos o top 3:
  ```html
  <h2>Mis pasatiempos</h2>
  <ul>
    <li>Escuchar música</li>
    <li>Jugar fútbol</li>
    <li>Diseñar páginas web</li>
  </ul>

  <h2>Top 3 metas</h2>
  <ol>
    <li>Aprender HTML</li>
    <li>Dominar CSS</li>
    <li>Publicar mi perfil</li>
  </ol>
  ```
  Presionar **Run**.
- **[En pantalla]**: Comparación visual: `<ul>` = puntos (viñetas) | `<ol>` = números `1, 2, 3` | `<li>` = cada ítem.
- **[Narración en off]**:
  > "Ahora organicemos ideas con listas. Si el orden no importa, usamos `<ul>` (*unordered list*), que pone puntitos o viñetas. Si el orden sí importa, como un Top 3 o una receta, usamos `<ol>` (*ordered list*), que numera automáticamente cada elemento. Dentro de cualquiera de las dos, cada ítem va envuelto en una etiqueta `<li>`. Presionamos **Run** y mira qué limpio queda."

## [03:45 - 04:30] Pausa interactiva
- **[En pantalla]**: Recuadro: *"Pausa el video — Añade un nuevo `<li>` a tu lista y cambia el `width` de la imagen a `180`"*.
- **[Narración en off]**:
  > "Pausa el video y pruébalo en JSFiddle: agrega un cuarto pasatiempo dentro de la etiqueta `<ul>` usando `<li>` y cambia el tamaño de la imagen modificando el atributo `width`."

## [04:30 - 05:00] Cierre
- **[En pantalla]**: Resumen: `<img>` (`src`, `alt`) | `<ul>` + `<li>` | `<ol>` + `<li>`.
- **[Narración en off]**:
  > "¡Genial! Ya tienes todas las piezas esenciales de HTML. Pero todo sigue viéndose en blanco y negro con letra básica... ¡Es hora de darle estilo! En la Lección 5 entramos al mundo de **CSS**."

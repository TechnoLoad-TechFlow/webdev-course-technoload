# Guion Lección 3: Atributos y enlaces: conectando páginas web

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 1
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-03/` y `completed-examples/lesson-03/`

---

## [00:00 - 00:40] Introducción
- **[En pantalla]**: Título: *"Lección 3: Atributos y Enlaces (`<a>`)"*.
- **[Narración en off]**:
  > "¡Hola de nuevo! La palabra 'web' significa red, y lo que convierte a páginas sueltas en una red gigante son los **enlaces** o links. Hoy vas a aprender qué es un **atributo** en HTML y cómo crear enlaces a tus sitios favoritos."

## [00:40 - 01:50] ¿Qué es un atributo HTML?
- **[En pantalla]**: Resaltado de código:
  `<a href="https://es.wikipedia.org">Ir a Wikipedia</a>`
  Flecha hacia `href="..."` con el texto: *"Atributo = información extra dentro de la etiqueta de apertura"*.
- **[Narración en off]**:
  > "Para hacer un enlace usamos la etiqueta `<a>`, que viene de *anchor* o ancla. Pero si solo escribimos `<a>Ir a Wikipedia</a>`, el navegador no sabe a qué dirección llevarnos. Ahí entran los **atributos**. Un atributo es un dato extra que va siempre dentro de la etiqueta de apertura, con la forma `nombre="valor"`. En los enlaces, el atributo obligatorio es `href`, donde pegamos la dirección web completa."

## [01:50 - 03:35] Creando enlaces y `target="_blank"` en JSFiddle
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-03/` y agregar dos enlaces:
  ```html
  <p>
    Mi enciclopedia favorita es
    <a href="https://es.wikipedia.org" target="_blank">Wikipedia</a>.
  </p>
  <p>
    También puedes aprender más en
    <a href="https://developer.mozilla.org/es/" target="_blank">MDN Web Docs</a>.
  </p>
  ```
  Presionar **Run** y mostrar cómo el texto aparece azul y subrayado.
- **[En pantalla]**: Anotación sobre `target="_blank"`: *"Abre el enlace en una pestaña nueva"*.
- **[Narración en off]**:
  > "Probémoslo en JSFiddle. Dentro de un párrafo escribimos `<a href="https://es.wikipedia.org">Wikipedia</a>`. Al presionar **Run**, ¡mira!, el texto se volvió azul y subrayado. Un truco muy útil: si agregamos un segundo atributo llamado `target="_blank"`, al hacer clic el enlace se abrirá en una pestaña nueva sin cerrar nuestra página. Recuerda siempre poner las comillas `""` alrededor del valor de cada atributo."

## [03:35 - 04:30] Pausa interactiva
- **[En pantalla]**: Recuadro: *"Pausa el video — Agrega un enlace a tu página de música, deportes o ciencia favorita usando `href` y `target="_blank"`"*.
- **[Narración en off]**:
  > "Tu turno: pausa el video y en tu JSFiddle agrega un nuevo párrafo con un enlace hacia un sitio que visites seguido. Verifica que empiece con `https://` y que tenga `target="_blank"`."

## [04:30 - 05:00] Cierre
- **[En pantalla]**: Resumen: `<a href="URL" target="_blank">Texto</a>`.
- **[Narración en off]**:
  > "¡Súper bien! Ya sabes usar etiquetas y atributos. En la próxima lección le vamos a dar vida visual a nuestra página agregando imágenes y listas ordenadas. ¡Nos vemos en la Lección 4!"

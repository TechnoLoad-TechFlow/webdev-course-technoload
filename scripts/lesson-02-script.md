# Guion Lección 2: Tu primera página HTML: etiquetas y estructura básica

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 1
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-02/` y `completed-examples/lesson-02/`

---

## [00:00 - 00:40] Bienvenida y objetivo
- **[En pantalla]**: Título: *"Lección 2: Etiquetas y Estructura HTML"*.
- **[Narración en off]**:
  > "¡Bienvenido a la Lección 2! En el video anterior vimos que HTML es el esqueleto de cualquier sitio web. Hoy vas a aprender el secreto detrás de esas palabras raras entre símbolos de menor y mayor que, y vas a escribir tu primera página HTML desde cero."

## [00:40 - 01:55] ¿Qué es una etiqueta HTML?
- **[En pantalla]**: Anatomía visual de un elemento:
  `<p>` (etiqueta de apertura) + `Hola` (contenido) + `</p>` (etiqueta de cierre) = **Elemento HTML**.
- **[Narración en off]**:
  > "En HTML todo funciona con **etiquetas**. Una etiqueta es como una cajita con nombre que le dice al navegador qué tipo de contenido estás poniendo. Casi todas las etiquetas vienen en pareja: una etiqueta para abrir, por ejemplo `<p>`, luego el texto que quieres mostrar, y al final una etiqueta para cerrar, `</p>`, que lleva una barra diagonal `/` antes del nombre. Esa barra es como decirle al navegador: 'aquí termina este párrafo'."

## [01:55 - 03:30] Escribiendo encabezados y párrafos en JSFiddle
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-02/` (panel HTML vacío con comentario guía). Escribir paso a paso:
  ```html
  <h1>Mi Diario Digital</h1>
  <h2>Sobre mí</h2>
  <p>Hola, estoy aprendiendo a crear páginas web desde cero.</p>
  <h3>Mis metas</h3>
  <p>Quiero diseñar mi propio sitio web este mes.</p>
  ```
  Presionar **Run** después de `<h1>` y luego al completar todo.
- **[En pantalla]**: Anotación comparando `<h1>` (título principal más grande) vs `<h2>` y `<h3>` (subtítulos más pequeños).
- **[Narración en off]**:
  > "Vamos a JSFiddle. Escribamos nuestro título principal con `<h1>`, que viene de *heading 1*. Abrimos `<h1>`, escribimos `Mi Diario Digital` y cerramos con `</h1>`. Presionamos **Run** y ahí está, grande y en negrita. Ahora agreguemos un subtítulo más pequeño con `<h2>`: `Sobre mí`. Y debajo, un párrafo normal con `<p>`. Como ves, HTML tiene títulos desde `<h1>` hasta `<h6>`, siendo `<h1>` el más importante y grande. Nunca olvides cerrar cada etiqueta."

## [03:30 - 04:30] Reto práctico en pantalla
- **[En pantalla]**: Recuadro: *"Pausa el video — Crea un `<h1>` con tu película o juego favorito, un `<h2>` que diga '¿Por qué me gusta?' y un `<p>` explicándolo"*.
- **[Narración en off]**:
  > "Ahora es tu turno. Pausa el video, entra al enlace de JSFiddle en la descripción y crea una mini página sobre tu película, serie o videojuego favorito usando al menos un `<h1>`, un `<h2>` y dos párrafos `<p>`. Presiona **Run** para comprobar que todo se vea ordenado."

## [04:30 - 05:00] Cierre
- **[En pantalla]**: Resumen: `<h1>` a `<h6>` (títulos) | `<p>` (párrafos) | `</etiqueta>` (siempre cerrar).
- **[Narración en off]**:
  > "¡Excelente trabajo! Ya dominas la estructura básica de texto en HTML. Pero una página web sin enlaces sería como una isla sin puentes. En la Lección 3 aprenderás a conectar tu página con cualquier sitio de internet. ¡Nos vemos!"

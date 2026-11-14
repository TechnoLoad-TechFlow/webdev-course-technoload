# Guion Lección 8: Proyecto Final (Parte 1): Estructura HTML de tu página de perfil

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 3
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-08/` y `completed-examples/lesson-08/`

---

## [00:00 - 00:40] Introducción al proyecto
- **[En pantalla]**: Vista previa rápida de la tarjeta de perfil terminada (solo 3 segundos para motivar) y título: *"Lección 8: Tu Página de Perfil — Parte 1 (HTML)"*.
- **[Narración en off]**:
  > "¡Llegó el momento de juntar todo lo que aprendiste! En estas dos próximas lecciones vamos a construir esta página de perfil personal paso a paso. Hoy en la Parte 1 armaremos toda la estructura en **HTML**; en la Lección 9 la vestiremos con **CSS**."

## [00:40 - 02:15] Creando el contenedor y la cabecera del perfil
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-08/` (que incluye un enlace de imagen listo para usar). Escribir en el panel **HTML**:
  ```html
  <div class="tarjeta">
    <img class="avatar" src="https://api.dicebear.com/9.x/thumbs/svg?seed=Alex" alt="Avatar de perfil" width="120">
    <h1>Alex Rivera</h1>
    <p class="subtitulo">Estudiante de secundaria y futuro creador web</p>
  ```
  Presionar **Run**.
- **[En pantalla]**: Anotación señalando `<div class="tarjeta">` (*"Caja principal que agrupará todo el perfil"*).
- **[Narración en off]**:
  > "Empezamos en JSFiddle creando una caja principal con `<div class="tarjeta">`. Un `div` es un contenedor invisible que agrupa elementos para luego poder centrarlos o darles fondo juntos. Adentro ponemos nuestra imagen con `class="avatar"`, un `<h1>` con el nombre, y un párrafo `<p class="subtitulo">` que describe quiénes somos."

## [02:15 - 03:50] Agregando biografía, intereses y botón de enlace
- **[Acción en JSFiddle]**: Continuar dentro de `<div class="tarjeta">`:
  ```html
    <h2>Sobre mí</h2>
    <p>Me encanta la música, los videojuegos y aprender cómo funcionan los sitios web.</p>

    <h2>Mis intereses</h2>
    <ul class="lista-intereses">
      <li>Diseño web</li>
      <li>Fotografía</li>
      <li>Programación creativa</li>
    </ul>

    <a class="boton" href="https://developer.mozilla.org/es/" target="_blank">Mi recurso favorito</a>
  </div>
  ```
  Presionar **Run**.
- **[En pantalla]**: Flechas señalando cómo se cierra `</div>` al final de todo.
- **[Narración en off]**:
  > "Ahora añadimos una sección `Sobre mí` con `<h2>` y `<p>`. Luego una lista `<ul>` con `class="lista-intereses"` para tres pasatiempos. Y al final, un enlace `<a>` con `class="boton"` que luego convertiremos en un botón real con CSS. No olvides cerrar el `</div>` al final. Si presionamos **Run**, ya tenemos toda la información lista, aunque todavía sin estilo."

## [03:50 - 04:30] Pausa interactiva
- **[En pantalla]**: Recuadro: *"Pausa el video — Personaliza el nombre, el subtítulo, la biografía y los 3 intereses con tus propios gustos"*.
- **[Narración en off]**:
  > "Pausa el video y haz tuya esta página en JSFiddle: cambia el nombre por el tuyo o un apodo, escribe tu propia descripción y pon tres cosas que te apasionen en la lista."

## [04:30 - 05:00] Cierre
- **[En pantalla]**: Checklist: `✓ Contenedor .tarjeta`, `✓ Avatar + Títulos`, `✓ Lista + Enlace`.
- **[Narración en off]**:
  > "¡Estructura lista! En la Lección 9 viene la transformación más satisfactoria: convertir este HTML sencillo en una tarjeta moderna con CSS. ¡Nos vemos ahí!"

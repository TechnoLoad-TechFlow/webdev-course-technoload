# Guion Lección 2: Tu primera página HTML: etiquetas y estructura básica

- **Duración objetivo**: 5:00 a 5:20 minutos (ritmo pausado y explicativo)
- **Responsable sugerido**: Estudiante 1
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-02/` y `completed-examples/lesson-02/`

---

## [00:00 - 00:50] Bienvenida y el idioma de los navegadores
- **[En pantalla]**: Portada con título: *"Lección 2: Tu primera página HTML: etiquetas y estructura básica"*.
- **[Narración en off]**:
  > "¡Hola de nuevo y bienvenido a la Lección 2! En el video anterior descubrimos que HTML es la base sólida sobre la que se construye cualquier página de internet. Pero ahora nos toca responder a una gran pregunta: ¿cómo entiende la computadora lo que queremos escribir?
  > 
  > Cuando tú escribes una tarea en un procesador de textos como Word o Google Docs, para hacer un título más grande solo seleccionas el texto y haces clic en el botón de cambiar tamaño o negrita. Sin embargo, en el desarrollo web no existen esos botones. Nosotros le damos órdenes directas al navegador utilizando un lenguaje con reglas claras y precisas. Hoy vas a aprender a hablar ese idioma, entenderás qué son las etiquetas y cómo organizar títulos y párrafos con la jerarquía correcta."

---

## [00:50 - 02:05] Anatomía de una etiqueta: apertura, contenido y cierre
- **[En pantalla]**: Diagrama animado y visualmente descompuesto en 3 partes:
  ```html
  <p>Hola, mundo</p>
  ```
  - Flecha verde al primer `<p>`: *"Etiqueta de apertura (indica dónde empieza el elemento)"*
  - Flecha blanca al texto `Hola, mundo`: *"Contenido (lo que verá el usuario)"*
  - Flecha roja a `</p>` con zoom a la barra `/`: *"Etiqueta de cierre con diagonal (indica dónde termina)"*
- **[Narración en off]**:
  > "En HTML, todo contenido vive dentro de lo que llamamos **elementos**, y un elemento está compuesto principalmente por **etiquetas**.
  > 
  > Una etiqueta se escribe encerrando una palabra o letra clave entre dos símbolos: el signo de menor que `<` y el signo de mayor que `>`.
  > 
  > La gran mayoría de las etiquetas vienen en parejas, como dos sujetalibros:
  > Primero escribimos la **etiqueta de apertura**, por ejemplo `<p>`, que le avisa al navegador: '¡Atención, aquí comienza un párrafo de texto!'.
  > Después escribimos el **contenido**, que es el mensaje que queremos que la gente lea en la pantalla.
  > Y finalmente, es fundamental escribir la **etiqueta de cierre**, que es prácticamente igual a la de apertura pero con una barra diagonal `/` antes del nombre: `</p>`.
  > 
  > Esa barra diagonal es crucial: le dice al navegador exactamente dónde termina ese párrafo para que no aplique ese mismo formato a todo el resto de la página. Si olvidas cerrar una etiqueta, el navegador se confundirá y puede desordenar por completo el diseño."

---

## [02:05 - 03:20] Jerarquía de títulos: de `<h1>` a `<h6>` y el párrafo `<p>`
- **[En pantalla]**: Tabla visual mostrando la escala de encabezados:
  - `<h1>`: Título principal (solo uno por página o sección principal, el más grande e importante)
  - `<h2>`: Subtítulo principal (secciones de la página)
  - `<h3>`: Subsecciones o temas específicos
  - `<h4>`, `<h5>`, `<h6>`: Títulos menores para detalles
  - `<p>`: Párrafo de texto normal
- **[Narración en off]**:
  > "HTML tiene diferentes tipos de etiquetas para clasificar la información según su importancia. Esto se conoce como **jerarquía**.
  > 
  > Para los títulos existen seis niveles de encabezados: van desde `<h1>` hasta `<h6>`. La letra 'h' viene de la palabra en inglés *heading*, que significa encabezado o título.
  > 
  > `<h1>` es el título principal de la página, el más grande y llamativo de todos. Por buenas prácticas, se recomienda usar un solo `<h1>` por página, tal como un libro solo tiene un título en su portada.
  > 
  > Luego tenemos `<h2>` y `<h3>`, que funcionan como los capítulos y subtemas de tu contenido. Son un poco más pequeños pero siguen viéndose en negrita para organizar la lectura. Y si seguimos bajando, llegamos hasta `<h6>`, que es el título más pequeño.
  > 
  > Y para todo el texto común y corriente —como explicaciones, historias o artículos— usamos la etiqueta `<p>`, que viene de *paragraph*.
  > 
  > Un dato curioso para principiantes: en HTML, si presionas la tecla Enter cinco veces entre dos palabras, el navegador ignorará todos esos espacios en blanco. Para separar ideas en párrafos distintos, la única forma correcta es envolver cada párrafo dentro de sus propias etiquetas `<p>` y `</p>`."

---

## [03:20 - 04:20] Manos a la obra en JSFiddle: escribiendo tu primer diario digital
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-02/`.
  1. En el panel HTML, borrar el comentario y escribir en vivo a ritmo pausado:
     ```html
     <h1>Mi Diario Digital</h1>
     ```
  2. Presionar **Run** y mostrar cómo aparece el título grande.
  3. Continuar escribiendo:
     ```html
     <h2>Sobre mí</h2>
     <p>Hola, estoy aprendiendo a crear páginas web desde cero.</p>
     ```
  4. Presionar **Run** para mostrar la diferencia de tamaño entre el título `h1`, el subtítulo `h2` y el texto regular `<p>`.
  5. Agregar una subsección con `<h3>`:
     ```html
     <h3>Mis metas</h3>
     <p>Quiero diseñar mi propio sitio web este mes.</p>
     ```
  6. Demostración rápida del error común: borrar la barra diagonal de `</p>` o dejar un `<h2>` abierto, presionar **Run** para que el alumno vea cómo el texto siguiente se vuelve grande por error, y volver a colocar la barra de cierre correctamente.
- **[En pantalla]**: Anotaciones en pantalla resaltando cada etiqueta mientras se escribe.
- **[Narración en off]**:
  > "Vamos a poner todo esto en práctica en nuestro JSFiddle. Abre el enlace que está en la descripción de este video.
  > 
  > En el panel de HTML, vamos a construir una pequeña página para un diario personal.
  > Primero abrimos la etiqueta `<h1>`, escribimos `Mi Diario Digital` y cerramos con `</h1>`. Si hacemos clic en **Run**, ¡ahí está nuestro título principal, grande y con peso!
  > 
  > Justo debajo, queremos una sección que hable sobre nosotros, así que usamos un encabezado de segundo nivel: abrimos `<h2>`, ponemos `Sobre mí` y cerramos con `</h2>`.
  > Para contar nuestra historia usamos un párrafo: abrimos `<p>`, escribimos `Hola, estoy aprendiendo a crear páginas web desde cero`, y cerramos con `</p>`. Presionamos **Run** y observa qué bien se lee: el título guía la vista y el párrafo presenta la información con claridad.
  > 
  > Ahora añadamos una subsección con `<h3>`: `Mis metas`, y otro `<p>` que diga `Quiero diseñar mi propio sitio web este mes`.
  > 
  > Fíjate en lo que ocurre si por descuido olvido la barra diagonal al cerrar el `h2`... Presiono **Run** y... ¡mira eso! El párrafo de abajo se volvió un título gigante porque el navegador cree que el título nunca terminó. Por eso es vital revisar que cada etiqueta abierta tenga su correspondiente etiqueta de cierre."

---

## [04:20 - 04:55] Pausa interactiva para la práctica
- **[En pantalla]**: Cartel animado:
  *"⏸️ TU RETO PRÁCTICO (Pausa el video durante 1 minuto):*
  *1. Abre tu JSFiddle.*
  *2. Crea un <h1> con el título de tu videojuego, película o serie favorita.*
  *3. Agrega un <h2> que diga '¿De qué trata?' y un párrafo <p> explicándolo.*
  *4. Agrega un <h3> que diga 'Mi personaje favorito' y otro <p> con su nombre.*
  *5. Presiona Run y verifica que ninguna etiqueta quede abierta."*
- **[Narración en off]**:
  > "Llegó el momento de tu reto práctico. Pausa este video un minuto y entra a tu JSFiddle. Crea una mini página sobre tu película, serie o videojuego favorito: usa un `<h1>` para el título principal, un `<h2>` para explicar de qué trata con un párrafo `<p>`, y un `<h3>` con tu personaje favorito. Asegúrate de cerrar todas tus etiquetas y presiona **Run** para comprobar el resultado."

---

## [04:55 - 05:20] Resumen y transición a la Lección 3
- **[En pantalla]**: Resumen con iconos:
  - `<etiqueta>` y `</etiqueta>`: Siempre en pareja (no olvides la barra `/`).
  - `<h1>` a `<h6>`: Títulos ordenados de mayor a menor importancia.
  - `<p>`: El contenedor de texto para párrafos limpios.
- **[Narración en off]**:
  > "¡Excelente trabajo! Has aprendido a estructurar texto con significado y jerarquía en HTML, la misma técnica que usan los redactores de noticias y los blogs profesionales en todo el mundo.
  > 
  > Pero hasta ahora, nuestra página es como una hoja de papel aislada del resto del mundo. ¿Cómo hacemos para que el usuario pueda hacer clic en una palabra y viajar a otra página web?
  > 
  > En la Lección 3 descubriremos los **atributos** y aprenderemos a crear **enlaces interactivos** con la etiqueta `<a>`. ¡Te espero en el próximo video!"

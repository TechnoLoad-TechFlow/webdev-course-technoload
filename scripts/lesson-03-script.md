# Guion Lección 3: Atributos y enlaces: conectando páginas web

- **Duración objetivo**: 5:00 a 5:20 minutos (ritmo pausado y demostrativo)
- **Responsable sugerido**: Estudiante 1
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-03/` y `completed-examples/lesson-03/`

---

## [00:00 - 00:50] Introducción: la magia detrás de la 'Telaraña Mundial'
- **[En pantalla]**: Portada con título: *"Lección 3: Atributos y Enlaces en HTML (`<a>`)"*. Debajo: *"Conectando tu página con el resto de internet"*.
- **[Narración en off]**:
  > "¡Hola de nuevo y bienvenido a la Lección 3! ¿Alguna vez te has preguntado por qué a internet la llamamos la 'web' o telaraña mundial? En los primeros años de las computadoras, los documentos digitales estaban completamente aislados: leías un archivo y para consultar otro tenías que buscarlo manualmente.
  > 
  > Todo cambió a principios de los años 90, cuando los científicos inventaron una idea revolucionaria: los **hipervínculos** o enlaces. La posibilidad de hacer clic en una palabra y viajar al instante a otra página en cualquier rincón del planeta es lo que transformó a internet en una red viva y conectada.
  > 
  > Hoy vas a aprender a crear tus propios enlaces y, de paso, vas a dominar uno de los conceptos más importantes de todo el desarrollo web: los **atributos HTML**."

---

## [00:50 - 02:05] ¿Qué es un atributo HTML? La anatomía de una etiqueta con superpoderes
- **[En pantalla]**: Diagrama visual con lupa apuntando a la etiqueta de apertura:
  ```html
  <a href="https://es.wikipedia.org" target="_blank">Ir a Wikipedia</a>
  ```
  - Recuadro resaltando: `href="https://es.wikipedia.org"` -> *"Atributo 1: Destino del enlace"*
  - Recuadro resaltando: `target="_blank"` -> *"Atributo 2: Abrir en pestaña nueva"*
  - Flecha indicando: *"Los atributos SIEMPRE van dentro de la etiqueta de apertura, separados por un espacio"*
- **[Narración en off]**:
  > "Para crear un enlace en HTML usamos la etiqueta `<a>`, que viene de la palabra en inglés *anchor*, que significa ancla, porque ancla o conecta dos documentos entre sí.
  > 
  > Pero pensemos en algo lógico: si solo escribimos `<a>Ir a Wikipedia</a>`, el navegador sabe que queremos un enlace, pero... ¿hacia dónde debe dirigir al usuario? ¡No tiene forma de adivinarlo!
  > 
  > Para resolver esto, HTML inventó los **atributos**.
  > Imagina los atributos como las características o 'superpoderes' que le asignas a una etiqueta para personalizar su comportamiento.
  > 
  > Los atributos tienen tres reglas de oro que nunca debes olvidar:
  > Primero: **siempre van dentro de la etiqueta de apertura**, justo después del nombre de la etiqueta y separados por un espacio. Nunca los coloques en la etiqueta de cierre.
  > Segundo: se escriben con el formato **nombre del atributo, signo de igual, y el valor entre comillas dobles**: `nombre="valor"`.
  > Y tercero: en la etiqueta `<a>`, el atributo indispensable se llama **`href`**, que significa *Hypertext Reference* o referencia de hipertexto. En el valor de `href` pegamos la dirección web completa a la que queremos llegar."

---

## [02:05 - 03:20] Enlaces en acción y el truco de `target="_blank"` en JSFiddle
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-03/`.
  1. En el panel HTML escribir:
     ```html
     <h1>Mis sitios favoritos</h1>
     <p>
       Mi enciclopedia favorita es
       <a href="https://es.wikipedia.org">Wikipedia</a>.
     </p>
     ```
  2. Presionar **Run**. Mostrar cómo la palabra "Wikipedia" aparece subrayada y de color azul en el panel Result.
  3. Explicar el comportamiento por defecto: si haces clic, la página actual se reemplaza.
  4. Agregar el segundo atributo: `target="_blank"`.
     ```html
     <p>
       Mi enciclopedia favorita es
       <a href="https://es.wikipedia.org" target="_blank">Wikipedia</a>.
     </p>
     ```
  5. Agregar un segundo párrafo con otro enlace de gran utilidad:
     ```html
     <p>
       También puedes aprender más en
       <a href="https://developer.mozilla.org/es/" target="_blank">MDN Web Docs</a>.
     </p>
     ```
  6. Presionar **Run** y verificar ambos enlaces.
- **[En pantalla]**: Anotación destacada: *"`target="_blank"` = Abre el enlace en una pestaña nueva para que el visitante no abandone tu sitio"*.
- **[Narración en off]**:
  > "Vamos a comprobarlo en JSFiddle. Abre el enlace que dejamos en la descripción de este video.
  > 
  > Tenemos un título que dice `<h1>Mis sitios favoritos</h1>`. Ahora escribamos un párrafo normal: `Mi enciclopedia favorita es `.
  > Justo después abrimos nuestra etiqueta `<a>`. Dejamos un espacio y escribimos `href="https://es.wikipedia.org"`. Cerramos el símbolo mayor que `>`, escribimos el texto visible que será `Wikipedia`, y cerramos con `</a>`.
  > 
  > Al presionar el botón **Run**, observa con atención el panel Result: la palabra 'Wikipedia' se convirtió en un enlace azul y con una línea debajo. Al pasar el cursor por encima, el puntero se transforma en una manito lista para hacer clic.
  > 
  > Pero aquí hay un detalle importante: si el usuario hace clic, abandonará nuestra página. ¿Cómo logramos que el enlace se abra en una pestaña nueva sin cerrar nuestra web?
  > Agregamos un segundo atributo dentro de la misma etiqueta de apertura: dejamos un espacio y escribimos `target="_blank"`.
  > 
  > Añadamos también un segundo enlace hacia **MDN Web Docs**, que es la biblioteca oficial de documentación web más consultada por los desarrolladores profesionales en todo el mundo. Presionamos **Run**... ¡y ahora tenemos dos enlaces perfectamente integrados en nuestras oraciones!"

---

## [03:20 - 04:20] Errores comunes al crear enlaces: ¿qué pasa si algo sale mal?
- **[Acción en JSFiddle]**:
  1. Mostrar el error 1: olvidar escribir `https://` y poner solo `href="wikipedia.org"`. Presionar **Run** y explicar que el navegador pensará que es un archivo interno de tu computadora y dará un error 404.
  2. Mostrar el error 2: olvidar las comillas dobles `""` en el valor del atributo: `href=https://es.wikipedia.org`.
  3. Corregir ambos errores en pantalla para que el código quede impecable.
- **[En pantalla]**: Comparación visual en pantalla:
  - `❌ href="wikipedia.org"` -> Falta el protocolo `https://`.
  - `❌ href=https://...` -> Faltan las comillas dobles.
  - `✅ href="https://es.wikipedia.org"` -> Enlace completo y seguro.
- **[Narración en off]**:
  > "Antes de pasar a tu práctica, déjame advertirte sobre dos errores súper comunes que frustran a casi todos los principiantes:
  > 
  > El primer error es **olvidar el `https://` al inicio de la dirección**. Si escribes únicamente `wikipedia.org` a secas, el navegador no sabrá que te refieres a un sitio externo en internet y buscará una carpeta dentro de tu propio proyecto, causando que el enlace no funcione. Siempre incluye la dirección web completa, con su protocolo `https://`.
  > 
  > El segundo error es **olvidar las comillas dobles**. Aunque en algunos casos el navegador intente adivinarlo, si tu dirección tiene caracteres especiales o espacios, sin comillas todo se romperá.
  > Acostúmbrate desde hoy a la buena práctica: `href="https://..."`."

---

## [04:20 - 04:55] Pausa interactiva para la práctica
- **[En pantalla]**: Cartel animado:
  *"⏸️ TU RETO PRÁCTICO (Pausa el video durante 1 minuto):*
  *1. Entra a tu JSFiddle.*
  *2. Agrega un tercer párrafo recomendando tu plataforma de música, videos o juegos favorita.*
  *3. Envuelve el nombre de la plataforma en una etiqueta <a> con su dirección completa (con https://).*
  *4. Asegúrate de incluir target="_blank" para que abra en una nueva pestaña.*
  *5. Presiona Run y pruébalo con un clic."*
- **[Narración en off]**:
  > "Es momento de poner a prueba lo que aprendiste. Pausa este video durante un minuto, entra a tu JSFiddle y agrega un tercer párrafo donde menciones tu sitio web o plataforma favorita: puede ser Spotify, YouTube, la NASA o tu juego favorito. Envuelve el nombre en una etiqueta `<a>`, escribe su dirección completa con `https://`, agrégale `target="_blank"` y presiona **Run** para comprobar que funcione a la perfección."

---

## [04:55 - 05:20] Resumen y avance de la Lección 4
- **[En pantalla]**: Resumen final:
  - Atributo = `nombre="valor"` dentro de la etiqueta de apertura `<etiqueta ...>`.
  - Enlaces = `<a href="https://..." target="_blank">Texto</a>`.
- **[Narración en off]**:
  > "¡Excelente trabajo! Hoy diste un paso gigantesco: tu página web ya no está aislada, ahora forma parte de la red mundial gracias a tus enlaces.
  > 
  > Ya dominas títulos, párrafos y enlaces. Pero un sitio web moderno necesita verse atractivo y organizado visualmente.
  > 
  > En la Lección 4 vamos a aprender a insertar **imágenes** con la etiqueta `<img>` y a organizar información paso a paso usando **listas numeradas y con viñetas** con las etiquetas `<ul>` y `<ol>`. ¡Nos vemos en el siguiente video!"

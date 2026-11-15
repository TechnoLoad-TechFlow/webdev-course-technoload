# Guion Lección 1: ¿Qué es el desarrollo web? Tu primer vistazo a JSFiddle

- **Duración objetivo**: 5:00 a 5:15 minutos (ritmo pausado y claro)
- **Responsable sugerido**: Estudiante 1
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-01/` y `completed-examples/lesson-01/`

---

## [00:00 - 00:50] Introducción y el misterio detrás de la pantalla
- **[En pantalla]**: Portada con título grande: *"Lección 1: ¿Qué es un sitio web?"*. Debajo: *"Curso de desarrollo web para principiantes"*.
- **[Narración en off]**:
  > "¡Hola y bienvenido a tu primer paso en el mundo de la programación web! Seguro que todos los días usas internet: entras a ver videos en YouTube, buscas información en Wikipedia, revisas redes sociales o juegas en línea. Pero... ¿alguna vez te has detenido a pensar qué hay realmente detrás de esa pantalla? ¿Cómo hace tu computadora o tu celular para saber dónde colocar un botón, cómo mostrar una imagen o por qué un texto aparece en color azul?
  > 
  > Lo increíble es que todas esas páginas, desde las más sencillas hasta las más populares del planeta, están construidas con código. Y hoy vas a descubrir que aprender a crearlas no es un secreto reservado para genios de la informática, sino una habilidad creativa que cualquiera puede aprender. Lo mejor de todo es que no necesitas descargar programas pesados ni tener una computadora avanzada: todo lo que necesitas ya lo tienes abierto frente a ti, y es tu navegador web."

---

## [00:50 - 02:05] ¿Cómo funciona la web? El navegador y la analogía de la casa
- **[En pantalla]**: Ilustración animada o diagrama visual:
  1. Iconos de navegadores (Chrome, Firefox, Safari, Edge) recibiendo archivos de texto plano.
  2. Dos columnas comparativas:
     - **HTML**: Los ladrillos, vigas y tuberías (Estructura y Contenido).
     - **CSS**: La pintura de las paredes, ventanas decoradas y muebles (Estilo y Apariencia).
- **[Narración en off]**:
  > "Para entender cómo funciona un sitio web, primero debemos conocer a nuestro mejor amigo: el **navegador web**, como Google Chrome, Mozilla Firefox, Microsoft Edge o Safari. Cuando tú entras a una dirección web, el navegador no recibe una imagen estática ni un video de la página; lo que recibe son archivos de texto con instrucciones escritas en dos lenguajes esenciales: **HTML** y **CSS**. El navegador funciona como un traductor súper veloz que lee esas líneas de texto y las transforma en la página visual e interactiva que tú ves en pantalla.
  > 
  > Para recordar la diferencia entre ambos lenguajes, usemos una analogía muy famosa: **la construcción de una casa**.
  > 
  > **HTML** son los cimientos, las columnas, los ladrillos y las divisiones de las habitaciones. HTML decide *qué elementos existen* en la página: 'aquí va un título principal', 'aquí va un párrafo de texto', 'aquí colocamos una fotografía' y 'aquí un botón'. Sin HTML, simplemente no hay nada que mostrar.
  > 
  > Pero una casa hecha solo de ladrillos grises sería fría y poco atractiva, ¿verdad? Ahí es donde entra **CSS**. CSS es el diseñador de interiores: elige el color de la pintura de las paredes, el tipo de letra, el tamaño de las fotos, los bordes redondeados y la posición de cada mueble en la habitación. Con HTML defines el contenido; con CSS defines cómo se ve."

---

## [02:05 - 03:20] Conociendo nuestro laboratorio: JSFiddle en vivo
- **[Acción en JSFiddle]**: Abrir en el navegador el enlace del Fiddle precargado (`starter-files/lesson-01/`). Zoom al 125% o 150%.
- **[En pantalla]**: Flechas y recuadros de color resaltando las 4 secciones:
  - Arriba izquierda: **HTML**
  - Abajo izquierda: **CSS**
  - Arriba derecha: **JavaScript** (con una nota: *"No lo usaremos en este curso básico"*)
  - Abajo derecha: **Result** (donde cobra vida la web)
  - Botón superior: **Run**
- **[Narración en off]**:
  > "Muchos cursos te piden instalar programas complicados en tu computadora, pero en este curso queremos que te concentres al cien por ciento en aprender y divertirte. Por eso vamos a utilizar **JSFiddle**, un editor de código en línea totalmente gratuito que funciona directo en tu navegador, sin necesidad de instalar nada y sin necesidad de crear una cuenta para empezar.
  > 
  > En la descripción de este video encontrarás el enlace directo para abrir exactamente la pantalla que estoy mostrando ahora mismo.
  > 
  > Observemos la pantalla juntos. JSFiddle divide tu espacio de trabajo en cuatro paneles principales:
  > En la esquina superior izquierda tenemos el panel de **HTML**, donde escribiremos la estructura y los textos.
  > Justo debajo, en la esquina inferior izquierda, está el panel de **CSS**, donde daremos estilo y color.
  > En la parte superior derecha hay un panel de **JavaScript**; este lenguaje se utiliza para programar funciones lógicas avanzadas, pero por ahora no lo tocaremos.
  > Y en el panel restante, llamado **Result**, es donde ocurre la magia: aquí veremos nuestra página web exactamente igual a como la vería cualquier persona en internet.
  > Arriba a la izquierda verás un botón azul que dice **Run**. Cada vez que hagamos un cambio en el código y presionemos ese botón, la ventana Result se actualizará de inmediato."

---

## [03:20 - 04:20] Nuestra primera prueba en vivo: modificando texto y estilo
- **[Acción en JSFiddle]**:
  1. Mostrar el código existente:
     - HTML: `<h1>¡Hola, mundo web!</h1>` y `<p>Esta es mi primera página en JSFiddle.</p>`
     - CSS: `h1 { color: #2563eb; }`
  2. Presionar **Run** para que se vea el título azul en el panel Result.
  3. Modificar en HTML: cambiar `¡Hola, mundo web!` por `¡Bienvenidos a mi espacio digital!`.
  4. Presionar **Run** y señalar el cambio.
  5. Modificar en CSS: cambiar `#2563eb` por `#16a34a` (verde) o escribir directamente `darkorange`.
  6. Presionar **Run** nuevamente.
- **[En pantalla]**: Texto resaltado: *"1. Edita el texto en HTML -> 2. Cambia el color en CSS -> 3. Presiona Run"*.
- **[Narración en off]**:
  > "Fíjate en lo que ya tenemos preparado. En el panel de HTML tenemos dos líneas: una etiqueta llamada `<h1>`, que contiene la frase `¡Hola, mundo web!`, y una etiqueta `<p>` con una pequeña descripción. En el panel CSS tenemos una regla que dice que ese `h1` debe pintarse de color azul.
  > 
  > Si presiono el botón **Run**, observa la ventana de Result: el título aparece grande, en negrita y de color azul.
  > 
  > Ahora hagamos algo emocionante. Voy a cambiar el texto del `<h1>` y voy a escribir: `¡Bienvenidos a mi espacio digital!`. Ahora presiono **Run**... ¡y el texto cambia al instante!
  > 
  > ¿Y qué pasa si quiero cambiar el color? Me voy al panel de CSS, busco la propiedad `color` y en lugar del código azul voy a escribir `darkorange` o `purple`. Presiono **Run** nuevamente... ¡y mira eso! El título ahora es anaranjado brillante. Con solo dos cambios de texto ya modificamos por completo el aspecto de la página."

---

## [04:20 - 04:55] Pausa interactiva para la práctica
- **[En pantalla]**: Cartel animado:
  *"⏸️ TU TURNO: Pausa el video durante 1 minuto*
  *1. Abre el enlace de JSFiddle en la descripción del video.*
  *2. Cambia el título por tu nombre o tu frase favorita.*
  *3. Elige un color en CSS: red, green, crimson, o tu favorito.*
  *4. Presiona el botón Run."*
- **[Narración en off]**:
  > "Ahora te toca a ti ensuciarte las manos con código. Haz clic en el enlace de JSFiddle que dejé en la descripción, pausa este video durante un minuto, cambia el título para que tenga tu nombre o tu frase favorita, prueba con un color nuevo en CSS como `crimson`, `navy` o `teal`, y presiona **Run** para ver el resultado. Cuando lo hayas probado, dale play al video para continuar."

---

## [04:55 - 05:20] Resumen, recomendaciones y cierre
- **[En pantalla]**: Tarjeta resumen con 3 puntos clave:
  - `✓ HTML` = Estructura y contenido (ladrillos).
  - `✓ CSS` = Diseño y colores (decoración).
  - `✓ JSFiddle` = Tu herramienta 100 % en línea sin descargas.
- **[Narración en off]**:
  > "¡Excelente trabajo! Si lograste ver tu cambio en pantalla, acabas de escribir y ejecutar tu primera línea de código web.
  > 
  > Recuerda siempre los dos conceptos clave de hoy: HTML construye la estructura y el contenido, mientras que CSS se encarga del diseño visual y los estilos.
  > 
  > En la siguiente lección vamos a adentrarnos de lleno en HTML. Aprenderás qué significan exactamente esos símbolos de menor y mayor que, cuáles son las etiquetas principales para organizar títulos y párrafos, y el error más común que cometen todos los principiantes al escribir texto. ¡Nos vemos en la Lección 2!"

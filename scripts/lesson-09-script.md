# Guion Lección 9: Proyecto Final (Parte 2): Estilizando tu página de perfil con CSS

- **Duración objetivo**: 5:00 minutos
- **Responsable sugerido**: Estudiante 4
- **Herramienta en línea**: [JSFiddle](https://jsfiddle.net/)
- **Archivos asociados**: `starter-files/lesson-09/` y `completed-examples/lesson-09/`

---

## [00:00 - 00:35] Introducción
- **[En pantalla]**: Título: *"Lección 9: Tu Página de Perfil — Parte 2 (CSS)"*.
- **[Narración en off]**:
  > "¡Bienvenido a la Parte 2 de nuestro proyecto! Ya tenemos todo el HTML de nuestra página de perfil. Hoy vamos a aplicarle CSS paso a paso para transformarla en una tarjeta moderna, limpia y lista para compartir."

## [00:35 - 02:10] Fondo de página y tarjeta centrada
- **[Acción en JSFiddle]**: Abrir `starter-files/lesson-09/` (ya trae el HTML completo de la Lección 8). Escribir en **CSS**:
  ```css
  body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: #e0f2fe;
    color: #1e293b;
    margin: 0;
    padding: 20px;
  }

  .tarjeta {
    background-color: #ffffff;
    max-width: 420px;
    margin: 30px auto;
    padding: 32px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  }
  ```
  Presionar **Run**.
- **[En pantalla]**: Anotación en `box-shadow`: *"Agrega una sombra suave para dar efecto de tarjeta flotante"*.
- **[Narración en off]**:
  > "Empecemos dando un fondo celeste suave al `body` y una letra limpia. Luego estilizamos `.tarjeta`: fondo blanco, ancho máximo de `420px`, `margin: 30px auto` para centrarla y `padding: 32px` para que respire. Le añadimos `border-radius: 16px` y un truco genial: `box-shadow`, que dibuja una sombra suave detrás de la tarjeta. Presionamos **Run** y ¡mira cómo cobra vida al instante!"

## [02:10 - 03:50] Avatar circular, lista limpia y botón
- **[Acción en JSFiddle]**: Agregar al **CSS**:
  ```css
  .avatar {
    border-radius: 50%;
    border: 4px solid #38bdf8;
    background-color: #f8fafc;
  }

  .subtitulo {
    color: #64748b;
    font-size: 15px;
  }

  .lista-intereses {
    list-style: none;
    padding: 0;
  }

  .lista-intereses li {
    background-color: #f1f5f9;
    margin: 8px 0;
    padding: 8px 12px;
    border-radius: 8px;
  }

  .boton {
    display: inline-block;
    margin-top: 16px;
    background-color: #0284c7;
    color: #ffffff;
    text-decoration: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-weight: bold;
  }
  ```
  Presionar **Run**.
- **[En pantalla]**: Resaltado en `border-radius: 50%` (*"Convierte cualquier imagen cuadrada en un círculo perfecto"*) y `text-decoration: none` (*"Quita el subrayado del enlace"*).
- **[Narración en off]**:
  > "Ahora hagamos la magia en los detalles. Para que la foto sea circular, usamos `border-radius: 50%` con un borde celeste. A `.lista-intereses` le quitamos los puntitos con `list-style: none` y convertimos cada `<li>` en una pequeña etiqueta gris redondeada. Y finalmente, a nuestro enlace `.boton` le quitamos el subrayado con `text-decoration: none`, le damos fondo azul, texto blanco y `padding` para que parezca un botón real. Presionamos **Run**... ¡y listo! Mira tu página de perfil terminada."

## [03:50 - 04:30] Pausa interactiva
- **[En pantalla]**: Recuadro: *"Pausa el video — Cambia los colores del fondo (`body`), del borde del avatar y del `.boton` por tu paleta favorita"*.
- **[Narración en off]**:
  > "Pausa el video y personaliza los colores en JSFiddle: prueba tonos morados, verdes o modo oscuro. Si haces clic en **Save** en JSFiddle, ¡obtendrás un enlace único para compartir tu creación con tus amigos!"

## [04:30 - 05:00] Cierre
- **[En pantalla]**: Mensaje: *"¡Proyecto completado! Siguiente: Lección 10 — Errores comunes y próximos pasos"*.
- **[Narración en off]**:
  > "¡Felicidades por terminar tu primer proyecto web completo! Antes de despedirnos, en la Lección 10 te voy a mostrar los 5 errores más comunes que comete todo principiante y cómo evitarlos para siempre."

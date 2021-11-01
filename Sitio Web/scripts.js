/**
 * Configuración de Canvas
 */
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
ctx.strokeStyle = "#000000";
ctx.lineWidth = 1;
var draw_pixels;

/**
 * Funciones Jquery
 */
$(document).ready(function () {
  /**
   * Función de limpiar
   */
  $("#clean").on("click", function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  });

  /**
   * Función de enviar
   * Envía un post con ajax hacia el puerto 8000.
   * Se envia 'pixeles', el cual es el arreglo convertido en cadena separada por comas.
   * Al regresar el resultado, lo pone en el div con id 'resultado'
   */
  $("#send").on("click", function () {
    $.post("http://localhost:8000", { pixeles: draw_pixels },
      function (response) {
        console.log("Resultado: " + response);
        $("#resultado").html("Resultdo: " + response);
      }
    );
  });
});

//mousedown, mouseup y mousemove: Eventos de canvas para dibujar segun el estado del mouse
var mousedown = false;

canvas.onmousedown = function (e) {
  var pos = fixPosition(e, canvas);
  // const context = canvas.getContext('2d');
  // context.clearRect(0, 0, canvas.width, canvas.height);
  mousedown = true;
  ctx.beginPath();
  ctx.moveTo(pos.x, pos.y);
  return false;
};

canvas.onmousemove = function (e) {
  var pos = fixPosition(e, canvas);
  if (mousedown) {
    ctx.lineTo(pos.x, pos.y);
    ctx.stroke();
  }
};

canvas.onmouseup = function (e) {
  mousedown = false;

  //Arreglo para almacenar los pixeles
  var pixels = [];
  for (var x = 0; x < 28; x++) {
    for (var y = 0; y < 28; y++) {
      var imgData = ctx.getImageData(y, x, 1, 1);
      var data = imgData.data;

      //Pixel negro o blanco?
      var color = (data[3]) / 255; //Data tiene 4 canales. Rojo, Verde, Azul, Alpha
      //Divido entre 255 para tener de 0 a 1

      //Dejar siempre 2 decimales
      color = (Math.round(color * 100) / 100).toFixed(2)
      pixels.push(color);
    }
  }

  console.log("Se ha dibujado", pixels);
  draw_pixels = pixels.join(",");
};

// Página ejemplo pintar en canvas
// http://jsfiddle.net/ghostoy/wTmFE/1/
function fixPosition(e, gCanvasElement) {
  var x;
  var y;
  if (e.pageX || e.pageY) {
    x = e.pageX;
    y = e.pageY;
  }
  else {
    x = e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
    y = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
  }
  x -= gCanvasElement.offsetLeft;
  y -= gCanvasElement.offsetTop;
  return { x: x, y: y };
}
function yukle() {
    var dosya = document.getElementById("dosya").files[0]
    if (!dosya) {
        alert("Lütfen bir dosya seçin.")
        return
    }
    if (dosya.type != "image/bmp") {
        alert("Lütfen BMP uzantılı bir dosya seçin.")
        return
    }
    var okuyucu = new FileReader()
    var yuklenenDosya
    okuyucu.onload = function (event) {
        yuklenenDosya = document.getElementById("resim")
        yuklenenDosya.src = event.target.result
        yuklenenDosya.style.display = "block"
    }
    okuyucu.readAsDataURL(dosya)

    // canvas açılır
    // document.getElementById("myCanvas").style.display = "block"
    document.getElementById("encode").style.display = "block"

    // img canvasa yükle
    setTimeout(function () {
        imgToCanvas()
    }, 100)
}

function imgToCanvas() {
    var canvas = document.getElementById("myCanvas")
    var context = canvas.getContext("2d")
    var img = document.getElementById("resim")
    // draw the image to canvas using drawImage.
    // Make image fit into canvas.
    context.drawImage(img, 0, 0, canvas.width, canvas.height)

    // Get the CanvasPixelArray from the given coordinates and dimensions.
    var imgd = context.getImageData(0, 0, context.width, context.height)
    var pix = imgd.data

    // Loop over each pixel and invert the color.
    for (var i = 0, n = pix.length; i < n; i += 4) {
        pix[i] = 255 - pix[i] // red
        pix[i + 1] = 255 - pix[i + 1] // green
        pix[i + 2] = 255 - pix[i + 2] // blue
        // i+3 is alpha (the fourth element)
    }
}

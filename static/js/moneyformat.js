var formatter = new Intl.NumberFormat('en-US', {


  });
var price =document.getElementById("gia")
var price1 = parseInt(price.dataset.price)
document.getElementById("gia").innerHTML="Giá: " +formatter.format(price1) +" VNĐ"

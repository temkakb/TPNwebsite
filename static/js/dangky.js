var input = document.getElementById("password");
input.addEventListener('keyup', function(){

if (input.value.length<8)
document.getElementById('password').setCustomValidity("mật khẩu trên 8 ký tự");
});
          
          	// Bổ sung hành động nữa
          


var updateBtns= document.getElementsByClassName('update-cart')
// lâý tất cả sản phẩm ở trang chủ or sản phẩm
var size = document.getElementsByClassName('get_sizevalue')
// lấy size ở trang chi tiết sp
var S=null
for (var i = 0; i<size.length;i++)
{
    size[i].addEventListener('click',function(){
        
        S = this.dataset.id
        // lấy size theo event mà khách hàng click
        //console.log('get size :',S) 
        
        
       // gán event click cho các size trong product detail
        
        
    }) 
}

for( var i = 0;i< updateBtns.length;i++)
{
    // gán event click ở tất cả các nút thêm vào giỏ hàng tại trang home và trang sp
    updateBtns[i].addEventListener('click',function(){
        var productId= this.dataset.product
        var action = this.dataset.action
        var size_delete = this.dataset.size
        // load dữ liệu
       
        console.log('productId:',productId,'action',action) // show ra console

        console.log('user: ',user)
        if(user ==='AnonymousUser'){
            console.log('Chưa đăng nhập')
            alert("Mời bạn đăng nhập")
            return // check đăng nhập
        }
       
        else{
            if (this.dataset.detail) 
        // data-detail có dữ liệu là "YES" để check đang ở ngoài trang chi tiết 
            {
                if (confirm('Bạn có muốn chọn Size mặc định là S?')) {
                    // nếu ở ngoài trang chi tiết thì show bản yes no chọn size mặc định là s
                    S="S"
                    // nếu ng dùng đồng ý size S thì gắn S = "s"
                  }
                   else {
                    
                    return
                    // KHÔNG THÌ KHÔNG LÀM J CẢ
                  }
                
            }
           
                if (action=="remove")
                {
                    // nếu acction là remove thì xóa sp
                updateUserOrder(productId,action,size_delete)

                }
                else{
                   
                    
                    updateUserOrder(productId,action,S)
                    // ngược lại là thêm sản phẩm. với size đó
                    
                }
            
        
        }
    })
}

function updateUserOrder(productId,action,getsize){
    console.log('Item was added ') // show ra console thôi à hihii
    var url ='/dathang/updateItem/'
    //tạo biến url
    
    if (getsize) // nếu mà biến getszie có tức là mặc định là ngoài trang chi tiết là S, trong trang chi tiết thì người dùng chọn
    {// còn nếu getsize -> null tức là người dùng vào trang chi tiết xong rồi ấn mua hàng -> báo lỗi chưa chọn size
        // ngược lại gửi request tới url như trên với phần header phải là csrftoken django yêu cầu vậy.
        // phần body là chuỗi json mà ta sử lý ở server
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
           
            body:JSON.stringify({'productId': productId,'action':action,'Size':getsize})
        })
    
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('data:',data)
            location.reload()
        })
    
    }
    else{
        alert("bạn chưa chọn size")
}
}

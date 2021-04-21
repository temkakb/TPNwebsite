var get_quantity = document.getElementsByClassName("change-quantity") //lay du lieu

    for (var i = 0; i<get_quantity.length;i++){
    get_quantity[i].addEventListener('input', function(){
      
         var quantity=this.value
        
        var productID =this.dataset.product
       
        var action= this.dataset.action
       
        
        console.log('productId:',productID,'action',action,'quantity',quantity)
       
      
        
       
        quantity_change(productID,action,quantity)


    })
    
    
}
function quantity_change(productId,action,quantity){
    
    var url ='/dathang/updatequantity/'
    
 
        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,
            },
           
            body:JSON.stringify({'productId': productId,'action':action,'Quantity':quantity})
        })
    
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('data:',data)
           
        })
    
    
}

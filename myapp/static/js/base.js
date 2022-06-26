
// add to cart 
var btns = document.getElementsByClassName("addToCart");
for (let i = 0; i < btns.length; i++ ){
    btns[i].addEventListener('click' , function(e){

        let product_id = e.target.dataset.product
        let action = e.target.dataset.action
    
        if(user == 'AnonymousUser'){
            console.log('user not loged')

        } 
        else{

            addToCartItem(product_id , action)
        }


    });


}

function addToCartItem(p_id , action){
 const data = {product_id: p_id, action: action};
    debugger;
    let url = '/add-to-cart/'
    fetch(url, {
    method: 'POST', // or 'PUT'
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(data),
    })
    .then(response => response.json())

    .then(data => {
    console.log('Success:', data);

    })

    .catch((error) => {
    console.error( 'Error:', error);
    });
    
    }




    
$(document).ready(function (){
/*

$(document).on('click' , ".addToWishlist" ,  function(){
    var prod_id = $(this).attr('data-product');

}); */

$('.addToWishlist').click(function(e){
    var prod_id = e.target.dataset.product
    
    //ajax

    $.ajax({
        url : "/add-to-wishlist/",
        data : {
            product : prod_id

        },
        dataType : 'json' ,

        success : function(res){

            console.log(res);
        }



    });

    // endajax


});




}) 
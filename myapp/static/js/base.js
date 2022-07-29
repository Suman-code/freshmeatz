// address form collapse
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}











// add to cart 
var btns = document.getElementsByClassName("addToCart");
for (let i = 0; i < btns.length; i++ ){
    btns[i].addEventListener('click' , function(e){

        var product_id = this.dataset.product
        var action = this.dataset.action
       
  
            if(user == 'AnonymousUser'){
            console.log('user not loged')

        } 
        else{

            addToCartItem(product_id , action)
        }


    });


}



//add to cart
function addToCartItem(product_id , action){
 var data = {product_id : product_id, action : action};

    var url = '/add-to-cart/'
    fetch(url, {
    method: 'POST', // or 'PUT'
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify(data),
    })
    .then((response) => {
        return response.json() 
        
    })

    .then(data => {
    console.log('Success:', data);
        document.getElementById('cartcount').innerHTML = `<span>${data.cartQuantity}</span>`

    })
    .catch((error) => {
        console.error('Error:', error);
      });

   
    }

// Update cart quantity
/*
let inputfields = document.getElementsByTagName('input');
for(let i=0 ; i< length.inputfields; i++){
    inputfields[i].addEventListener('change' , updateQuantity)


}
function updateQuantity(e){
    debugger;
    let inputvalue = e.target.value

    let product = e.dataset.target.product
    
    let data = {'prduct_id' : product , 'input_val' : inputvalue}
    console.log(data)

    let url = '/update-cart-quantity/'

    fetch(url, {
        method : "POST",
        headers : {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body : body.JSON.stringify(data),
    })
    .then((response) => {
        return response.json()

    })

    .then(data => {
        console.log(data)

    })

    .catch((error) => {
        console.error('Error:', error);
      });
    }

*/

/*
let qtyBtns = document.getElementsByClassName('cart-item-quantity')
console.log(qtyBtns);
for(let i = 0; i < qtyBtns.length ; i++){
    qtyBtns[i].addEventListener('click' , updateCartQuantity)

}



function updateCartQuantity(){
    let product_id = this.dataset.product
    let itemValue = $('#quantity').val()
    console.log(product_id, itemValue)

    let data = {'product_id' : product_id , 'itemValue': itemValue}
    console.log(data)

    url = "/update-cart-quantity/"
    fetch(url, {
        method : 'POST',
        headers :{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

        },

        body : JSON.stringify(data),

        })
        .then((respose) => {
            return respose.json()


        })
        .then(data => {
            console.log('success' , data)

            document.getElementById('subtotal').innerHTML = `<h6>${data.subtotal}</h6>`
            document.getElementById('totalamount').innerHTML = `<span>${data.grandtotal}</span>`
           

        })
        .catch((error) => {
            console.error('Error:', error);
          });


}

*/



let savBtn =document.getElementById("saveBtn").addEventListener('click' , delievryAddress)
//savBtn.addEventListener('click' , delievryAddress)



//delivery address
function delievryAddress(e){
    //e.preventDefault()
    var first_name = $('#firstname').val();
    var last_name = $('#lastname').val();
    var email = $('#inputemail').val();
    var phone = $('#inputphone').val();
    var inputTextarea = $('#inputTextarea').val();
    var locality= $('#inputLocality').val();
    var city = $('#inputCity').val();
    var landmark = $('#inputLandmark').val();
    var state = $('#inputState').val();
    var pincode = $('#inputPincode').val();
    var addresstype = $('#addressType').val();

    if(first_name == ''){
        alert('Please enter First name');
    }else if(last_name == ""){
        alert('Please enter last name');
    }else if(email == ""){
        alert('Please enter email name')
    }else if(phone == ""){
        alert('Please enter phone number')
    }else if(inputTextarea == ""){
        alert('Please enter address details')
    }else if(locality == ""){
        alert('Please enter locality name')

    }else if(city == ""){
        alert('Please enter city name')
    }else if(landmark == ""){
        alert('Please enter landmark')
    }else if(state == ""){
        alert('Please enter state name')
    }else if(pincode == ""){
        alert('Please enter pincode')
    }else if(addresstype == ""){
        alert('Please enter your address type')
    } else{

    let data = {first_name : first_name , last_name:last_name, email:email , mobile_number : phone , address : inputTextarea,
        locality :locality , city:city, landmark:landmark, state : state , pincode:pincode, address_type :addresstype,
        };

    url = "/userprofileaddress/"
    fetch(url, {
        method : 'POST',
        headers :{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

        },

        body : JSON.stringify(data),

        })
        .then((respose) => {
            return respose.json()


        })
        .then(data => {
            //console.log('success' , data)
            if (data.status == 'Added address'){
                return data.user_data;
                $("form")[0].reset()
            }

      
           

        })
        .catch((error) => {
            console.error('Error:', error);
          });


}













// add to wishlist
    
$(document).ready(function (){

//add to wishlist

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



    })

    // endajax


});

// wishlist delete

    $('.wishlist-delete').click(function(e){
        e.preventDefault();
        product_id = $("#proud_id").val();
        //console.log(product_id);

        $.ajax({
            method : "GET",
            url : "/delete-wishlist-item/",
            data : {
                'product_id' : product_id, 


            },
            success: function(res){
                console.log(res.status);
                $('.wishdata').load(location.href + " .wishdata");
            }


        })


    
    });



// delete cart item

    $('.delete-cart-item').click(function (e){

        e.preventDefault();
        var product_id = $('.prod_id').val();
        console.log(product_id);

        //ajax

        $.ajax({
           
            url : "/delete-cart-item/",
            data : {
                'product_id' : product_id,
            },
            
            success: function(response){
                return response
            }

        })


        //ajax end

    });


// update cart quantity
// minus cart item

$('.minus-cart').click(function(e){
    let product_id = this.dataset.product
    let ele = this.parentNode.children[2]
    console.log(product_id, ele);

    //ajax
    $.ajax({
        type : 'GET',
        url : '/minus-cart-item/',
        data :{
            'product_id' : product_id
        

        },

        sucess : function(data){

            ele.innerText = data.quantity
            $('#cartItem').load(location.href  + " #cartItem");


        }    

    })

    //ajax end

});

// minus cart item

$('.plus-cart').click(function(e){
    let product_id = this.dataset.product
    let ele = this.parentNode.children[2]
    console.log(product_id, ele);

    //ajax
    $.ajax({
        type : 'GET',
        url : '/plus-cart-item/',
        data :{
            'product_id' : product_id
        

        },

        sucess : function(data){

            ele.innerText = data.quantity
        }
        
    })

    //ajax end

});


// delivery date picker
$('#datepicker').datepicker({

    dateFormat : "yy-mm-dd",
    maxDate : "2D",
    minDate: 0,
 
});

// end delivery date picker


// deleivery address
/*
$("#saveBtn").click(function(){
    var first_name = $('#firstname').val();
    var last_name = $('#lastname').val();
    var email = $('#inputemail').val();
    var phone = $('#inputphone').val();
    var inputTextarea = $('#inputTextarea').val();
    var locality= $('#inputLocality').val();
    var city = $('#inputCity').val();
    var landmark = $('#inputLandmark').val();
    var state = $('#inputState').val();
    var pincode = $('#inputPincode').val();
    var addresstype = $('#addresstype').val();
    let csr = $('input[name=csrfmiddlewaretoken]').val();


    if(first_name == ''){
        alert('Please enter First name');
    }else if(last_name == ""){
        alert('Please enter last name');
    }else if(email == ""){
        alert('Please enter email name')
    }else if(phone == ""){
        alert('Please enter phone number')
    }else if(inputTextarea == ""){
        alert('Please enter address details')
    }else if(locality == ""){
        alert('Please enter locality name')

    }else if(city == ""){
        alert('Please enter city name')
    }else if(landmark == ""){
        alert('Please enter landmark')
    }else if(state == ""){
        alert('Please enter state name')
    }else if(pincode == ""){
        alert('Please enter pincode')
    }else if(addresstype == ""){
        alert('Please enter your address type')
    } else{
        
        let mydata = {first_name : first_name , last_name:last_name, email:email , mobile_number : phone , address : inputTextarea,
                        locality :locality , city:city, landmark:landmark, state:state, pincode:pincode, address_type :addresstype,
                        csrfmiddlewaretoken : csrftoken};


    //ajax

        $.ajax({
            url : '/userprofileaddress/',
            method : "POST",
            data : JSON.stringify(mydata),
            dataType: 'json',
            async: true,
            contentType: 'application/json; charset=utf-8',

            success : function(data){
                console.log(data.status)

            },
            error: (error) => {
                console.log(error);
            }


           
            })
          

        



            // ajax end
        }

})











})

*/


// delievry time slot

function deliveryTime(ele){
    var btnValue = ele.innerText;
    console.log('btn' , btnValue)

}




var timeSlots = [
    { 'time_range' : '07:00 AM - 09:00AM' },
    { 'time_range' : '09:00 AM - 11:00 AM' },
    { 'time_range' : '11:00 AM - 01:00 PM' },
    { 'time_range' : '01:00 PM - 03:00 PM' },
    { 'time_range' : '03:00 PM - 05:00 PM' },
    { 'time_range' : '05:00 PM - 07:00 PM' },
    { 'time_range' : '07:00 PM - 09:00 PM' },
    
 
];


var currentTime = new Date().getHours();

var newSlot = timeSlots.filter(Slots => filterSlots(Slots))

function filterSlots(Slots) {
    var slot = Slots['time_range'];

    var startTime = slot.substring(0, slot.indexOf('-'));

    var isPM = startTime.toLocaleLowerCase().indexOf('pm');

    var time = parseInt(startTime);

    if (isPM > -1) {
        time += 12;
    }
    
    if ( time >= currentTime ) {
        return slot;
    }     
   
}

console.log('newSlot :>> ', newSlot);

// end the time delievery




})

}
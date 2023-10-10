var bcart= document.querySelector('#bcart');
var btotal= document.querySelector('#btotal');


function addBurger(bid){
    //get Name
    burgerId = '#bur' + bid;
    var name = document.querySelector(burgerId).innerHTML;
    // get pizza price
    var radio ='burger'+bid;
    var pri = document.getElementsByName(radio);
    var size,price;
    if (pri[0].checked){
        price = pri[0].value;
        size = 'M' ;
    }
    else {
        price = pri[1].value;
        size = 'L';
    }
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    orders[cartSize] = [name,size,price]
    localStorage.setItem('orders',JSON.stringify(orders));
    total = Number(total) + Number(price);
    localStorage.setItem('total',total);
    var cart = document.querySelector('#cart')
    cart.innerHTML=orders.length;

    btn = '<button class="del" onclick="removeBurger(' + cartSize + ')">x</button>';

    btotal.innerHTML = 'Total :' + total +'₹';
    bcart.innerHTML += '<li>' + name +' '+ size +' : '+ price +' ₹' + btn +' </li>';
}
function bshoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    bcart.innerHTML = '';
    for (let i = 0; i < cartSize;i++)
    {
        btn = '<button class="del" onclick="removeBurger(' + i + ')" >x</button>';

        bcart.innerHTML += '<li>' + orders[i][0] +' '+ orders[i][1] +' : '+ orders[i][2] +' ₹' + btn +' </li>';

    }
    btotal.innerHTML = 'Total :' + total +'₹';


}
bshoppingCart();

function removeBurger(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total= Number(total)-Number(orders[n][2]);
    orders.splice(n,1);
    var cart = document.querySelector('#cart')
    cart.innerHTML=orders.length;
    localStorage.setItem('orders',JSON.stringify(orders));
    localStorage.setItem('total',total);
    bshoppingCart();
}
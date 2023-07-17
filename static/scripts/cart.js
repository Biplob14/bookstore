function cartItem(attr){
    var product_qty = $('#prod-qty').val();
    if (!product_qty) {
        product_qty = 1
    }
    console.log("element exist: " + $('#add-to-cart-btn').length)
    if($('#add-to-cart').length){
        product_id = $('#add-to-cart').val()
        request_url = $('#add-to-cart').data('url')
    } else if($('#add-to-cart-btn').length){
        request_url = $('#add-to-cart-btn').data('url')
        product_id = attr.value
    }
    console.log("product id: " + product_id)
    console.log("product qty: " + product_qty)
    $.ajax({
        type: 'POST',
        url: request_url,
        data: {
            productid: product_id,
            productqty: product_qty,
            csrfmiddlewaretoken: CSRF_TOKEN,
            action: 'post'
        },
        success: function(json) {
            console.log("quantity: ", json)
            document.getElementById("basket-qty").innerHTML = json.qty
        },
        error: function(xhr, errmsg, err) {}
    });
}
// $(document).on('click', '#add-to-cart', function(e){
//     console.log($('#prod-qty').val())

//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url: $('#add-to-cart').data('url'),
//         data: {
//             productid: $('#add-to-cart').val(),
//             productqty: $('#prod-qty').val(),
//             csrfmiddlewaretoken: CSRF_TOKEN,
//             action: 'post'
//         },
//         success: function(json) {
//             document.getElementById("basket-qty").innerHTML = json.qty
//         },
//         error: function(xhr, errmsg, err) {}
//     });
// })
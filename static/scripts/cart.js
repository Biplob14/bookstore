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
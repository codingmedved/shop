$(document).ready(function () {
    var form = $('#form_ordering_product')
    console.log(form)

    function basketUpdating(product_id, num, is_delete) {
        var data = {}
        data.product_id = product_id
        data.num = num
        var csrf_token = $('#form_ordering_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete) {
            data['is_delete'] = true
        }

        var url = form.attr('action')

        console.log(data)

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OKi")
                console.log(data.products_total_numb)
                if (data.products_total_numb || data.products_total_numb == 0) {
                    $('#cart_total_numb').text('(' + data.products_total_numb + ')')
                    console.log(data.products)
                    $('.cart-items ul').html('')
                    $.each(data.products, function (k, v) {
                        $('.cart-items ul').append('<li>' + v.name + '<br /> x ' + v.num + ' Total: ' + v.price_per_item * num + ' mon <a class="delete-item" data-product_id="' + v.id + '" href="">x</a></li>')
                    })
                }
            },
            error: function () {
                console.log("error")
            }
        })
    }

    form.on('submit', function (e) {
        e.preventDefault()
        console.log('123')
        var num = $('#number').val()
        console.log(num)
        var submit_btn = $('#submit_btn')
        var product_id = submit_btn.data('product-id')
        var product_name = submit_btn.data('product-name')
        var product_price = submit_btn.data('product-price')
        console.log(product_id, product_name, product_price * num)

        basketUpdating(product_id, num, is_delete = false)


        $('.cart-items ul').append('<li>' + product_name + '<br /> x ' + num + ' Total ' + product_price * num + ' mon</li>')
    })

    function showingCart() {
        $('.cart-items').removeClass('hidden')
    }

    // $('.cart-container').on('click', function (e) {
    //     e.preventDefault()
    //     showingCart()
    // })
    $('.cart-container').mouseover(function (e) {
        e.preventDefault()
        showingCart()
    })

    // $('.cart-container').mouseout(function () {
    //     showingCart()
    // })

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault()
        product_id = $(this).data('product_id')
        num = 0
        basketUpdating(product_id, num, is_delete = true)
    })

    function calculatingBasketAmount() {
        var total_order_amount = 0
        $('.total_product_price_in_cart').each(function () {
            total_order_amount += parseFloat($(this).text())
        })
        total_order_amount = total_order_amount.toFixed(2)
        $('#total_order_amount').text(total_order_amount)
    }

    $(document).on('change', '.product_number_in_cart', function () {
        var current_num = $(this).val()
        var current_tr = $(this).closest('tr')
        var current_price = parseFloat(current_tr.find('.product_price_in_cart').text())
        var total_price = (current_price * current_num).toFixed(2)
        current_tr.find('.total_product_price_in_cart').text(total_price)

        calculatingBasketAmount()
    })

    calculatingBasketAmount()
})
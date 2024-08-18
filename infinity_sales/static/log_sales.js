

function display_sales_list(sales) {
    $("#sales_container").empty()   

    $.each(sales, function(i, datum){
        var new_row = $("<div>").addClass("row sales").attr("id", datum["id"]);
        new_row.append($("<div>").addClass("col-3").html(datum["salesperson"]));
        new_row.append($("<div>").addClass("col-4").html(datum["client"]));
        new_row.append($("<div>").addClass("col-3").html(datum["reams"]));
        var new_col = $("<div>").addClass("col-2")
        new_col.append($("<button>").text("X").addClass("btn trash_btn").attr("id", datum["id"]));
        new_row.append(new_col);
        $("#sales_container").append(new_row);
    })
    
    hover();
    reset_tbox()
}

function delete_sale(id){
    id = {"id": id} 
    $.ajax({
        type: "POST",
        url: "delete_sale",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(id),
        success: function(result){
            sales = result["sales"]
            display_sales_list(sales)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}


function save_sale(new_sale) {
    $.ajax({
        type: "POST",
        url: "save_sale",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_sale),
        success: function(data){
            var new_sales = data.sales
            var new_clients = data.clients
            console.log(new_sales)
            display_sales_list(new_sales)
            $('#client').autocomplete('option', 'source', new_clients);
            $('#client').focus();
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function reset_tbox(){
    $("#reams").val("");
    $("#client").val("");
    $("#clientWarning").text("");
    $("#reamWarning").text("");
    $("#client").focus();
}

function hover() {
    $(".sales").hover(
        function() {
            $(this).css("cursor","move");
            $(this).addClass("hovering");
        }, 
        function() {
            $(this).removeClass("hovering");
        }
    );
    $(".sales").draggable({revert: "invalid"});
    $("#trash_row").droppable({
        drop: function( event, ui ) {
            delete_sale(parseInt(ui.draggable.attr("id")));
            display_sales_list(sales);
            $(this).removeClass("hovered");
        },
        over: function(event, ui) {
            $(this).addClass("hovered");
        },
        out: function(event, ui) {
            $(this).removeClass("hovered");
        }
    });
}


function submission() {
    $("#clientWarning").text("");
    $("#reamWarning").text("");
    const salesperson = "Anish C. Nanjappa";
    const client = $("#client").val();
    const reams = $("#reams").val();

    if (!client && !reams) {
        $("#clientWarning").text("Client name is required!");
        $("#reamWarning").text("# of Reams is required!");
        $("#client").focus();
    } else if (!client) {
        $("#clientWarning").text("Client required!");
        if ( /\D/.test(reams) ) {
            $("#reamWarning").text("").text("# Reams not a number");
        }
        $("#client").focus();
    } else if (!reams){
        $("#reamWarning").text("# Reams required!");
        $("#reams").focus();
    } else {
        if ( /\D/.test(reams)) {
            $("#reamWarning").text("").text("# Reams not a number");
            $("#reams").focus();
        } else {
            const new_sale = {
                "salesperson" : salesperson, 
                "client": client,
                "reams": reams
            };
            save_sale(new_sale)
        }
    }
}

$(document).ready(function(){
    //console.log(sales)
    display_sales_list(sales);
    hover();

    $("#client").autocomplete({
        source: clients
    });

    $("#submit").click(function(){
        submission();
    });

    $("body").on("click", ".trash_btn", function() {
        delete_sale(parseInt($(this).attr('id')));
        display_sales_list(sales);
    })

    $("#reams").keypress(function(event){
        if(event.which === 13) {
            submission();
        }
    });
    

})

//$("#client").autocomplete("option", "source", clients);
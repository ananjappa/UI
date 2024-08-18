function rand_arry(length) {
    let pop_item_ids = new Array(length)
    for (i = 0; i < length; i++) {
        do {
            num = Math.floor(Math.random() * 10) + 1;
        } while (pop_item_ids.includes(num));
        pop_item_ids[i] = num;
    }
    return pop_item_ids
}

function display_bosses(bosses){
    let disp_length = 3;
    let pop_item_ids = rand_arry(disp_length);
    for (i = 0; i < pop_item_ids.length; i++) {
        var new_row = $("<div>").addClass("row boss align-items-center").attr("id", bosses[pop_item_ids[i]]["id"]);
        new_row.append($("<div>").addClass("col-2 text-center name").html(bosses[pop_item_ids[i]]["name"]));
        new_row.append($("<div>").addClass("col-3").append($("<img>").addClass("charc_pic").attr("src", bosses[pop_item_ids[i]]["image"]).attr("alt", bosses[pop_item_ids[i]]["name"] + " image")));
        new_row.append($("<div>").addClass("col-6 boss-summary").html(bosses[pop_item_ids[i]]["summary"]));
        $("#pop_container").append(new_row);
    }
    
}

function hover() {
    $(".boss").hover(
        function() {
            $(this).css("cursor","move");
            $(this).addClass("hovering");
        }, 
        function() {
            $(this).removeClass("hovering");
        }
    );
    $(".boss").click(function(){
        window.location.href = "/view/" + this.id
    });
}

function clicked(search) {

    if (!( /^\s*$/.test(search) )){
        window.location.href = "/search_results/" + search
    }

    $("#textbox").val("");
    $("#textbox").focus();
}

$(document).ready(function(){

    display_bosses(bosses);
    hover();

    $("#textbox").autocomplete({
        source: names
    });

    $("#textbox").keypress(function(event){
        if(event.which === 13) {
            clicked($("#textbox").val());
        }
    });

    $("#search-bar").on("submit", function(event) {
        event.preventDefault();
        clicked($("#textbox").val());
    });

})
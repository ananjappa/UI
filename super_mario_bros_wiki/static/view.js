function display_charc() {
    $("#pop_container").empty()
    $("#pop_container").append($("<div>").addClass("row title").html(boss["name"])).append($("<a>").addClass("nickname_view").attr("href", "/search_results/" + boss["nickname"]).html(" aka " + boss["nickname"]));
    var new_row = $("<div>").addClass("row").attr("id", boss["id"]);
    var new_col = $("<div>").addClass("col-6 text-center");
    new_col.append($("<div>").addClass("row world_difficulty").append($("<div>").addClass("col-3 world").html("World Level: " + boss["boss-level"]), $("<div>").addClass("col-3 difficulty").html("Difficulty: " + boss["difficulty"])));
    new_col.append($("<div>").addClass("row align-items-center summary").html(boss["summary"]));
    new_col.append($("<div>").addClass("row enemy_title").attr("id", boss["id"]).html("Enemies:"));
    $.each(boss["enemies"], function(index, enemy){
        new_col.append($("<a>").addClass("row enemy").attr("id", boss["id"]).attr("href", "/search_results/" + enemy).html(enemy));
    })
    new_row.append(new_col);
    new_row.append($("<div>").addClass("col-2"))
    new_row.append($("<div>").addClass("col-3").append($("<img>").addClass("charc_page_pic").attr("src", boss["image"]).attr("alt", boss["name"] + " image")))
    $("#pop_container").append(new_row);
    $("#pop_container").append("<button class='edit-btn' onclick=\"window.location.href='/edit/" + boss["id"] + "'\">Edit " + boss["name"] + "</button>");
}

function clicked(search) {
    if (!(/^\s*$/.test(search))){
        window.location.href = "/search_results/" + search
    } 
    
    $("#textbox").val("");
    $("#textbox").focus();
        
}

$(document).ready(function(){

    display_charc()
    $("#textbox").keypress(function(event){
        if(event.which === 13) {
            clicked($("#textbox").val());
        }
    });

    $("#search-bar").on("submit", function(event) {
        event.preventDefault()
        clicked($("#textbox").val());
    });

    $("#textbox").autocomplete({
        source:names
    });


});
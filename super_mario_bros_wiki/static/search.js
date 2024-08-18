function highlight(item){
    var name_highlight = item["name"]
    var summary_highlight = item["summary"]
    var nickname_highlight = item["nickname"]
    var padding = 55
    if (item["matched"].includes("name")) {
        for (let i = 0; i < item["start_ind_name"].length; i++) {
            st = item["start_ind_name"][i] + (padding * i)
            en = item["end_ind_name"][i] + (padding * i)
            name_highlight = [name_highlight.slice(0, st), "<span class='highlight-result border-secondary'>", name_highlight.slice(st, en), "</span>", name_highlight.slice(en)].join('')
        } 
    } 
    
    if (item["matched"].includes("summary")) {
        for (let i = 0; i < item["start_ind_summary"].length; i++) {
            st = item["start_ind_summary"][i] + (padding * i)
            en = item["end_ind_summary"][i] + (padding * i)
            summary_highlight = [summary_highlight.slice(0, st), "<span class='highlight-result border-secondary'>", summary_highlight.slice(st, en), "</span>", summary_highlight.slice(en)].join('')
        }
    }

    if (item["matched"].includes("nickname")) {
        for (let i = 0; i < item["start_ind_nickname"].length; i++) {
            st = item["start_ind_nickname"][i] + (padding * i)
            en = item["end_ind_nickname"][i] + (padding * i)
            nickname_highlight = [nickname_highlight.slice(0, st), "<span class='highlight-result border-secondary'>", nickname_highlight.slice(st, en), "</span>", nickname_highlight.slice(en)].join('')
        }
    }
    return {
        new_name: name_highlight, 
        new_summary: summary_highlight, 
        new_nickname: nickname_highlight
    };
}


function display_bosses(n_items, results){
    $("#textbox").val("");
    $("#textbox").focus();
    $("#pop_container").empty()
    $("#pop_container").append($("<div>").addClass("title").html("Search Results for " + '"' + search + '"'));
    if (n_items == 0){
        $("#pop_container").append($("<div>").addClass("col align-items-center finding").html("No results found."));
    } else {
        $("#pop_container").append($("<div>").addClass("col align-items-center finding").html("Found " + n_items + " items:"));
        for (i = 0; i < n_items; i++) {
            
            result = highlight(results[i])
            if (results[i]["matched"].includes("nickname")){
                var new_row = $("<div>").addClass("row boss align-items-center").attr("id", results[i]["id"]);
                new_row.append($("<div>").addClass("col-2").append($("<div>").addClass("text-center name").html(result.new_name)).append($("<div>").addClass("text-center nickname").html(" aka " + result.new_nickname)));
                new_row.append($("<div>").addClass("col-4").append($("<img>").addClass("charc_pic").attr("src", results[i]["image"]).attr("alt", results[i]["name"]+" image")));
                new_row.append($("<div>").addClass("col-5 boss-summary").html(result.new_summary));
                new_col = new_row.append($("<div>").addClass("enemy col-4").attr("id", results[i]["id"]))
                $("#pop_container").append(new_row);
            } else {
                var new_row = $("<div>").addClass("row boss align-items-center").attr("id", results[i]["id"]);
                new_row.append($("<div>").addClass("col-2").append($("<div>").addClass("text-center name").html(result.new_name)).append($("<div>").addClass("text-center nickname").html(" aka " + results[i]["nickname"])));
                new_row.append($("<div>").addClass("col-4").append($("<img>").addClass("charc_pic").attr("src", results[i]["image"]).attr("alt", results[i]["name"]+" image")));
                new_row.append($("<div>").addClass("col-5 boss-summary").html(result.new_summary));
                new_col = new_row.append($("<div>").addClass("enemy col-4").attr("id", results[i]["id"]))
                $("#pop_container").append(new_row);
            }
            
        }
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

    if (!(/^\s*$/.test(search))){
        window.location.href = "/search_results/" + search
    } 

    $("#textbox").val("");
    $("#textbox").focus();
        
}


$(document).ready(function(){

    display_bosses(n_items, results);
    hover();


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
        source: names
    });

    

})
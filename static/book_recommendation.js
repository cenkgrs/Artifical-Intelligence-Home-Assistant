 $(document).ready(function(){

    // This will work when user starts to type a book name to input
    $("#book-name-input").keyup(function( event ) {
        inp = $(this).val()
        console.log(inp)
        if (inp.length >= 1){
            $.ajax({
                url: "http://localhost:5000/get_book_input",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({"inp": inp,})
            }).done(function(data) {
                console.log(data)
                if (data && data["status"] != false)
                {
                    console.log(data)
                    $("#book-input-items").empty()
                    $("#book-input-items").fadeIn()
                    data.forEach(function(entry, i) {
                        name = entry
                        console.log(name)
                        item = document.createElement("strong");
                        item.className = "book-input-item";
                        item.innerHTML = name;
                        $("#book-input-items").append(item)
                    })
                }
            });
        }else{
            $("#book-input-items").empty()
            $("#book-input-items").fadeOut()

        }
    })

    // This will works when user clicks one of the similar inputs
    $(document).on("click", ".book-input-item", function() {
        $("#book-name-input").val($(this).html())
        $("#book-input-items").empty()
        $("#book-input-items").fadeOut()
    })

    // This will work when recommend button clicked and will fill the result container with recommended books
    $(document).on("click", "#recommend-button", function() {
        book_name = $("#book-name-input").val()

        $.ajax({
            url: "http://localhost:5000/get_book_recommendation",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({"book_name": book_name,})
        }).done(function(data) {
            if (data && data["status"] != false)
            {
                console.log(data)
                $("#book-input-items").empty()
                $("#book-input-items").fadeOut()
                $("#book-recommendations").empty()
                $("#book-recommendations").fadeIn()
                data.forEach(function(entry, i) {
                    name = entry
                    console.log(name)
                    item = document.createElement("strong");
                    item.className = "recommended-book-item";
                    item.innerHTML = name;
                    $("#book-recommendations").append(item)
                })
            }else{
                speak("I can't give you similar book to this one sir")
            }
        });
    })

 });

 function get_book_input(){

 }
$.ajax({
    type: "GET",
    url: "http://localhost:7000/headlines", 
}).done(function (data) {
    $("#headlines").empty(); 
    $("#headlines").append($("<ul/>")); 
    var news = JSON.parse(data); 
    news.forEach(function (element) {
        console.log(element)
        var newsItem = element.title + ", read more: " + element.links;
        $("#headlines ul").append($("<li/>").html(newsItem)); 
    });
});
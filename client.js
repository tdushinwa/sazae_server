$.ajax({
    url: "http://172.17.0.1:8080",
    type: "POST",
    data: "id=1&id=2&id=3&id=4",
    dataType: "json",
    success: function(data, textStatus){
        console.log(data);
    },
    error: function(xhr, textStatus, errorThrown){
        console.log(xhr);
    }
});

function transform(line) {
    var values = line.split(',');
    var obj = new Object();

    obj.hotel_id = parseInt(values[0], 10);  
    obj.name = values[1];
    obj.city = values[2];
    obj.address = values[3];
    obj.hotel_class = values[4];  
    obj.url = values[5];
    obj.ranking = parseInt(values[6], 10);  
    obj.number_of_rooms = parseInt(values[7], 10);  

    return JSON.stringify(obj);
}
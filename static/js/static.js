let dataMap = new Map()
dataMap.set("test", ["Hi", "Test", "Next"])
dataMap.set("test2", ["Hi2", "Test2", "Next2"])

addCarsMakers()


function addCarsMakers() {
    let keysIterator = dataMap.keys()
    let key = keysIterator.next()
    while (!key.done) {

        addToSelect(key.value, "car_make")

        key = keysIterator.next()
    }


}


function addToSelect(value, name) {
    var x = document.getElementById(name);
    var option = document.createElement("option");
    option.text = value;
    option.value = value;
    x.add(option);
}


function prepareCarModel() {
    document.getElementById("car_model").innerHTML = "";
    var carMaker = document.getElementById("car_make").value;
    var modelsData = dataMap.get(carMaker);
    modelsData.forEach(element => {
        addToSelect(element, "car_model");
    });
}
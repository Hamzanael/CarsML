let dataMap = {}
getModels()

function getModels() {
    fetch('/models')
        .then(response => response.json())
        .then(data => {
            // console.log(data)
            dataMap = new Map(Object.entries(data))
            addCarsMakers(dataMap)
        })
    // console.log(dataMap)
    // return dataMap
}


function addCarsMakers(dataMap) {
    let keysIterator = dataMap.keys()
    let key = keysIterator.next()
    while (!key.done) {
        console.log(key)
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
    document.getElementById("car_model").innerHTML = "<option disabled hidden selected value=''>Choose...</option>";
    var carMaker = document.getElementById("car_make").value;
    var modelsData = dataMap.get(carMaker);
    modelsData.forEach(element => {
        addToSelect(element, "car_model");
    });
}


function parseResults(data,result){
    let keysIterator = data.values()
    document.getElementById("carFinalName").innerHTML=keysIterator.next().value
    document.getElementById("carFinalModel").innerHTML=keysIterator.next().value
    document.getElementById("carFinalYear").innerHTML=keysIterator.next().value
    document.getElementById("carFinalTransmission").innerHTML=keysIterator.next().value
    document.getElementById("carFinalColor").innerHTML=keysIterator.next().value
    document.getElementById("carFinalKilometers").innerHTML=keysIterator.next().value
    document.getElementById("carFinalPrice").innerHTML= result
}

//Form Submission
document.body.addEventListener("submit", async function (event) {
    event.preventDefault();
    const form = event.target;
    const data = new URLSearchParams([...(new FormData(form))])
    const result = await fetch("/search", {
            method: form.method,
            body: data,
        })
        .then((response) => response.json())
        .then((json) => {
           parseResults(data,json)
        }
       
        )
        .catch((error) => console.log(error));
});
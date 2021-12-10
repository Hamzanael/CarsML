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
    document.getElementById("carFinalPrice").innerHTML="$"+result
}

//Form Submission 
document.body.addEventListener("submit", async function (event) {
    event.preventDefault();
    const form = event.target;
    const data = new URLSearchParams([...(new FormData(form))])
    const result = await fetch("http://localhost:3000/", {
            method: form.method,
            body: data,
        })
        .then((response) => response.json())
        .then((json) => {
           parseResults(data,json.value)
        }
       
        )
        .catch((error) => console.log(error));
});
function runMacro(ip, port, macro) {
    const httpRequest = new XMLHttpRequest();
    const ad = ip
    const pn = port
    const ma = macro
    const url = `http://${ad}:${pn}/macro?name=${ma}`;

    httpRequest.open('GET', url);
    console.log(httpRequest)
    httpRequest.send();
}


function runTask(ip, port, macro) {
    var httpRequest = new XMLHttpRequest();
    const ad = ip
    const pn = port
    const ma = macro
    const url = `http://${ad}:${pn}/executetask?name=${ma}`;
    httpRequest.open('GET', 'http://10.0.0.111:8090/executetask?name=' + taskName);
    console.log(httpRequest)
    console.log(taskName)
    httpRequest.send();
}


function runTCP(ip, port, macro) {
    var httpRequest = new XMLHttpRequest();
    const ad = ip
    const pn = port
    const ma = macro
    const url = `http://${ad}:${pn}/executetask?name=${ma}`;
    httpRequest.open('GET', 'http://10.0.0.111:8090/executetask?name=' + taskName);
    console.log(httpRequest)
    console.log(taskName)
    httpRequest.send();
}
function dummy() {
	var f = document.getElementById("from").value;
    var dt=document.getElementById("data").value;
    var to=document.getElementById("to").value;
	eel.convert_currency_amount(dt,f,to)(run)
}


function run(li) {
	document.getElementById("output").value = li;
}

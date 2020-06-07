function dummy() {
	var f = document.getElementById("from").value;
  var dt=document.getElementById("data").value;
  var to=document.getElementById("to").value;
	eel.dll(dt,f,to)(run)
	/*eel.convert(data,dt,to)(run)*/
}


function run(li) {
	document.getElementById("output").value = li;
  /*document.getElementById('output').value = li;*/
}

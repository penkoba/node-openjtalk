var socket = io.connect('/');

function talkArea(){
  socket.emit('talk', document.getElementById("droparea").value);
}

function talkFile(file) {
  var reader = new FileReader();
  reader.onload = function(e) {
    var txt = e.target.result;
    document.getElementById("droparea").value = txt;
    socket.emit('talk', txt);
  }
  reader.readAsText(file, "utf-8");
}

function onChangeFile(e) {
  talkFile(e.target.files[0]);
}

function onDropFile(e) {
  e.preventDefault();
  talkFile(e.dataTransfer.files[0]);
};

function onDragOver(e) {
  if (e.preventDefault) {
    e.preventDefault();
  }
  return false;
};

function onDragEnter(e) {
  if (e.preventDefault) {
    e.preventDefault();
  }
  return false;
};

window.onload = function() {
  var btn = document.getElementById("readbtn");
  btn.addEventListener("change", onChangeFile, false);
  var da = document.getElementById("droparea");
  da.addEventListener("dragover", onDragOver, false);
  da.addEventListener("dragenter", onDragEnter, false);
  da.addEventListener("drop", onDropFile, false);
};

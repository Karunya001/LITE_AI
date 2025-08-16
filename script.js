function openApp(port) {
  window.open("http://localhost:" + port, "_blank");
}

document.getElementById("btn1").addEventListener("click", () => openApp(8501));
document.getElementById("btn2").addEventListener("click", () => openApp(8502));
document.getElementById("btn3").addEventListener("click", () => openApp(8503));
document.getElementById("btn4").addEventListener("click", () => openApp(8504));
document.getElementById("btn5").addEventListener("click", () => openApp(8505));
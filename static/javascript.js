fetch("/api/soma")
  .then(response => response.json())
  .then(data => {
    console.log("Resultado:", data.resultado);
  });
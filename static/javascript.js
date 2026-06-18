function python(api,a,b) {
return fetch(`/api/${api}`, {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    a: a,
    b: b
  })
})
.then(res => res.json())
.then(data => {
  return data.resultado
});
}

python("multiplicar", 5, 9).then(resultado => {
  console.log(resultado);
});
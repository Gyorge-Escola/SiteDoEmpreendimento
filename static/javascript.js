function python(api,a,b) {
fetch(`/api/${api}`, {
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
  console.log(data.resultado); // 50
});
  return data.resultado
}

python("multiplicar",5,9)
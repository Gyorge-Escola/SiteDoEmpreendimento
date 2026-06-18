fetch("https://127.0.0.1:8000/soma", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ a: 2, b: 3 })
})
.then(res => res.json())
.then(data => console.log(data));
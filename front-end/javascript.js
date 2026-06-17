fetch("https://symmetrical-space-capybara-q7x95grrvx9vf457v-8000.app.github.dev/:8000/soma", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ a: 2, b: 3 })
})
.then(res => res.json())
.then(data => console.log(data));
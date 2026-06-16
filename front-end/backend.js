async function calcular(a,b) {
    const res = await fetch(`/api/somar?a=${a}&b=${b}`);
    const data = await res.json();

    return data.resultado;
}


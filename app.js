const root = document.getElementById("root");

// const ishchi = {
//     ishchi_nomi: "Jhon Doe",
//     ish_joyi: "Hokimiyat",
//     ish_vaqti: "9:00/18:00",
//     daromadi: 2000000
// } 

// console.log(ishchi.ish_joyi);

fetch("data.json")
    .then(response => response.json())
    .then(data => {
        data.forEach(i => {
            root.innerHTML += `
        <h1>Ishchi nomi: ${i.ishchi_nomi}</h1>
        <p>Ishchi joyi: ${i.ish_joyi}</p>
        <p>Ish vaqti: ${i.ish_vaqti}</p>
        <i>Daromadi: ${i.daromadi}</i>
        `;
        });
    });
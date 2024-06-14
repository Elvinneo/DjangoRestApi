fetch("http://127.0.0.1:8000/movies-api/list/")
  .then((res) => res.json())
  .then((items) => items.map(item => doldur(item)));


function doldur(item){
  const page=`<div class="movie">
          <div class="imag">
              <img src="${item.image}" alt="">
          </div>
          <div class="options">
              <h3>${item.title}</h3>
              <h3>${item.name}</h3>
              <h3>${item.year}</h3>
              <h3>${item.score}</h3>
          </div>
      </div>;`

    document.querySelector(".items").innerHTML+=page;
}






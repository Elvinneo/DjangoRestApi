const main = document.querySelector('body')
let titles=[];
let names=[];
let years=[];
let images =[];
let scores =[];

let yoxla = 0;

fetch("http://127.0.0.1:8000/movies-api/list/")
  .then((res) => res.json())
  .then((items) => items.map((item) => (images.push(item.image),titles.push(item.title),years.push(item.year),names.push(item.name),scores.push(item.score))));
const movies = document.createElement("div");
movies.classList.add("movies");
main.append(movies);


function yukle(){
  for (let i=0 ; i<= titles.length-1;i++){
    const movie = document.createElement("div");
    movie.classList.add("movie");
    movies.append(movie);
    const img = document.createElement("div");
    img.classList.add("imag");
    movie.append(img);
    const imgg=document.createElement('img')
    imgg.src=images[i]
    img.append(imgg);
    const option = document.createElement("div");
    option.classList.add("options");
    movie.append(option);
    const titl=document.createElement("h3")
    titl.innerHTML=titles[i]
    const yea=document.createElement("h3")
    yea.innerHTML=years[i]
    const nam=document.createElement("h3")
    nam.innerHTML=names[i]
    const score=document.createElement("h3")
    score.innerHTML=scores[i]
    option.append(titl,nam,score,yea)
    
}
}










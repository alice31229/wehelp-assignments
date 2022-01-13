// https://stackoverflow.com/questions/53687439/write-out-api-object-from-fetch-to-html

let clist_name=[];
let clist_img=[];

function createdata() {
  let src =
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
  fetch(src)
    .then(function (response) {
      return response.json();
    })
    .then(function (result) {
        let x = result.result.results;
        let landmark = "";
        for (let i of x) {
            landmark = i.stitle;
            clist_name.push(landmark);
        }
        for (let i of x) {
            landmark = "https" + i.file.split("https")[1];
            clist_img.push(landmark);
        }
        //console.log("fetch finished");
        let demand8 = {
        title:clist_name.slice(0,8),
        photo:clist_img.slice(0,8)
        };

        const allEvents = eventsDomTree(demand8);
        document.querySelector('body').appendChild(allEvents);


        function eventsDomTree(events){
            const main = document.querySelector('main');
            let i = 0;
            events.title.forEach(event => {
                const allEvents = document.createElement('div');
                allEvents.setAttribute('class','picture');

                const card = document.createElement('div');
                card.setAttribute('class', 'word');
                card.textContent = event;

                const eventImg = document.createElement('img');
                eventImg.setAttribute('class','spot');
                eventImg.src = events.photo[i];
        
                allEvents.appendChild(eventImg);
                allEvents.appendChild(card);
        
                main.appendChild(allEvents);
                i+=1;
            });
            return main
        };
        const btn = document.createElement('button');
        btn.setAttribute('class','btn');
        btn.textContent = 'Load More';
        btn.style.paddingTop = '15px';
        btn.style.paddingBottom = '15px';
        btn.style.paddingLeft = '50px';
        btn.style.paddingRight = '50px';
        document.querySelector('main').appendChild(btn);

        //let btn = document.querySelector('.btn');
        btn.addEventListener('click', function(){
          let demand16 = {
            title:clist_name.slice(8,16),
            photo:clist_img.slice(8,16)
          };
          const allEvents = eventsDomTree(demand16);
          // in plain JavaScript, you can use the appendChild() method to move the existing source element in the document to the target element
          document.querySelector('main').appendChild(btn);
          //btn.style.borderStyle = 'bold';
          //btn.style.borderWidth = 'thick';
          btn.style.borderRadius = '10px';
          btn.style.border = 'solid 2px';
          //document.querySelector('.btn').style.border = '2px solid black';

        }, false);
        


    });
};
createdata();
//console.log("call");

// let bg = document.querySelector('.burger');
// bg.addEventListener('click', function(){
//   let Is = document.querySelector('.item');
//   Is.style.display = 'inline';
//   Is.style.float = 'none';
// }, flase);

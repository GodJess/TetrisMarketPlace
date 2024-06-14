


const ctx = document.getElementById('MyChart').getContext("2d");
let myChar = new Chart(ctx, {
    type: "doughnut",
    data:{
        labels: ['spend', 'get'],
        datasets:[{
            label: "Transactions",
            data: [15000, 23054],
            backgroundColor: ["#ffc505ec", "#58ED4B"],
            borderColor: [""],
            borderWidth: 2
        }]
    },
    options: {
        maintainAspectRatio: true,
        responsive: true,
        height: 100, 
        width: 100   
    }
});

const gtx = document.getElementById("Chart").getContext("2d");
let char = new Chart(gtx, {
    type: "bar",
    data:{
        labels: ['Win', 'Spr', 'Sum', 'Otm'],
        datasets:[{
            label: "profit",
            data: [ 1343, 5346, 12333, 5623],
            backgroundColor: ['#0febcd', '#f50acf',  '#0bda84', '##ff0055'],
            borderColor: [''],
            borderWidth:2
        }]
        
    },
    options: {
        maintainAspectRatio: true,
        responsive: true,
        height: 100, 
        width: 100   
    }
});

document.addEventListener('DOMContentLoaded', ()=>{

    const SelectProd = document.getElementById('selector');
    const prod = SelectProd.querySelector('.GetOptions');
    const Count = document.querySelector('.count-product');


    const Shoes = (i)=>{
        var size = ''
        if(i == 0){
            size = 's'
        }
        else if(i == 1){
            size = 'm'
        }
        else if(i == 2){
            size = 'l'
        }
        else if(i == 3){
            size = 'xl'
        }
        else if(i == 4){
            size = 'xxl'
        }
        return size;
    }

    SelectProd.addEventListener('change', ()=>{
        const selectOptions = SelectProd.options[SelectProd.selectedIndex];
        const name = selectOptions.value;
        console.log(name);
        Form(name);
    });

    const Form = (name) =>{
        Count.innerHTML = '';
        if(name == "shoes"){
            for(var i = 0; i < 5; i++){
                var size = Shoes(i);
                console.log(size);
                var sizeDiv = document.createElement('div');
                sizeDiv.className = 'ell';
                sizeDiv.innerHTML =  '<input class="' + size + '" type="count" name="' + size + '" placeholder=" '+ size +' ">'
                Count.appendChild(sizeDiv);
            }
        }
        else if(name  == 'snikers'){
            for(var i = 36; i < 46; i++){
                var size = i;
                var sizeDiv = document.createElement('div');
                sizeDiv.className = 'ell';
                sizeDiv.innerHTML =  '<input class="'+ size +'" type="count" name="'+ size + '" placeholder=" '+ size +' ">'
                Count.appendChild(sizeDiv);
            }
        }
        else if(name == 'product'){
            var sizeDiv = document.createElement('div');
            sizeDiv.className = 'prodell';
            sizeDiv.innerHTML =  '<input class="count" type="count" name="count" placeholder="0">'
            Count.appendChild(sizeDiv);
        }
    }


    const image = document.querySelectorAll('.ImageSrc');

    document.querySelectorAll('.load').forEach(input => {
        input.addEventListener('change', (e) => {
            const file = e.target.files[0];
            const reader = new FileReader();
    
            reader.onload = function(e) {
                const imageSrc = e.target.result;
                const imageInputId = input.getAttribute('id');
                image.forEach(img => {
                    if (img.getAttribute('id') == imageInputId) {
                        img.src = imageSrc;
                    }
                })
            };
    
            reader.readAsDataURL(file);
        });
    });


    const infoabout = document.querySelectorAll('.info-about-saler');
    const infoblock = document.querySelectorAll('.info-block-opt');
    infoabout.forEach(inf =>{
        inf.addEventListener('click', ()=>{
            infoblock.forEach(block=>{
                if(inf.getAttribute('id') == block.getAttribute('id')){
                    if(block.classList.contains('open')){
                        block.classList.remove('open');
                    }
                    else{
                        block.classList.add('open');
                    }
                }
            })
            
        });
    });

    const settings = document.querySelector('.settings');
    const menuBlock = document.querySelector('.block-menu-settings');
    const iconMenu = document.querySelector('.icon-menu')

    settings.addEventListener('click', ()=>{
        if(menuBlock.classList.contains('open')){
            menuBlock.classList.remove('open');
        }
        else{
            menuBlock.classList.add('open');
        }
    })

    iconMenu.addEventListener('click', ()=>{
        menuBlock.classList.remove('open')
    })
    

});





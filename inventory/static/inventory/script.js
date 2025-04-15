const receive = document.querySelector('#receive')
const inventory = document.querySelector('#inventory')
const plusinventory = document.querySelector('#plusinventory')
const edit = document.querySelector('#edit')
receive.addEventListener('click',()=>{
    inventory.style.display = 'none';
    plusinventory.style.display = 'block';
})

 
      

function editb(id){
    document.querySelector(`#id${id}`).style.display = 'none';
    document.querySelector(`#editform${id}`).style.display = 'block';
}

function goback(id){
    document.querySelector(`#id${id}`).style.display = 'block';
    document.querySelector(`#editform${id}`).style.display = 'none';
    return false;
}

function del(id){
    fetch(`/del/${id}`,{
        method:'DELETE',
        headers: {
            'X-CSRFToken':gettoken()
        }
    })
  document.querySelector(`.id${id}`).classList.add('del'); 
  setTimeout(()=>{
  document.querySelector(`.id${id}`).remove();  
  },1100) 
  

}

function gettoken(){
    return document.querySelector('[name=cs]').value;
}
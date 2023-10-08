const name=document.getElementsByClassName('name')[0]
const btn=document.getElementsByClassName('btn')[0]

btn.addEventListener('click',function (){
    if ( name.value=='' ){
        alert('Я всего лишь попросил ввести данные')
    }
})

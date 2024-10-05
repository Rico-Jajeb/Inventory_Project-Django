
const ab34 = document.getElementById('ab3');
function ab4()
{
    ab34.innerHTML = "cba";
}








// -------------------------------------- left sidebar file


const ToResizeLeftSidebar = document.getElementById("ToResizeLeftSidebar");
const toResizeMainContent = document.getElementById("toResizeMainContent");

const hide = document.getElementById("hide");
const hide1 = document.getElementById("hide1");
const hide2 = document.getElementById("hide2");
const hide3 = document.getElementById("hide3");
const hide4 = document.getElementById("hide4");
const hide5 = document.getElementById("hide5");
const hide6 = document.getElementById("hide6");
const hide7 = document.getElementById("hide7");
const hide8 = document.getElementById("hide8");
const hide9 = document.getElementById("hide9");


function buttonToResizeLeftSidebar(){
    ToResizeLeftSidebar.classList.toggle('ToResizeLeftSidebar');
    toResizeMainContent.classList.toggle('toResizeMainContent');
    hide.classList.toggle('hide');
    hide1.classList.toggle('hide');
    hide2.classList.toggle('hide');
    hide3.classList.toggle('hide');
    hide4.classList.toggle('hide');
    hide5.classList.toggle('hide');
    hide6.classList.toggle('hide');
    hide7.classList.toggle('hide');
    hide8.classList.toggle('hide');
    hide9.classList.toggle('hide');
}


const userDropDown = document.getElementById('userDropDown');

function UdropDown(){
    userDropDown.classList.toggle('userDropdownOnn')

}



const userDropDown2 = document.getElementById('userDropDown2');
function UdropDown2(){
    userDropDown2.classList.toggle('userDropdownOnn')

}

const userDropDown3 = document.getElementById('userDropDown3');
function UdropDown3(){
    userDropDown3.classList.toggle('userDropdownOnn')

}







// ------------------------------------------------------ navbar file -------------------------------------------

const searchbar = document.getElementById('searchbar');
searchbar.addEventListener('click', function(){
    this.style.borderBottom = '2px solid';
    this.style.borderBottomColor = "#e91e62fb";
})

searchbar.addEventListener('blur', function(){
    this.style.borderBottom = '';
    this.style.borderBottomColor = '';
})




const itmInput = document.getElementById('itmInput');
const itmInput2 = document.getElementById('itmInput2');
const itmInput3 = document.getElementById('itmInput3');
const itmInput4 = document.getElementById('itmInput4');
const itmInput5 = document.getElementById('itmInput5');
const itmInput6 = document.getElementById('itmInput6');
itmInput.addEventListener('click', function(){
    this.style.borderBottom = '2px solid';
    this.style.borderBottomColor = "#e91e62fb";
})
itmInput2.addEventListener('click', function(){
    this.style.borderBottom = '2px solid';
    this.style.borderBottomColor = "#e91e62fb";
})
itmInput3.addEventListener('click', function(){
    this.style.borderBottom = '2px solid';
    this.style.borderBottomColor = "#e91e62fb";
})
itmInput4.addEventListener('click', function(){
    this.style.borderBottom = '2px solid';
    this.style.borderBottomColor = "#e91e62fb";
})
itmInput5.addEventListener('click', function(){
    this.style.borderBottom = '2px solid';
    this.style.borderBottomColor = "#e91e62fb";
})
itmInput6.addEventListener('click', function(){
    this.style.borderBottom = '2px solid';
    this.style.borderBottomColor = "#e91e62fb";
})

itmInput.addEventListener('blur', function(){
    this.style.borderBottom = '';
    this.style.borderBottomColor = '';
})
itmInput2.addEventListener('blur', function(){
    this.style.borderBottom = '';
    this.style.borderBottomColor = '';
})
itmInput3.addEventListener('blur', function(){
    this.style.borderBottom = '';
    this.style.borderBottomColor = '';
})
itmInput4.addEventListener('blur', function(){
    this.style.borderBottom = '';
    this.style.borderBottomColor = '';
})
itmInput5.addEventListener('blur', function(){
    this.style.borderBottom = '';
    this.style.borderBottomColor = '';
})
itmInput6.addEventListener('blur', function(){
    this.style.borderBottom = '';
    this.style.borderBottomColor = '';
})


// importt================================



function toggleMenu() {
    var menu = document.getElementById("offCanvasMenu");
    menu.classList.toggle("active");
  }




//--------------- modal 

//----------------------------------------open modal
function pop_modal()
{
    const modal1 = document.getElementById('modal1');
    const modal2 = document.getElementById('modal2');
    modal1.style.display = "block";
    modal2.style.display = "block";

}

function pop_modal2()
{
    const modal1 = document.getElementById('modal3');
    const modal2 = document.getElementById('modal4');
    modal1.style.display = "block";
    modal2.style.display = "block";
}

function pop_modal3()
{
    const modal1 = document.getElementById('modal5');
    const modal2 = document.getElementById('modal6');
    modal1.style.display = "block";
    modal2.style.display = "block";
}

function pop_modal4()
{
    const modal1 = document.getElementById('modal7');
    const modal2 = document.getElementById('modal8');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal5()
{
    const modal1 = document.getElementById('modal9');
    const modal2 = document.getElementById('modal10');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal6()
{
    const modal1 = document.getElementById('modal11');
    const modal2 = document.getElementById('modal12');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal7()
{
    const modal1 = document.getElementById('modal13');
    const modal2 = document.getElementById('modal14');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal8()
{
    const modal1 = document.getElementById('modal15');
    const modal2 = document.getElementById('modal16');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal9()
{
    const modal1 = document.getElementById('modal17');
    const modal2 = document.getElementById('modal18');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal10()
{
    const modal1 = document.getElementById('modal19');
    const modal2 = document.getElementById('modal20');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal11()
{
    const modal1 = document.getElementById('modal21');
    const modal2 = document.getElementById('modal22');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal12()
{
    const modal1 = document.getElementById('modal23');
    const modal2 = document.getElementById('modal24');
    modal1.style.display = "block";
    modal2.style.display = "block";
}
function pop_modal13()
{
    const modal1 = document.getElementById('modal25');
    const modal2 = document.getElementById('modal26');
    modal1.style.display = "block";
    modal2.style.display = "block";
}







//-----------------------------close modal
function close_pop_modal()
{
    const modal1 = document.getElementById('modal1');
    const modal2 = document.getElementById('modal2');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal2()
{
    const modal1 = document.getElementById('modal3');
    const modal2 = document.getElementById('modal4');
    modal1.style.display = "none";
    modal2.style.display = "none";
}
function close_pop_modal3()
{
    const modal1 = document.getElementById('modal5');
    const modal2 = document.getElementById('modal6');
    modal1.style.display = "none";
    modal2.style.display = "none";
}
function close_pop_modal4()
{
    const modal1 = document.getElementById('modal7');
    const modal2 = document.getElementById('modal8');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal5()
{
    const modal1 = document.getElementById('modal9');
    const modal2 = document.getElementById('modal10');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal6()
{
    const modal1 = document.getElementById('modal11');
    const modal2 = document.getElementById('modal12');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal7()
{
    const modal1 = document.getElementById('modal13');
    const modal2 = document.getElementById('modal14');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal8()
{
    const modal1 = document.getElementById('modal15');
    const modal2 = document.getElementById('modal16');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal9()
{
    const modal1 = document.getElementById('modal17');
    const modal2 = document.getElementById('modal18');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal10()
{
    const modal1 = document.getElementById('modal19');
    const modal2 = document.getElementById('modal20');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal11()
{
    const modal1 = document.getElementById('modal21');
    const modal2 = document.getElementById('modal22');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal12()
{
    const modal1 = document.getElementById('modal23');
    const modal2 = document.getElementById('modal24');
    modal1.style.display = "none";
    modal2.style.display = "none";
}

function close_pop_modal13()
{
    const modal1 = document.getElementById('modal25');
    const modal2 = document.getElementById('modal26');
    modal1.style.display = "none";
    modal2.style.display = "none";
}







// External JavaScript file

function changeText() {
    var heading = document.getElementById("bv");
    heading.innerHTML = "Text changed by button";
  }
  










  

  
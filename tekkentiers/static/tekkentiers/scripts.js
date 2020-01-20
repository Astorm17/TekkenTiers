$('.characterCard').draggable();

function addRow() { 
  // create row div
  var rowDiv = document.createElement('div');
  rowDiv.setAttribute('class', 'row tierRow');
  rowDiv.setAttribute('id', 'tier-row');

  // create div that prepends buttons
  var spanDiv = document.createElement('span');
  var color = getRandomColor();
  spanDiv.setAttribute('class', 'tierInputField');
  spanDiv.setAttribute('contenteditable', 'true');
  spanDiv.setAttribute('style', 'color: white; background-color: ' + color + ';');

  // assemble the div
  rowDiv.appendChild(spanDiv);

  document.getElementById("tier-rows").appendChild(rowDiv);
}

function delRow() {
  // removes most recent row
  var rows = document.getElementsByClassName('tierRow');
  var row = rows[rows.length - 1];
  row.parentNode.removeChild(row);
  
}

function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function shareList() {
  var rows = getRows();
  var characterCards = getCharacterCards();
  var tierRows = {};
  var row;
  var character;

  tierRows["tier"] = [];

  var i;
  var j;
  for(i = 0; i < rows.length; i++) {
    row = rows[i];
    tierRows["row" + i] = [];
    tierRows["tier"].push(row.getElementsByTagName("span")[0].innerText);
    for(j = 0; j < characterCards.length; j++){
      character = characterCards[j];
      if(isInRow(character, row) == true) {
        tierRows["row" + i].push(character.getElementsByClassName("nameplate")[0].innerText);
      } 
    }
  }
  console.log(JSON.stringify(tierRows));

  var input = document.getElementById("id_post");
  input.setAttribute('value', JSON.stringify(tierRows));
}

function getRows() {
  var rows = document.getElementsByClassName('tierRow');
  return rows;
}

function getCharacterCards() {
  var characterCards = document.getElementsByClassName('characterCard');
  return characterCards;
}

// checks if portrait is in row
function isInRow(character, row) {
  var charBound = character.getBoundingClientRect();
  var rowBound = row.getBoundingClientRect();

  // calculate portraits midpoint
  var xMid = (charBound.left + charBound.right) / 2;
  var yMid = (charBound.top + charBound.bottom) / 2;

  // check if portrait is in row
  if(xMid <= rowBound.right && xMid >= rowBound.left) {
    if(yMid <= rowBound.bottom && yMid >=rowBound.top) {
      return true;
    }
  }
  return false;
}
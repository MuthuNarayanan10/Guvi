
function question0(array){
  let arr = [];
  for (let i = 0; i < array.length; i++){
    if (array[i] % 2 === 0){
      arr.push(array[i]);
    }
  }
  return arr;
}

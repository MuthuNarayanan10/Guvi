var object = {
    name: 'ISRO',
     age: 35, role: 
     'Scientists'};
 
  
  function convertObjectToList(obj) {
    var outer = [];
    
    for(var prop in obj){
     
      var inner = [];
      inner.push(prop);
      inner.push(obj[prop]);
    
      outer.push(inner);
    }
    return outer;
  }
  
  console.log(convertObjectToList(object));
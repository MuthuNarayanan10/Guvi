let obj1 ={name: "RajiniKanth", age: 33, hasPets : false};
let list = [];
let i = 0;
for(let prop in obj1)
{
    list[list.length] = [prop, obj1[prop]];
    i+=1;
}
console.log(list);
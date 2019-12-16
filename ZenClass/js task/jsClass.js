class Javascript{
    oddfunc(x) {
    if(x%2!==0)
    return true;
    }
    PrimeFunc(x){
        for(let i=2;i<x;i++){
            if(x%i==0)
            {
                return false;
            }
            else{
                return true;
            }
        }
    }
    sumofarray(list){
      return  list.reduce((a,b)=>(a+b));
    }
    pallindromeFunc(string){
        var re = /[^A-Za-z0-9]/g;
        var lowRegStr = string.toLowerCase().replace(re, '');
        var reverseStr = lowRegStr.split('').reverse().join(''); 
        return reverseStr === lowRegStr;
    }
    toupperString(string){
        return string.toUpperCase();
    }
}
let x=new Javascript;
if(x.oddfunc(5))
console.log("number is odd");
if(x.PrimeFunc(7))
console.log("number is prime number");
list=[1,2,3,4,5,6,6,7,8,8,9];
y=x.sumofarray(list);
console.log(y);
list2=['mom','muthu']
list2.filter(a=>{x.pallindromeFunc(a)});
console.log("pallindrome",list2)
list3=['guvi','zenclass']
for(let i=0;i<list3.length;i++)
{
    x.toupperString(list3[i]);
}
console.log("toupperString",list3);


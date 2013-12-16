// function for doubling an array

var doubler=function (arr) {
    var obj={};
for (var i=0; i < arr.length; i++){
    obj[arr[i]]=arr[i]*2;
}
return obj;
};

console.log(doubler([1, 2, 3]))

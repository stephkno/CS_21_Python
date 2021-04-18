var max = parseInt(process.argv[2])

isprime = function(num){
    var count = 2
    while (count < num){
        var d = num/count
        if (d - Math.floor(d) == 0.0){
            return false
        }
        count+=1
      }
    return true
}

p = 1
for(var i = 0; i <= max; i++){
    if (isprime(i)){
        console.log(p, i)
        p+=1
    }
}

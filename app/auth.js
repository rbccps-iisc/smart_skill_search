
var login =function(user,password){

    console.log(user,password)
    if(user==="arin@arin.com" && password==="arin"){
        return true;
    }
    else{
        return false;
    }
}

module.exports=login;
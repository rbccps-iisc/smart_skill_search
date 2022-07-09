const config = require('../../config');
const MongoClient = require('mongodb').MongoClient;
const client = new MongoClient(config.mongo.uri, { useNewUrlParser: true });


exports.search = function(req,res){
    //players.findOne({},function(err,result){
    var filter = makefilter(req);
    //console.log(filter);
    players.find(filter).toArray(function(err,result){
        if (err)
            res.send(500);
        else {
            //console.log("result length",result.length);
            var i = getRandomInt(result.length);
            //console.log(result[i]);
            if(result.length === 1){
                result = result.pop();
            } else{
                result = result[i];
            }
            if (result) {
                //console.log(result);
                var img = result.image//.split("=");

                //var out_img = "https://drive.google.com/thumbnail?id=";
                //out_img = out_img.concat(img[1],"&sz=w480");
                //console.log(out_img);
                var out_img = "/assets/images/players/";
                var out_img = out_img.concat(img,".jpeg");//[1],".jpg");
                //console.log(out_img);
                res.render('auction', {
                    name: result.name,
                    spl: result.specialization,
                    //bat: getStats(result.batting),
                    //bowl: getStats(result.bowling),
                    //field: getStats(result.keeping),
                    //wk: getStats(result.keeping),
                    bat: result.batting,
                    bats: result.batsman,
                    bowl: result.batting,
                    bowls: result.bowler,
                    tag: result.available,
                    //quote: result.quote,
                    img: out_img
                })
            }else {
                res.render("empty",{spl: filter.specialization});
            }
        }
    });
};
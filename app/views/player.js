const config = require('../../config');
const MongoClient = require('mongodb').MongoClient;
const client = new MongoClient(config.mongo.uri, { useNewUrlParser: true });

var players= null;// = require('../models/player');

client.connect(err => {
    players = client.db(config.mongo.dbname).collection(config.mongo.collectionname);
});

function makefilter(req){
    var filter = [];

        //console.log(filter);


    return filter;
}

exports.search = function(req,res){
    var id = []// makefilter(req);
    players.find({},{ projection: {id: 1, input_skills: 1 }}).toArray(function(err, result) {
        if (err)
            res.send(500);
        else{
            //console.log(result);
            result.forEach(row=>{
                if(row.input_skills.includes(req.query.skill)){
                    //console.log(row.id);
                    id.push(row.id);
                }
            })
        }
        //console.log(filter);
        //res.send(filter);
        res.render('display',{_id: id, skill: req.query.skill});
    });
};

exports.search = function(req,res){
    var id = []// makefilter(req);
    players.find({},{ projection: {id: 1, input_skills: 1 }}).toArray(function(err, result) {
        if (err)
            res.send(500);
        else{
            //console.log(result);
            result.forEach(row=>{
                if(row.input_skills.includes(req.query.skill)){
                    //console.log(row.id);
                    id.push(row.id);
                }
            })
        }
        //console.log(filter);
        //res.send(filter);
        res.render('display',{_id: id, skill: req.query.skill});
    });
};

exports.sm_search = function(req,res){
    var in_id = []
    var out_id = []
    players.find({},{ projection: {id: 1, input_skills: 1,output_skills: 1 }}).toArray(function(err, result) {
        if (err)
            res.send(500);
        else{
            //console.log(result);
            result.forEach(row=>{
                if(row.input_skills.includes(req.query.skill)){
                    //console.log(row.id);
                    in_id.push(row.id);
                }
            })
            result.forEach(row=>{
                if(row.output_skills.includes(req.query.skill)){
                    //console.log(row.id);
                    out_id.push(row.id);
                }
            })
        }
        var combined = in_id.concat(out_id.filter((item) => in_id.indexOf(item) < 0));
        let difference = out_id.filter(x => !in_id.includes(x));
        //console.log(filter);
        //res.send(filter);
        res.render('smartdisplay',{in_id: in_id, difference:difference, skill: req.query.skill});
    });
};

const csvtojson = require('csvtojson');
var db_c = require('../models/db');

const fileName = "/home/acharya/test/csv_python/combined.csv";

exports.get = function (req, res) {
    csvtojson()
        .fromFile(fileName)
        .then((jsonObj) => {
            console.log(jsonObj);
            db_c.insert(jsonObj, function (err, result) {
                if (err)
                    res.send(500);
                else {
                    res.send(200);
                }
            });
        });
}

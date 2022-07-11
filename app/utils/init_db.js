
const csvtojson = require('csvtojson');
var db_c = require('../models/db');

const fileName = "/home/acharya/test/csv_python/combined_2.csv";

exports.get = function (req, res) {
    csvtojson()
        .fromFile(fileName)
        .then((jsonObj) => {
            console.log(jsonObj);
            let data = [];
            //FIXME: fixed to clear the db before update.
            db_c.clear((err, result) => {
                data.push(jsonObj);
            });
            db_c.insert(data, function (err, result) {
                if (err)
                    res.send(500);
                else {
                    res.send(200);
                }
            });
        });
}

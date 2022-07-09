/**
 * Application route resides here.
 */

const router = require("express").Router();

router.get("/", function (req, res) {
    res.send("Hi there!");
});

router.get("/search", require('./views/player.js').search);



module.exports = router;
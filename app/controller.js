/**
 * Application route resides here.
 */

const router = require("express").Router();

router.get("/", function (req, res) {
    res.send("Hi there!");
});

router.get("/search", require('./views/player.js').search);
router.get("/sm_search", require('./views/player.js').sm_search);



router.get("/api/initdb", require('./utils/init_db.js').get);


module.exports = router;
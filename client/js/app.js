var express = require("express");
var parser = require("body-parser");
var app = express();

app.use(parser.json())

app.post("/move", function(request, response) {
    var data = request.body;

    var board = data.board;
    var player = data.player;
    var available_columns = data.available_columns;

    response.setHeader('Content-Type', 'application/json')
    response.send(JSON.stringify({
        'column': available_columns[Math.floor(Math.random()*available_columns.length)]
    }));
});

app.listen(3000);

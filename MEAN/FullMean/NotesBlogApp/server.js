var express = require("express"); // tools on top of node allows to hanle link between node & mongo
var path = require("path");

var app = express();
var bodyParser = require("body-parser");
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }));


app.use(express.static(path.join(__dirname, "./public/dist")));
app.set('view engine', 'ejs');

require('./server/config/mongoose.js');

var routes_setter = require('./server/config/routes.js');
routes_setter(app);

app.get('*', function(req, res){
  res.redirect('/')
})

app.listen(8000, function() {
  console.log("listening on port 8000");
})

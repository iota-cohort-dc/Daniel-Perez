var mongoose = require('mongoose')
var users = require('../controllers/users.js')

module.exports = function(app){


  app.post('/login', function(req, res){
    users.login(req, res);
  });







}

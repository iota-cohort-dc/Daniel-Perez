var mongoose = require('mongoose');
var users = require('../controllers/users.js')
var appt = require('../controllers/appointments.js')


module.exports = function(app){

  app.get('/appointments', function(req, res){
    appt.index(req, res);
  })

  app.post('/login', function(req, res){
    users.login(req, res)
  })

  app.post('appointments/new/:user', function(req, res){
    appt.new(req, res)
  })
  app.delete('/appointments/:id/:user', function(req, res){
    appt.delete(req, res)
  })



}

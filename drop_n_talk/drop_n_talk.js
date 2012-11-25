
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , user = require('./routes/user')
  , http = require('http')
  , path = require('path')
  , sockio = require('socket.io')
  , OpenJTalk = require('../build/Release/openjtalk').OpenJTalk;

var app = express();

var mei = new OpenJTalk();
mei.init("../data/mei_normal", "../openjtalk/open_jtalk_dic_utf_8-1.05");

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view engine', 'jade');
  app.use(express.favicon());
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(app.router);
  app.use(express.static(path.join(__dirname, 'public')));
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.get('/', routes.index);
app.get('/users', user.list);

var server = http.createServer(app);
server.listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});

var io = sockio.listen(server);
io.on('connection', function(socket) {
  socket.on('talk', function(txt) {
    mei.talk(txt);
  });
});

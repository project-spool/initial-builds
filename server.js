/* Load the HTTP library */
var http = require("http");

/* Create an HTTP server to handle responses */
http.createServer(function(request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.write("Rahul you fucken betch \n");
  response.write("Just stop trying to learn node, it's all useless")
  response.end();
}).listen(8888);

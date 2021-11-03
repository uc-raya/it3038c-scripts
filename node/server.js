var fs = require("fs")
var http = require("http");
var ip = require("ip");
const os = require("os");

function getUptime() {
    uptime = os.uptime();
    days = Math.floor(uptime / 86400);
    hours = Math.floor(uptime % (86400) / 3600);
    minutes = Math.floor(uptime % 3600 / 600);
    seconds = Math.floor(uptime % 3600 % 60);
    return ` ${days} Days, ${hours} Hours, ${minutes} Minutes, ${seconds} Seconds`;
}
var server = http.createServer(function(req, res) {
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body) {
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        });    
      }
      else if(req.url.match("/sysinfo")) {
          myHostName=os.hostname();
          totalMemory = ((os.totalmem()) / 1048576);
          freeMemory = ((os.freemem()) / 1048576);
          totalCPUs = os.cpus().length;
          html = `
          <!DOCTYPE html>
                <html>
                <head>
                    <title>Node JS Response</title>
                    </head>
                    <body>
                    <p>Hostname: ${myHostName}</p>
                    <p>IP: ${ip.address()}</p>
                    <p>Server Uptime: ${getUptime()}</p>
                    <p>Total Memory: ${totalMemory} MB</p>
                    <p>Free Memory: ${freeMemory} MB</p>
                    <p>Number of CPUs: ${totalCPUs}</p>
                    </body>
                </html>
          `
          res.writeHead(200, {"Content-Type":"text/html"});
          res.end(html);
       }
      else{
          res.writeHead(400, {"Content-Type": "text/html"});
          res.end(`404 file not found at ${req.url}`);
      }
}).listen(3000)

console.log("Server listening on port 3000");
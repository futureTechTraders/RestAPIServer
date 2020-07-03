/*eslint-env es6*/
/*global require*/
/*global console*/
var express = require('express'); 
var app = express();
  
// Creates a server which runs on port 3000 and  
// can be accessed through localhost:3000
app.listen(3000, function() { 
    console.log('server running on port 3000'); 
} ) 

app.get('/name', function(req, res) {
 
    console.log('Running');
      
    // Use child_process.spawn method from  
    // child_process module and assign it 
    // to variable spawn 
    var spawn = require("child_process").spawn;   
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
    
    if(req.query.indicator == "stock_bot") {
        
        console.log("entered stock bot");
        console.log(req.query.ticker);
        
        // E.g : http://localhost:3000/name?firstname=Levente
        var process = spawn('py',['StockBot.py', 
                            req.query.ticker, req.query.period, req.query.interval, req.query.start, req.query.end, req.query.days]);
  
        // Takes stdout data from script which executed 
        // with arguments and send this data to res object
        var output = '';
        process.stdout.on('data', function(data) {
        
            console.log("Sending Info")
            res.end(data.toString('utf8'));
        });
    
        console.log(output);
    } else if(req.query.indicator == "watchlist") {
        
        console.log("entered watchlist");
        
        // E.g : http://localhost:3000/name?firstname=Levente
        var process = spawn('py',['DataScrape.py', 
                            req.query.ticker]);
  
        // Takes stdout data from script which executed 
        // with arguments and send this data to res object
        var output = '';
        var num = 0;
        process.stdout.on('data', function(data) {
        
            console.log("Sending Info")
            num += 1;
            
            if(num == 2) {
                
                res.end(data.toString('utf8'));
            }
            //output = data.toString('utf8');
            //res.end(data.toString('utf8'));
        });
        
        //console.log(output)
        //res.end(output);
    
        console.log(output);
    }
}); 

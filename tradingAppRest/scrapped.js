// Use child_process.spawn method from  
    // child_process module and assign it 
    // to variable spawn 
    var spawn = require("child_process").spawn;   
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
    
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
    var process = spawn('python',["./apiTest.py", 
                            req.query.firstname]);
  
    // Takes stdout data from script which executed 
    // with arguments and send this data to res object
    var output = '';
    process.stdout.on('data', async function(data) {
        
       let promise = new Promise((resolve, reject) => {
           
           setTimeout(() => resolve("done"), 1000);
       });
        
        let result = await promise;
        alert(result);
        
        return output += data.toString();
const http = require('http')
var express = require('express')

var server = express()
/*
server.post('127.0.0.1',function(request,response){
	response.send('post')
	})
*/	
server.get('/',function(request,response){
	respond.send('get')
	})
/*
const server = http.createServer((request,response)=>{
	console.log('visited')
	response.write('yes')
	response.end()
	})
	*/ 
var client = server.listen(3000,function(){
	var host = client.address().address
	var port = client.address().port
	console.log(host,port)
	
	})
console.log('port 3000')

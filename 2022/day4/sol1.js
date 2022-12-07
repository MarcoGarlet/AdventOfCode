const fs = require('fs');
const fname = './inp.txt';


let data = undefined;

try{
	data = fs.readFileSync(fname,'utf-8');
}catch (err){
	console.log('Error in reading file');
	process.exit(1);	
}

input = data.split('\n').filter(line=>line.length>0);

let res = 0;

for (let line of input){
	[firstG,secondG] = line.split(',');
	[firstGLow,firstGHigh] = firstG.split('-');
	[secondGLow,secondGHigh] = secondG.split('-');
	firstGLow = parseInt(firstGLow), firstGHigh = parseInt(firstGHigh);
	secondGLow = parseInt(secondGLow),secondGHigh = parseInt(secondGHigh)

	let c = (firstGLow<=secondGLow && firstGHigh>=secondGHigh)
	let c1 = (secondGLow<=firstGLow && secondGHigh>=firstGHigh)

	if ( c||c1 ){
		res +=1;
	}
	
}

console.log(res);

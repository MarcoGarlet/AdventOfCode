const fs = require('fs');
const fname = 'inp.txt';

let data = undefined;

try{
	data = fs.readFileSync(fname,'utf-8');
}catch(e){
	console.error('Error in reading ', fname);
	process.exit(1);
}

prog = data.split('\n').filter(line=>line.length>0)

let clock = [];
let v = 1;


function sol(){
	let res=0;
	let clocks_res = [20,60,100,140,180,220];
	for (let clock_res of clocks_res){
		res += clock[clock_res-1][1]*clock_res;
	}
	return res;
}

for (let line of prog){
	let inst = line.split(' ')[0];
	switch(inst){
		case 'addx':
			let arg = parseInt(line.split(' ')[1]);
			clock.push([v,v,v]);
			clock.push([v,v,v+arg]);
			v+=arg;
		break;
		case 'noop':
			clock.push([v,v,v]);
		break;	
	
		default:
		break;
	}

}

console.log(sol())




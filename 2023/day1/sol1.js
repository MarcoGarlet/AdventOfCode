const fs = require('fs');
const fname = 'inp.txt';

let data = undefined;

try{
        data = fs.readFileSync(fname,'utf-8');
} catch(err){
        console.log('Error in reading file');
        process.exit(1);
}


const getNumbers = line => [...line].filter(ch=>Number(ch));
const getFirstLast = numbers => numbers[0]+numbers[numbers.length-1];

data = data.split('\n').filter(line=>line.length>0);

function sol(data){
	const numbers = data.map(line=>Number(getFirstLast(getNumbers(line))));
	return numbers.reduce((number,acc=0)=>acc+number);
}

console.log(sol(data))






const fs = require('fs');
const fname = 'inp.txt';

let data = undefined;

try{
        data = fs.readFileSync(fname,'utf-8');
} catch(err){
        console.log('Error in reading file');
        process.exit(1);
}

spelledNumbers={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
spelledSearchFunct = {};

Object.keys(spelledNumbers).map(spelledNumber=>{spelledSearchFunct[spelledNumber] =  (line)=>line.search(spelledNumber)});

spelledReplaceFunct = {};

Object.keys(spelledNumbers).map(spelledNumber=>{spelledReplaceFunct[spelledNumber] = (line)=>line.replace(spelledNumber)});


const index = (line,word) => line.search(word);
function replaceSpelledNumbers(line){
	replaceStack = [];	
	let newLine = line;
	while(Object.keys(spelledSearchFunct).reduce((acc, k)=> acc || spelledSearchFunct[k](newLine)>=0,false)){
		subArr = Object.keys(spelledSearchFunct).map(k=>({k:k, position:spelledSearchFunct[k](newLine)})).filter(el=>el.position>=0)
		subArr.sort((a,b)=>a.position - b.position);
		newLineArr = [...newLine]
		for (let el of subArr){
			newLineArr[el.position]=spelledNumbers[el.k]
		}
		newLine = [...newLineArr].join('')
	}
	return newLine;	
}

const getNumbers = line => [...line].filter(ch=>Number(ch));
const getFirstLast = numbers => numbers[0]+numbers[numbers.length-1];

data = data.split('\n').filter(line=>line.length>0);
function sol(data){
	newData = [];
	for (let line of data){
		newData.push(replaceSpelledNumbers(line))
	}
	const numbers = newData.map(line=>Number(getFirstLast(getNumbers(line))));
	return numbers.reduce((acc,number)=>acc+number,0);
}

console.log(sol(data))






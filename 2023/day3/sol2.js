const fs = require('fs');
const fname = 'inp.txt';

let data = undefined;

try{
        data = fs.readFileSync(fname,'utf-8');
} catch(err){
        console.log('Error in reading file');
        process.exit(1);
}


data = data.split('\n').filter(line=>line.length>0);

numbers = Array.from(Array(10).keys()).map(c=>String(c))

let regularChar = Array.from(Array(10).keys()).map(c=>String(c))
regularChar.push('.')
let symbolPositions = []

data.map((line,row)=>[...line].map((el,col)=>{
	if(!regularChar.includes(el)){
		symbolPositions.push([row,col,el]);
	}
}));

let numberPositions = [];

for (let row =0; row < data.length; row++){
	let line = data[row];
	let token='';
	for(let i=0; i<line.length;i++){
		if( ((!numbers.includes(line[i]))&&token!=='')|| (i==line.length-1 && numbers.includes(line[i])) ){
			if(i==line.length-1 && numbers.includes(line[i])){
				token+=line[i];
				numberPositions.push([token, row,i-token.length+1,i])
			}
			else{
				numberPositions.push([token,row,i-token.length,i-1])
			}
			token='';
		}
		if(numbers.includes(line[i])){
			token+=line[i];
		}
			
	}
}

let cRow = 0;
let linePut=[];
for(let i=0;i<numberPositions.length;i++){
	let currentRow = numberPositions[i][1];
	if(currentRow!==cRow){
		cRow = currentRow;
		linePut=[numberPositions[i][0]];
	}	
	else{
		linePut.push(numberPositions[i][0]);
		
	}
	
}

let result = {};

for(let numberPosition of numberPositions){
	let number_el = numberPosition[0];
	let number_row = numberPosition[1];
	let number_col = numberPosition[2];
	let number_last_col = numberPosition[3];

	for(let symbolPosition of symbolPositions){
		let symbol_el = symbolPosition[2];
		if(symbol_el!=='*')
			continue
		let symbol_row = symbolPosition[0];
		let symbol_col = symbolPosition[1];
		if (Math.abs(symbol_row-number_row)<2 && (number_col-1<=symbol_col && number_last_col+1>=symbol_col) ){
			//console.log(`pushing ${number_el}\nsymbol_row:${symbol_row};symbol_col:${symbol_col}\nnumber_row:${number_row};number_col:${number_col};number_last_col:${number_last_col};number_el:${number_el}`)
			let candidateKey = String(symbol_row)+' '+String(symbol_col);
			if (!Object.keys(result).includes(candidateKey)){
				result[candidateKey] = [];
			}
			result[candidateKey].push(number_el)
		}
		
	}

}

let final_result = []
for (let k of Object.keys(result)){
	if (result[k].length===2){
		let v = result[k].map(el=>Number(el)).reduce((acc,el)=>acc*el,1);
		final_result.push(v);
	}
}


console.log(final_result.reduce((acc,el)=>acc+el,0))

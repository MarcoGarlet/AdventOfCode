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





function getPoints(winningNumbers,playerNumbers){
	return playerNumbers.filter(number=>winningNumbers.includes(number)).length-1;

}


let result = 0;
for (let cards of data){
	cards = cards.split('|')
	cards[0] = cards[0].split(':')[1].trim().split(' ').filter(n=>n.length>0).map(el=>Number(el));
	cards[1] = cards[1].trim().split(' ').filter(n=>n.length>0).map(el=>Number(el));
	let winningResult=Math.floor(2**getPoints(cards[0],cards[1]));
	result+=winningResult;
}

console.log(result); 

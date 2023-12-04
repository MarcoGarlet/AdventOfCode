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
	return playerNumbers.filter(number=>winningNumbers.includes(number)).length;
}



let copies = 0;
let cardsDataDict = {};
data.map((cards,i)=>{cardsDataDict[i+1]=1});

let index=0;
for (let cards of data){
	let k = index+1;
	cards = cards.split('|')
	cards[0] = cards[0].split(':')[1].trim().split(' ').filter(n=>n.length>0).map(el=>Number(el));
	cards[1] = cards[1].trim().split(' ').filter(n=>n.length>0).map(el=>Number(el));

	let winningResult=getPoints(cards[0],cards[1]);
	for(let i=0;i<winningResult;i++){
		cardsDataDict[k+i+1]+=1*cardsDataDict[k];
	}
	index+=1;
}
for(let k of Object.keys(cardsDataDict)){
	copies+=cardsDataDict[k];
}
console.log(copies); 

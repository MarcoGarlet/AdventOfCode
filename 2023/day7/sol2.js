const data = (
	function readFile (fname){
		const fs = require('fs');
		let data = undefined;
		try{
        		data = fs.readFileSync(fname,'utf-8');
		} catch(err){
        		console.log('Error in reading file');
        		process.exit(1);
		}
		data = data.split('\n').filter(line=>line.length>0);
		return data;
	})('inp.txt');


const cardPoint = {};
const figureSymbols = "TQKA";
Object.keys(Array.from(new Array(10))).slice(2,10).map(card => {cardPoint[card]=Number(card)});
[...figureSymbols].map((symbol,i)=>{cardPoint[symbol]=10+i});
cardPoint['J'] = 1;
const getHand = (line) => {
	return [line.split(' ')[0], Number(line.split(' ')[1])];
}


const transformJolly = (hand) => {
	handNoJ = hand.replaceAll('J','');
	let handSet = [...new Set(handNoJ)];
	let handDict = {};
	let handDictCounter = {};
	handSet.map(handElement=>{handDict[handElement] = [...hand].filter(handChar=>handChar===handElement).length});
	for(let handElement of Object.keys(handDict)){
		if (!handDictCounter[handDict[handElement]])
			handDictCounter[handDict[handElement]] = [handElement];
		else
			handDictCounter[handDict[handElement]].push(handElement); 
	}
	
	const mostFreqCard = Object.keys(handDictCounter).length>0?Math.max(...Object.keys(handDictCounter)):0;
	
	if(handDictCounter[mostFreqCard])	
		handDictCounter[mostFreqCard].sort((a,b)=>{
			if(cardPoint[a]>cardPoint[b])
				return 1;
			return -1;
		});
	let replacedJCard = mostFreqCard<1?'A':handDictCounter[mostFreqCard][0]; 

	return hand.replaceAll('J',replacedJCard)	
	

}

const getPoints = (hand) => {
	let result = 0;
	let handSet = [...new Set(hand)];
	let countArray = handSet.map(handElement=>[...hand].filter(handChar=>handChar===handElement).length);
	
	
	if(handSet.length===1){
		result+=6;
	}	
	else if(handSet.length===2){		
		if(Math.max(...countArray)===4)
			result+=5;
		else
			result+=4;	
	}
	else if(handSet.length===3){
		if(Math.max(...countArray)===3){
			result+=3;
		}
		else{
			result+=2;
		}
	}
	else if(handSet.length===4){
		result+=1;
	}
	else{
		result+=0;
	}
	return result;
}


let handsValue = {};
let handsPoint = {};
Object.keys(Array.from(new Array(7))).map(k=>{handsValue[k]=[]});

for (let line of data){
	let [hand,...point] = getHand(line);
	let handOriginal = hand;
	hand = transformJolly(hand);
	handsPoint[handOriginal]=point[0];
	let handValue = getPoints(hand);
	handsValue[handValue].push(handOriginal);
}


let rankDict = {};
let rank = 1;
for (let point of Object.keys(handsValue)){
	handsValue[point].sort((hand1,hand2)=>{for(let i=0;i<hand1.length;i++){
		if(cardPoint[hand1[i]]>cardPoint[hand2[i]])
			return 1;
		else if(cardPoint[hand1[i]]<cardPoint[hand2[i]])
			return -1;
		else
			continue
	}
		return 0;
	});
	for(let hand of handsValue[point]){
		rankDict[hand]=rank;
		rank+=1;
	}
}
let result = 0;
for (let hand of Object.keys(handsPoint)){
	result+=handsPoint[hand]*rankDict[hand];
}

console.log(result)

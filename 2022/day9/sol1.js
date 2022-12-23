const fs = require('fs');

const fname = './inp.txt';
let data = undefined;

try{
	data = fs.readFileSync(fname,'utf-8');

}catch(err){
	console.log('Error in reading ',fname);
	process.exit(1);
}

data = data.split('\n').filter(line=>line.length>0);



s=[0,0],H=[0,0],T=[0,0]



function is_T_in_range(H,T){
	return [H[0],H[0]+1,H[0]-1].indexOf(T[0]) !== -1 && [H[1]-1,H[1],H[1]+1].indexOf(T[1]) !== -1
}

function updateT(){
	if (T[0]===H[0]){
		if(H[1]>T[1])
			T[1]=H[1]-1;
		else
			T[1]=H[1]+1;

	}	
	else if(T[1]===H[1]){
		if(H[0]>T[0])
			T[0]=H[0]-1;
		else
			T[0]=H[0]+1;

	}	
	else{
		if (is_T_in_range(H,[T[0]+1,T[1]+1])){
			T[0]++;
			T[1]++;
		}
		else if(is_T_in_range(H,[T[0]+1,T[1]-1])){
			T[0]+=1;
			T[1]-=1;
		}
		else if(is_T_in_range(H,[T[0]-1,T[1]+1])){
			T[0]-=1;
			T[1]+=1;
		}
		else{
			T[0]-=1;
			T[1]-=1;
		}
		
	}
}


tail_directions = [];
for (let line of data){
	let [direction,quantity] = line.split(' ');
	quantity = parseInt(quantity);
	for (let i=0;i<quantity;i++){
		switch (direction){
			case 'R':
				H[1]++;
				break;
			case 'L':
				H[1]--;
				break;
			case 'U':
				H[0]--;
				break;
			case 'D':
				H[0]++;
				break;
		
			default:
				break;
		}
		if (!is_T_in_range(H,T)){
			updateT();
		}
		
		tail_directions.push([...T]);
	}


}



console.log([...new Set(tail_directions.map(t=>t[0].toString()+' '+t[1].toString()))].length)



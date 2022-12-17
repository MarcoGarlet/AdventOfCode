const fs = require('fs');
const fname = './inp.txt';

let data = undefined;

try{
	data = fs.readFileSync(fname,'utf-8');
	

}catch(err){
	console.log('Error in reading file');
	process.exit(1);
}


data = data.split('\n').filter(line=>line.length>0);
const matrix = data.map(line=>[...line].map(tree=>parseInt(tree)));

let visible_trees = 0;
let max_score = 0;

function compute_score(elements,element){
	local_score = 0;
	for(let i=0;i<elements.length;i++){
		local_score+=1;
		if (elements[i]>=element)
			break
	}
	return local_score;
}

for (let row=1;row<matrix.length-1;row++){
	for(let col=1;col<matrix[0].length-1;col++){
		let current_element = matrix[row][col];
		let current_row = matrix[row];

		let current_col = [... Array(matrix.length).keys()].map(row_i=>matrix[row_i][col]);
		let right_elements = [...Array(matrix[0].length-(col+1)).keys()].map(right_pos=>current_row[right_pos+col+1]);
		let left_elements = [...Array(col).keys()].map(left_pos=>current_row[left_pos]).reverse();
		let up_elements = [...Array(row).keys()].map(up_pos=>current_col[up_pos]).reverse();
		let down_elements = [...Array(matrix.length-(row+1)).keys()].map(down_pos=>current_col[down_pos+row+1])

		// compute score for current node
	
		let local_score = 0;
		
		local_score=compute_score(right_elements,current_element)*compute_score(left_elements,current_element)*compute_score(up_elements,current_element)*compute_score(down_elements,current_element);
		max_score = (local_score>max_score)?local_score:max_score;	
		
			 
	}

}


console.log(max_score);


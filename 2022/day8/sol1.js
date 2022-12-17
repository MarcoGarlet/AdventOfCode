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

for (let row=1;row<matrix.length-1;row++){
	for(let col=1;col<matrix[0].length-1;col++){
		let current_element = matrix[row][col];
		let current_row = matrix[row];

		let current_col = [... Array(matrix.length).keys()].map(row_i=>matrix[row_i][col]);
		
		let right_elements = [...Array(matrix[0].length-(col+1)).keys()].map(right_pos=>current_row[right_pos+col+1]);
		let left_elements = [...Array(col).keys()].map(left_pos=>current_row[left_pos]);
		let up_elements = [...Array(row).keys()].map(up_pos=>current_col[up_pos]);
		let down_elements = [...Array(matrix.length-(row+1)).keys()].map(down_pos=>current_col[down_pos+row+1])

		
		
		if (current_element>Math.max(...right_elements)||current_element>Math.max(...left_elements)||current_element>Math.max(...up_elements)||current_element>Math.max(...down_elements)){
			visible_trees+=1;

		}
			 
	}

}

visible_trees+=matrix.length*2; // the outernmost top/bottom trees
visible_trees+=(matrix[0].length-2)*2 // the outernmost left/right trees


console.log(visible_trees);


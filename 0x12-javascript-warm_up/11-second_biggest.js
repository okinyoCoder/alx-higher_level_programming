#!/usr/bin/node
/**
 * function that performs bubble sort
 * arranges array items from small to large
*/
function sort(myArr){
	let n = myArr.length;

	// alterate through array items
	for (let i = 0; i < n-1; i++){
		//compare array items through every alteration
		for ( let j = 0; j < n - i -1; j++){
			// values of array are swapped in ascending order
			if (myArr[j] > myArr[j+1]{
				let temp = myArr[j];
				myArr[j] = myArr[j+1];
				myArr[j+1] = temp;
			}
		}
	}
	return myArr;
}

if (process.argv.length <= 3) {
	console.log(0);
} else {
	let arr = sort(process.argv.slice(2, process.argv.length));
	console.log(arr.at(-2));
}

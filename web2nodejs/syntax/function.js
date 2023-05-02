function f123(alpha) {
	for(let i = 0; i < 3; i++) {
		console.log(i);
	}
	for(let j = 0; j < alpha.length; j++) {
		console.log(alpha[j]);
	}
}

f123("ABC");
f123("CDE");
f123("EFG");

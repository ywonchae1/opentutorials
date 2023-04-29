var members = ['egoing', 'k8805', 'hoya'];
console.log(members[1]);
console.log('==========');
var i = 0;
while(i < members.length) {
	console.log(members[i]);
	i = i + 1;
}

var roles = {
	'programmer':'egoing',
	'designer':'k8805',
	'manager':'hoya'
}

console.log('==========');
console.log(roles.designer);
console.log('==========');

for(var name in roles) {
	console.log('object => ', name, 'value => ', roles[name]);
}

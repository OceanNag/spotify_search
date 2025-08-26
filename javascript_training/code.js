var MyName = "Ocean" // used anywhere
let our_name = "Ocean" // used temporarily e.g in a for loop
const pi = 3.14; // ; is optional but it denotes the end of a line
var j = 2 // sometimes you just declare a variable
var MyName = "Jamie"
// console.log(j)
// Most commonly we use let ... = - this is because var won't pick up errors we'd want it to pick up 
// e.g. var Name = Ocean, var Name = James - is fine, but we wouldn't (always) want to have Name defined twice
// j = j ** 2
// console.log(j)
// j = j % 3

// j *= 3
// console.log(j)

k = "I am a \\\n\"string\""
k += "\t finished"
k[0] = "h" // this won't work, you have to change k as a whole
// console.log(k[2])

function word_blank(noun, adjective, adverb, verb){
// example being my big cat is running quickly
var sentence = ""
sentence += "my " + adjective + " " + noun + " is " + verb + "ing " + adverb
return sentence}

// console.log(word_blank("dog", "happy", "slowly", "play"))

// arrays are basically lists, you can even have lists of lists
// you can amend arrays like array[0]=1 
// push = append, pop = pop for the last element -- array.pop(), 
// shift = pop for the first element, unshift - adds element to the beginning


function add_two_numbers(number1, number2){
    return console.log(number1 + number2);
}

// add_two_numbers(3,4)

// var name = Ocean -- this is a global variable
// function blah(){
    // var name2 = Peter -- this is specific to the function 
    // BUT simply
    // name2 = Peter -- this is a global variable, not solely specific to this function (yes this is f dumb)
// }

// console.log(3 === '3') // note 3 !== '3'
// console.log(3 == '3') // this does a type conversion of '3' into a number, which it can and = 3 so 3 == 3 => True

// && = &, || = |, else if = elif

// you can do some long np.where/if function -> easier to do a switch funciton

function test_switching(input_val){
    output = ""
    switch(input_val){
        case 1:
        case 3:
        case 5:
        case 7:
            output = "odd"
            break;
        case 2: 
        case 4:
        case 6:
        case 8:
            output = "even"
            break;
        default:
            output = "neither odd nor even"
    }
    return output
}
// console.log(test_switching(2))
// console.log(test_switching(4))

var count = 0
function cc(card){
    switch(card){
        case "A":
        case "K":
        case "Q":
        case "J":
        case "10":
            count = count - 1
            break;
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
            count = count +1
            break;
        default:
            count = count
    }
    var holdbet = "Hold"
    if (count>5)(
        holdbet = "Hot Hot"
    )
    else if (count > 1){
        holdbet = "Bet"}
    return holdbet
}

function testing_lookup(value){
    var result = ""
    var lookup = {
        "Hattie":"H",
        "Ocean":"O",
        "Jamie":"J"
    }
    result = lookup[value]
    return result
}

// console.log(testing_lookup("Hattie"))

cc(9);cc(4);cc(2);cc(2);cc("A");cc(3);cc(5);cc(6)
console.log(cc(4))
cc("K");cc("J");cc("K");cc("J");cc("K");cc("J")
console.log(cc(2))

// Objects are like classes I'd say
var testObj = {
    name:"Ocean",
    age:29,
    job:"Analyst",
    "work location":"Liverpool Street"
}
console.log(testObj.job)
testObj.job = "Senior Analyst"
testObj.friend = 'Hattie'
console.log(testObj.job)
console.log(testObj.friend)
delete testObj.friend
console.log(testObj.friend)

if (testObj.hasOwnProperty("wife")){
    console.log(testObj.wife);}
else{
    console.log("no wife")}

for (var i=7; i>3;i-=2){
    console.log("hi person number "+i)
}

function testing_equal2or4(value){
    return value === 2 ? "equal2": value === 4 ? "equal4": "neither"
}
console.log(testing_equal2or4(3))
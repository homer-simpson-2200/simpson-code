import {user, user_stack, Log, multiplication, Multiplication, Multiplication1, Multiplication2, init, print} from './user_stack'

let hellots: string = "hello", worldts = "world", typets: any = "typescript", user: {name: string; passward: string; premium?: boolean} = {name: 'homer', passward: '1234', premium: true};
console.log(`${hellots} ${typets} ${worldts}`)

let User: {
    Name: string; Passward: string; Premium?: boolean
} = {Name: 'homer', Passward: '1234', Premium: true}

if (user.premium == true && User.Premium == true) {
    console.log(`${user.name} is premium!`)
}

let nuser: user_stack = {username: "homer", userpassward: "1234", isp: false}, puser: user_stack = {username: "himer", userpassward: "1111", isp: true}, puserinput: user = {username: "himer", userpassward: "1111", isp: true};

if (puserinput.isp == true) {
    let nconsole: Log = new Log(puser.username, puser.userpassward, puserinput.username, puserinput.userpassward, puserinput.isp);
    nconsole.hellouser();
}
else {
    let nconsole: Log = new Log(nuser.username, nuser.userpassward, puserinput.username, puserinput.userpassward, puserinput.isp);
    nconsole.hellouser();
}

let Multiplication3 = (function(a: number, b: number) {return a*b})(1, 2)

let what_is_anonymous_function = Multiplication3

console.log(what_is_anonymous_function)

let hellohomer = print("homer")

init(() => console.log("callback function"), "callback")

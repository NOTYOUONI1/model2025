class user {
    constructor(name,email){
        this.name = name
        this.email = email
    }
    viewdata(){
        console.log('data','name :',this.name,'email :',this.email)
    }
}



let g = new user("rakib","sorry")
import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';
import { User } from '../../assets/models/User';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace

@Component({
	selector: 'app-login',
	templateUrl: './login.component.html',
	styleUrls: ['./login.component.css'],
	template: '<div><h1>JOLA</h1><app-home [userHome] = "user"></app-home></div>'
})
export class LoginComponent implements OnInit {

	user: User = new User();
	email = "";
	errors: any;

	constructor(
		private _http: UserService,
	) { }

	ngOnInit(){
		if(sessionStorage.getItem("userEmail")){
			this.loginUser(sessionStorage.getItem("userEmail"))
		}
	}

	newUser(){
		let temp = this._http.saveUser(this.user);
		temp.subscribe(
			data => {
				this.errors = "";
				if(data["errors"]){
					this.errors = data["errors"];
					console.log("This is an Error #3001 ", data);
				}else{
					this.user = data["user"];
					// console.log("Login: User:", this.user);
					sessionStorage.setItem("userEmail", this.user.email)
				}
			},
			error => {
				console.log("Something went wrong #2001.", error);
			},
			() => {
			}
		);
	}

	onSubmit(){
		this.newUser();
	}

	onLogin(){
		if(this.email.length > 0){
			this.loginUser(this.email.trim());
		}
	}

	loginUser(userEmail){
		let temp = this._http.loginUser({email: userEmail});
		temp.subscribe(
			data => {
				this.errors = "";
				if(data["errors"]){
					this.errors = data["errors"];
					console.log("This is an Error #2003 ", data);
				}else{
					this.user = data["user"];
					// console.log("Login: User:", this.user);
					sessionStorage.setItem("userEmail", this.user.email)
				}
			},
			err => {
				console.log("Something went wrong #2002.", err);
			}
		);
	}
}

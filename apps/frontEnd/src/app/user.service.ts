import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from '../assets/models/User';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace

@Injectable({
	providedIn: 'root'
})

export class UserService {

	baseUrl = 'http://localhost:8000/';
	// baseUrl = 'http://3.12.132.128:8000/';
	// baseUrl = '/';

	constructor(private _http: HttpClient) { }

	// user is an objet from Models --> User
	saveUser(user: User){
		return this._http.post(
			this.baseUrl + 'user/new', 
			user
		)
	}

	loginUser(email: object){
		return this._http.post(
			this.baseUrl + "user/login",
			email
		);
	}

	logOut(){
		return this._http.get(this.baseUrl + "user/logout")
	}
}


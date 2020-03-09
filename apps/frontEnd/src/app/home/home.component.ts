import { Component, OnInit, Input } from '@angular/core';
import { User } from '../../assets/models/User';
import { UserService } from '../user.service';
import { Router, ActivatedRoute } from '@angular/router';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.css']
	

})
export class HomeComponent implements OnInit {

	@Input() user: User;
	errors: any;

	constructor(
		private _httpUser: UserService,
		private _router: Router
	) {}

	ngOnInit(): void {
	}

	onLogOut(){
		let temp = this._httpUser.logOut();
		sessionStorage.clear()
		temp.subscribe(
			data => {
				this._router.navigateByUrl('/');
			},
			err => {
				console.log("Something went wrong #2002.", err);
			},
			() => {
			}
		);
	}

}

import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace eofline

@Component({
	selector: 'app-user',
	templateUrl: './user.component.html',
	styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

	users: any

	constructor(private _http: UserService) {  }

	ngOnInit(): void {
	}
}
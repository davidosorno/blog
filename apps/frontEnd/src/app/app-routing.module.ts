import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace

const routes: Routes = [
	{ path: '', component: LoginComponent},
	// { path: 'users', component: UserComponent},
	// { path: 'post', component: PostComponent },
	// { path: 'comment', component: CommentComponent },
	// use a colon and parameter name to include a parameter in the url
	// redirect to /alpha if there is nothing in the url
	{ path: '', pathMatch: 'full', redirectTo: ''},
	// the ** will catch anything that did not match any of the above routes
	{ path: '**', pathMatch: 'full', redirectTo: ''},
];

@NgModule({
	imports: [RouterModule.forRoot(routes)],
	exports: [RouterModule]
})
export class AppRoutingModule { }

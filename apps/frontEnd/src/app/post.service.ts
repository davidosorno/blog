import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Post } from '../assets/models/Post';
import { User } from 'src/assets/models/User';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace

@Injectable({
	providedIn: 'root'
})
export class PostService {

	// baseUrl = 'http://127.0.0.1:8000/';
	baseUrl = 'http://3.12.132.128:8000/';

	constructor(private _http: HttpClient) { }

	getPosts(userId){
		return this._http.get(this.baseUrl + `home/getPosts/${userId}`);
	}

	savePost(post: Post){
		return this._http.post(
			this.baseUrl + 'post/new', 
			post
		)
	}

	deletePost(postId, user: User){
		return this._http.post(
			this.baseUrl + 'post/delete',
			{
				user,
				postId
			}
		)
	}

	reportPostSpam(postId: object){
		return this._http.put(
			this.baseUrl + 'post/spam',
			postId
		)
	}
}
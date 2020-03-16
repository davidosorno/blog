import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Comment } from 'src/assets/models/Comment';
import { User } from 'src/assets/models/User';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace eofline

@Injectable({
	providedIn: 'root'
})
export class CommentService {

	// baseUrl = 'http://127.0.0.1:8000/';
	baseUrl = 'http://3.12.132.128:8000/';

	constructor(private _http: HttpClient) {}

	saveComment(comment: Comment){
		return this._http.post(
			this.baseUrl + 'comment/new', 
			comment
		)
	}

	getComments(userId, postId){
		return this._http.get(this.baseUrl + `home/getComments/${userId}/${postId}`);
	}

	deleteComment(idComment, idPost, user: User){
		// console.log(idComment, user);
		return this._http.post(
			this.baseUrl + 'comment/delete',
			{
				user,
				idComment,
				idPost
			}
		)
	}

	reportCommentSpam(idComment: object){
		return this._http.put(
			this.baseUrl + 'comment/spam',
			idComment
		)
	}
}

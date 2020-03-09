import { Component, OnInit, Input } from '@angular/core';
import { CommentService } from '../comment.service';
import { User } from 'src/assets/models/User';
import { Comment } from 'src/assets/models/Comment';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace eofline

@Component({
	selector: 'app-comment',
	templateUrl: './comment.component.html',
	styleUrls: ['./comment.component.css']
})
export class CommentComponent implements OnInit {

	@Input() currentUser: User = new User();
	@Input() postId = 0;
	@Input() commentList: Comment[];
	comment: Comment = new Comment();
	errors: any;

	constructor(
		private _http: CommentService
	) { }

	ngOnInit(): void {
		this.getComments()
	}

	onSubmit(){
		this.saveComment()
	}

	saveComment(){
		this.comment.userCommentFK = this.currentUser.id
		this.comment.postCommentsFK = this.postId
		let temp = this._http.saveComment(this.comment)
		temp.subscribe(
			data => {
				if(data["errors"]){
					this.errors = data["errors"];
					console.log("This is an Error #8003", data);
				}else{
					this.getComments();
					this.comment = new Comment();
				}
			},
			err => {
				console.log("Something went wrong #8002.", err);
			},
			() => {
			}
		);
	}

	getComments(){
		let temp = this._http.getComments(this.currentUser.id, this.postId)
		temp.subscribe( 
			data => {
				if(data["errors"]){
					this.errors = data["errors"];
					console.log("This is an Error #8003 ", data);
				}else{
					this.commentList = data["comments"];
					console.log(this.commentList);
				}
			},
			error => {
				console.log("Something went wrong #8001.", error);
			},
			() => {}
		)
	}

	reportSpam(idComment){
		if(confirm('Do you want to report this Comment as spam?')){
			let temp = this._http.reportCommentSpam({idComment})
			temp.subscribe(
				data => {
					if(data["errors"]){
						this.errors = data["errors"];
						console.log("This is an Error #8004 ", data);
					}else{
						this.getComments();
					}
				},
				err => {
					console.log("Something went wrong #8005.", err);
				},
				() => {
				}
			);
		}
	}

	deleteComment(idComment){
		if(confirm('Are you sure to Delete the Comment?')){
			// let temp = this._http.deletePost(postId, this.currentUser.id)
			let temp = this._http.deleteComment(idComment, this.postId, this.currentUser)
			temp.subscribe(
				data => {
					if(data["errors"]){
						this.errors = data["errors"];
						console.log("This is an Error #2004 ", data);
					}else{
						this.getComments();
					}
				},
				err => {
					console.log("Something went wrong #2005.", err);
				},
				() => {
				}
			);
		}
	}
}

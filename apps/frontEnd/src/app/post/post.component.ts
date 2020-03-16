import { Component, OnInit, Input } from '@angular/core';
import { User } from 'src/assets/models/User';
import { Post } from 'src/assets/models/Post';
import * as $ from 'jquery';
import { PostService } from '../post.service';

// tslint:disable: indent quotemark curly whitespace align semicolon prefer-const no-string-literal one-line variable-name
// tslint:disable: no-trailing-whitespace eofline

@Component({
	selector: 'app-post',
	templateUrl: './post.component.html',
	styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit {

	@Input() currentUser: User = new User();
	post: Post = new Post();
	postList: Post[];
	errors: any;

	comments: Comment[]

	constructor(
		private _http: PostService
	) {}

	ngOnInit(): void {
		this.getPosts()
		// Activate jQuery function
		$( () => {
			$(document).ready(() =>{
				hideAll();
			});
		})
	}

	getPosts(){
		let temp = this._http.getPosts(this.currentUser.id)
		temp.subscribe( 
			data => {
				this.errors = "";
				if(data["errors"]){
					this.errors = data["errors"];
					console.log("This is an Error #7003 ", data);
				}else{
					this.postList = data["posts"];
					// console.log(this.postList);
				}
			},
			error => {
				console.log("Something went wrong #7001.", error);
			},
			() => {}
		)
	}

	onSubmit(){
		this.savePost()
	}

	savePost(){
		this.post.userPostsFK = this.currentUser.id
		let temp = this._http.savePost(this.post)
		temp.subscribe(
			data => {
				if(data["errors"]){
					this.errors = data["errors"];
					console.log("This is an Error #2003", data);
				}else{
					this.getPosts();
					this.post = new Post();
				}
			},
			err => {
				console.log("Something went wrong #2002.", err);
			},
			() => {
			}
		);
	}

	reportSpam(idPost){
		if(confirm('Do you want to report this Post as spam?')){
			let temp = this._http.reportPostSpam({postId: idPost})
			temp.subscribe(
				data => {
					if(data["errors"]){
						this.errors = data["errors"];
						console.log("This is an Error #2004 ", data);
					}else{
						this.getPosts();
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

	deletePost(postId){
		if(confirm('Are you sure to Delete the Post?')){
			// let temp = this._http.deletePost(postId, this.currentUser.id)
			let temp = this._http.deletePost(postId, this.currentUser)
			temp.subscribe(
				data => {
					if(data["errors"]){
						this.errors = data["errors"];
						console.log("This is an Error #2004 ", data);
					}else{
						this.getPosts();
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

	callSldTogg(postId, event: Event){
		sldTogg(postId, event);
	}
}

// ************ JQUERY FUNCTION ************ 
function sldTogg(control, event = null){
	let getControl = document.getElementById("postComments"+control);
	$(getControl).slideToggle("slow");
	if(event){
		event.preventDefault();
	}
}

function hideAll(){	
	let elements = document.getElementsByTagName("div")
	for (let i = 0; i < elements.length; i++) {
		if(elements[i].className === "posts"){
			sldTogg(elements[i].id.substr(12));
		}
	}
}
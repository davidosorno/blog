export class Comment {
    id = 0;
    comment = '';
    createdAt: Date;
    updatedAt: Date;
    spam: boolean;
    userCommentFK = 0;
    postCommentsFK = 0;
}

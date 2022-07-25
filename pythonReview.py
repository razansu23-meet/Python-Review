def create_youtube_video(title , description):
	video = {"title" : title , "description" :  description , "likes" : 0 , "dislikes" : 0 , "comments" : {}}
	return video

def like(video):
	if "likes" in video:
		video["likes"] +=1
	return video 

def dislike(video):
	if "dislikes" in video:
		video["dislikes"] +=1
	return video 

def add_commment(youtubevideo , username , comment_text):
	youtubevideo["comments"][username] = comment_text
	return youtubevideo

video = create_youtube_video("ASMR destroying makeup" , "fun video")
like(video)
dislike(video)
add_commment(video)
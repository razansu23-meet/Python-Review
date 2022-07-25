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
for i in range(496):
	video = like(video)
video = dislike(video)
video = add_commment(video , "user" , "hey")
print(video)

def hasht():
	lst = []
	i = 0
	a=0
	print("enter space to stop")
	while a!=' ' and i<5:
		a = input()
		lst.append(a)
		i+=1
	if " " in lst:
		lst.remove(" ")
	return lst

#create_youtube_video["hashtag"] = lst


v1 = create_youtube_video("ASMR destroying makeup" , "fun video")
v2 = create_youtube_video("ASMR idk" , "fun video2")
v1["hashtag"] = hasht()
v2["hashtag"] = hasht()
def similarity_to_video(v1 , v2):
	s = 0
	for k in v1["hashtag"]:
		for j in v2["hashtag"]:
			if k == j:
				s+=1
	return s/5.0 * 100
print(similarity_to_video(v1 , v2))


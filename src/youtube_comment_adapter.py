import pytchat
import json

class YoutubeCommentAdapter:
    def __init__(self, video_id: str) -> None:
        self.chat = pytchat.create(video_id=video_id, interruptable=False)

    def get_comment(self):
        comments = self.__get_comments()
        if (comments == None):
            return None
        
        recent_comment = comments[-1].get("message")
        print("最新のコメント: " + recent_comment)
        return recent_comment
    
    def __get_comments(self):
        if (self.chat.is_alive() == False):
            print("配信が開始されていません。")
            return None
        
        comments = json.loads(self.chat.get().json())
        if (comments == []):
            print("最新コメントはありません")
            return None
        
        return comments


if __name__ == "__name__":
    import time
    video_id = "video"
    chat = YoutubeCommentAdapter(video_id=video_id)
    time.sleep(1)
    print(chat.get_comment())


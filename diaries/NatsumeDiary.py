from diaries.AbstractDiary import AbstractDiary

class NatsumeDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "今までgithubから逃げ続けてきたので、今すごくつらい。"
    
    def get_author(self):
        return "natsume"

from diaries.AbstractDiary import AbstractDiary

class OguraDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-12"
    
    def get_summary(self):
        return "サンシャイン水族館に行った。"
    
    def get_author(self):
        return "小倉"
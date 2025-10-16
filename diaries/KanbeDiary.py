from diaries.AbstractDiary import AbstractDiary
class KanbeDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    
    def get_summary(self):
        return "充電器わすれた。"
    
    def get_author(self):
        return "Kanbe"
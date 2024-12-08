from article import Article

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        
        self._name = name
        self._articles = []
        
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set(article.magazine for article in self._articles))
    
    def write_article(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
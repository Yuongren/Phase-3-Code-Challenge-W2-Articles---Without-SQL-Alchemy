class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        
        self._name = name
        self._category = category
        self._articles = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise ValueError("Category must be a string")
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = new_category
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list(set(article.author for article in self._articles))
    
    def publish_article(self, article):
        if isinstance(article, Article):
            self._articles.append(article)
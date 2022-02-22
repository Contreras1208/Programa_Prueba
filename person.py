class Person:
    def __init__(self, name, email) ->None:
        self.name=name
        self.email=email
        
        
    def __repr__(self) -> str:
        return f"Person('{self.name}',{self.email}')"
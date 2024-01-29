class RequiredParam:
    def __init__(self, name: str, col_index: int):
        self.name = name
        self.col_index = col_index
        self.cell = None
        self.value = None
        
        self.is_required = True
        self.is_conditional = False
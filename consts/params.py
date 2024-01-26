class Chandeliers:
    def __init__(self):
        self.params = [{
            "value": "pl:42",
            "is_required": True
        }, 
        {
            "value": "pi:20",
            "is_required": True
        }
    ]

    def check_condition(self):
        if self.params[0]
from dataclasses import dataclass

@dataclass
class RequiredParamType:
    name: str
    col_index: int
    value: str
    is_required: bool
    is_conditional: bool


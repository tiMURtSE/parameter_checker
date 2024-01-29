from dataclasses import dataclass
from typing import List
from openpyxl.cell.cell import Cell

@dataclass
class RequiredParamType:
    name: str
    col_index: int
    value: str
    is_required: bool
    is_conditional: bool

@dataclass
class ProductType:
    id: int
    category: str
    row: tuple[Cell]
    required_params: List[RequiredParamType]
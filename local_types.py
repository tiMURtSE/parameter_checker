from dataclasses import dataclass
from typing import List
from openpyxl.cell.cell import Cell

@dataclass
class RequiredParamType:
    name: str
    col_index: int
    cell: Cell
    value: str
    is_required: bool
    is_conditional: bool

@dataclass
class ProductType:
    id: int
    category: str
    required_params: List[RequiredParamType]
    row: tuple[Cell]
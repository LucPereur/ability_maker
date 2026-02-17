from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field

# ============================================
# Parapsy Mode Enum
# ============================================

class parapsyMode(Enum):
    TELEPATHY = "telepathy"
    TELEKINSIS = "telekinesis"


# ============================================
# Parapsy JSON Schema Models (Tree Structure)
# ============================================

class SchemaItem(BaseModel):
    """Leaf node: Individual item in the schema (6 per sublist)"""
    item_name: str
    item_value: int = Field(ge=0, le=5)
    item_description: str
    item_description_alt: Optional[str] = None


class SchemaSublist(BaseModel):
    """Branch node: Contains 6 items"""
    sublist_name: str
    sublist_description: str = ""
    items: list[SchemaItem] = Field(min_length=6, max_length=6)


class SchemaList(BaseModel):
    """Branch node: Contains multiple sublists"""
    list_name: str
    list_description: str
    sublists: list[SchemaSublist]


class SchemaModeDefinition(BaseModel):
    """Root node: Complete mode definition (3 lists)"""
    noun: str
    adjective: str
    general_description: str
    lists: list[SchemaList] = Field(min_length=3, max_length=3)


class ParapsySchema(BaseModel):
    """Top-level: Contains all mode definitions"""
    telepathy: SchemaModeDefinition
    telekinesis: SchemaModeDefinition


# ============================================
# API/Service Models (for ability composition)
# ============================================

class abilityDescription(BaseModel):
    ability_description: str

class compositionItem(BaseModel):
    list_name: str = ""
    sublist_name: str = ""
    sublist_description: str = ""
    sublist_items: list[SchemaItem] = Field(min_length=6, max_length=6, default=[])
    sublist_selection: SchemaItem = None
    prompt_terms: Optional[str] = None

    def update(self, schema_sublist: SchemaSublist):
        self.sublist_name = schema_sublist.sublist_name
        self.sublist_description = schema_sublist.sublist_description
        self.sublist_items = schema_sublist.items

class abilityComposition(BaseModel):
    """Final ability composition with selected items"""
    parapsy_mode: parapsyMode
    composition: list[compositionItem] = Field(default_factory=list)

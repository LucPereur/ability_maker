from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field

# ============================================
# Parapsy Mode Enum
# ============================================

class parapsyMode(Enum):
    TELEPATHY = "telepathy"
    TELEKINESIS = "telekinesis"


# ============================================
# Parapsy JSON Schema Models (Tree Structure)
# ============================================

class SchemaItem(BaseModel):
    """Leaf node: Individual item in the schema (6 per sublist)"""
    item_name: str
    item_value: int = Field(ge=0, le=5)
    item_description: str
    item_description_alt: Optional[str] = None
    quantitative_effect: Optional[str] = None

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
    name: str
    noun: str
    adjective: str
    general_description: str
    lists: list[SchemaList] = Field(min_length=3, max_length=3)


class ParapsySchemaList(BaseModel):
    """Top-level: Contains all mode definitions"""
    schemas: list[SchemaModeDefinition]


# ============================================
# API/Service Models (for ability composition)
# ============================================

class abilityDescription(BaseModel):
    ability_description: str

class compositionItem(BaseModel):
    list: SchemaList = None
    sublist: SchemaSublist = None
    sublist_selection: SchemaItem = None
    prompt_terms: Optional[str] = None
    
    def composition_item_summary(self):
        if self.sublist_selection and self.list and self.sublist:
            return f"""
            - {self.sublist.sublist_name} : {self.sublist.sublist_description}
            Valeur {self.sublist_selection.item_value} => {self.sublist_selection.item_name} : {self.sublist_selection.item_description}"""

class abilityComposition(BaseModel):
    """Final ability composition with selected items"""
    ability_name: Optional[str] = None
    ablity_description: Optional[str] = None
    parapsy_mode: parapsyMode
    composition: list[compositionItem] = Field(default_factory=list)

    def composition_summary(self):
        summary = []
        if len(self.composition) > 0:
            list_names = list(set([item.list.list_name for item in self.composition]))
            for list_name in list_names:
                item_from_list = [item for item in self.composition if item.list.list_name == list_name]
                first_one = True
                for item in item_from_list:
                    if first_one:
                        summary.append(f"*{item.list.list_name.capitalize()} : {item.list.list_description.capitalize()}*")
                        first_one = False
                    summary.append(item.composition_item_summary())
            return "\n".join(summary)
import json
from app.api.models import ParapsySchema, parapsyMode, abilityComposition
from app.core.config import settings

class schemaLoader():
    def __init__(self):
        pass

    def _validate(self, schema: ParapsySchema):
        """Validate schema structure"""
        try:
            # This would fail if JSON doesn't have exactly 3 lists
            for mode_def in [schema.telepathy, schema.telekinesis]:
                assert len(mode_def.lists) == 3, "Must have 3 lists"
                for parapsy_list in mode_def.lists:
                    for sublist in parapsy_list.sublists:
                        assert len(sublist.items) == 6, "Must have 5 items"
            return schema
        except Exception as e:
            print(f"✗ Schema validation failed: {e}")
            raise

    def load_schema(self) -> ParapsySchema:
        """Load and validate the entire JSON schema"""
        with open(settings.PATH_TO_JSON, 'r') as f:
            data = json.load(f)

        # Unpack the dict into ParapsySchema
        schema = ParapsySchema(**data)

        # Validate and return
        return self._validate(schema)
    
def print_schema(schema: ParapsySchema):
    """Example: Navigate the tree with full type safety"""

    telepathy = schema.telepathy
    print(f"Mode: {telepathy.noun}")
    print(f"Adjective: {telepathy.adjective}")
    print(f"Description: {telepathy.general_description[:50]}...\n")

    for list_idx, parapsy_list in enumerate(telepathy.lists):
        print(f"List {list_idx + 1}: {parapsy_list.list_name}")

        for sublist_idx, sublist in enumerate(parapsy_list.sublists):
            print(f"  Sublist {sublist_idx + 1}: {sublist.sublist_name}")

            for item in sublist.items:
                print(f"    Item {item.item_value}: {item.item_name} --- {item.item_description}")

if __name__ == "__main__":
    loader = schemaLoader()
    schema = loader.load_schema()
    print_schema(schema=schema)
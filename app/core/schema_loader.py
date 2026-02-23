import json
from app.api.models import ParapsySchemaList, parapsyMode, SchemaModeDefinition
from app.core.config import settings

class schemaLoader():
    def __init__(self):
        pass

    def _validate(self, to_validate: ParapsySchemaList | SchemaModeDefinition ):
        try:
            if isinstance(to_validate, SchemaModeDefinition):
                assert len(to_validate.lists) == 3, "Must have 3 lists"
                for parapsy_list in to_validate.lists:
                    for sublist in parapsy_list.sublists:
                        assert len(sublist.items) == 6, "Must have 5 items"
            elif isinstance(to_validate, ParapsySchemaList):
                for mode_def in to_validate.schemas:
                    assert len(mode_def.lists) == 3, "Must have 3 lists"
                    for parapsy_list in mode_def.lists:
                        for sublist in parapsy_list.sublists:
                            assert len(sublist.items) == 6, "Must have 5 items"
            return to_validate
        except Exception as e:
            print(f"✗ Schema validation failed: {e}")
            raise

    def load_all_schemas(self) -> ParapsySchemaList:
        with open(settings.PATH_TO_JSON, 'r') as f:
            data = json.load(f)

        schema_list = ParapsySchemaList(**data['schemas'])
        return self._validate(schema_list)

    def load_schema(self, parapsy_mode: parapsyMode) -> SchemaModeDefinition:
        with open(settings.PATH_TO_JSON, 'r') as f:
            data = json.load(f)
            data_selection = next((mode for mode in data['schemas'] if mode['name'] == parapsy_mode.value))

        data_selection = SchemaModeDefinition(**data_selection)
        return self._validate(data_selection)
    
def print_schema(schema_list: ParapsySchemaList):

    for schema in schema_list.schemas:
        print(f"Mode: {schema.noun}")
        print(f"Adjective: {schema.adjective}")
        print(f"Description: {schema.general_description[:50]}...\n")

        for list_idx, parapsy_list in enumerate(schema.lists):
            print(f"List {list_idx + 1}: {parapsy_list.list_name}")

            for sublist_idx, sublist in enumerate(parapsy_list.sublists):
                print(f"  Sublist {sublist_idx + 1}: {sublist.sublist_name}")

                for item in sublist.items:
                    print(f"    Item {item.item_value}: {item.item_name} --- {item.item_description}")

if __name__ == "__main__":
    loader = schemaLoader()
    schema_list = loader.load_all_schemas()
    print_schema(schema_list=schema_list)
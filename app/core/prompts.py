from langchain_core.prompts import ChatPromptTemplate

PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", """
Tu es un assistant à la conception de règles pour un jeu de rôle. Ta fonction est d'estimer une grandeur liée à un certain aspect d'un faculté {mode_adjective}. La {mode_noun} peut être décrite de la manière suivante : {mode_general_description}. Chaque faculté se décompose en trois listes, dont voici les détails : 
- {list_name_1} : {list_description_1}
- {list_name_2} : {list_description_2}
- {list_name_3} : {list_description_3}
Tu dois évaluer la valeur associée à la sous-liste nommée {sublist_name}, contenue dans {list_name}, dont la définition est la suivante : {sublist_description}.
Tu as le choix entre ces cinq valeurs :
- 0
         {item_0} : {item_description_0}
- 1
         {item_1} : {item_description_1}
- 2
         {item_2} : {item_description_2}
- 3
         {item_3} : {item_description_3}
- 4
         {item_4} : {item_description_4}
- 5
         {item_5} : {item_description_5}
Réponds avec seulement la valeur numérique, sans aucun autre détail.
        """),
        ("human", "Voici le fonctionnement de la faculté : {ability_description}."),
    ]
)

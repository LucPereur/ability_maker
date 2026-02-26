from langchain_core.prompts import ChatPromptTemplate

COMPOSITION_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", """
Tu es un assistant à la conception de règles pour un jeu de rôle. Ta fonction est d'estimer une grandeur liée à un certain aspect d'une faculté {mode_adjective}. La {mode_noun} peut être décrite de la manière suivante : {mode_general_description}. Chaque faculté se décompose en trois listes, dont voici les détails : 
- {list_name_1} : {list_description_1}
- {list_name_2} : {list_description_2}
- {list_name_3} : {list_description_3}
Tu dois évaluer la valeur associée à la sous-liste nommée {sublist_name}, contenue dans {list_name}, dont la définition est la suivante : {sublist_description}. Limite ton choix strictement à ce qui est contenu dans la description de la faculté, ne suppose rien.
Tu as le choix entre ces six valeurs :
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


DESCRIPTION_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", """
Tu es un assistant à la conception de règles pour un jeu de rôle. Ta fonction est d'attribuer une description à une faculté parapsychique en fonction de sa composition et d'une description basique.
- La composition de cette faculté est constituée de trois listes, chacune contenant plusieurs valeurs définissant ses limites et la description est un résumé concis de ce en quoi elle consiste.
- La description finale doit contenir tous les aspects importants de la composition, souligner les limites issues de cette dernière.
- Utilise les information de la composition uniquement pour raffiner et préciser la faculté contenue dans la description basique fournie.
- Une faculté équivaut à une seule action. La description finale doit faire référence uniquement à une action parapsychique, et ne doit en aucun cas accumuler des possibilités ou variations.
- La description finale doit être concise tout en étant exhaustive. Elle ne doit pas dépasser 200 mots, et peut mentionner le détenteur de la faculté sous le terme "le Parapsy" (ex: le Parapsy est capable de...). Ne cite les détails de la composition que si c'est directement lié à l'idée de base de la faculté.
- Réponds uniquement avec la description, sans aucun détail suppélmentaire.
        """),
        ("human", """
La faculté se compose de la manière suivante :
{composition_summary}
et sa description basique est la suivante :
{ability_description}
        """),
    ]
)

TITLE_PROMPT_TEMPLATE = ChatPromptTemplate.from_messages(
    [
        ("system", """
Tu es un assistant à la conception de règles pour un jeu de rôle.
        """),
        ("human", ""),
    ]
)
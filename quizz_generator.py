import re
import json


import json
import random


def parse_quiz_text(text):
    # Utiliser une expression régulière pour extraire les questions et réponses
    pattern = r"(\d+)\. \*\*Question\*\*: (.*?)\s+\*\*Réponse\*\*: (.*?)\s+(?=\d+\. \*\*Question\*\*:|$)"
    matches = re.findall(pattern, text, re.DOTALL)

    quizzes = []
    for match in matches:
        id, question, answer = match
        # Ajouter chaque question et réponse dans la liste des quizzes
        quizzes.append({
            "id": int(id),
            "question": question.strip(),
            "answer": answer.strip()
        })

    # Retourner le JSON structuré
    return json.dumps({"quizzes": quizzes}, indent=4, ensure_ascii=False)

# Exemple de texte de quiz
quiz_text = """
1. **Question**: Qu'est-ce que C# ?  
   **Réponse**: C# est un langage de programmation utilisé pour créer des programmes et des jeux sur des ordinateurs.

2. **Question**: À quoi sert un langage de programmation comme C# ?  
   **Réponse**: Il sert à donner des instructions à un ordinateur pour qu'il sache quoi faire.

3. **Question**: Qu'est-ce que l'on peut faire avec C# ?  
   **Réponse**: On peut développer des jeux, des applications pour Windows, ou des sites web.

4. **Question**: Quels sont les types de constructions que l'on peut utiliser dans C# ?  
   **Réponse**: On utilise des commandes spéciales qui aident l'ordinateur à comprendre ce qu'il doit faire.

5. **Question**: Qu'est-ce qu'un algorithme ?  
   **Réponse**: Un algorithme, c'est comme une recette de cuisine, une série d'instructions pour résoudre un problème ou accomplir une tâche.

6. **Question**: Que signifie "structures de données" en programmation ?  
   **Réponse**: Ce sont des manières d'organiser l'information dans un programme pour qu'elle soit facile à utiliser.

7. **Question**: Pourquoi est-il important de connaître différents types de données dans C# ?  
   **Réponse**: Chaque type de donnée est adapté à certaines tâches, donc savoir les utiliser aide à écrire de meilleurs programmes.

8. **Question**: Qu'est-ce qu'un programme ?  
   **Réponse**: Un programme est un ensemble d'instructions que l'on donne à l'ordinateur pour qu'il réalise des tâches.

9. **Question**: Pourquoi utilise-t-on C# dans beaucoup de scénarios différents ?  
   **Réponse**: Parce qu'il est très flexible et puissant, ce qui permet de l'utiliser dans beaucoup de projets différents.

10. **Question**: Qu'est-ce qu'une "introduction brève" dans le contexte de l'apprentissage de C# ?  
    **Réponse**: Cela signifie qu'on explique les idées de base de C# rapidement sans entrer dans tous les détails.

11. **Question**: Pourquoi ce texte ne serait pas un cours complet sur C# ?  
    **Réponse**: Parce qu'il donne seulement une description rapide des idées principales sans aller trop en profondeur.

12. **Question**: Qu'est-ce que cela signifie quand on dit que C# a de "larges possibilités" ?  
    **Réponse**: Cela veut dire que l'on peut utiliser C# pour beaucoup de types de projets différents.


"""

# Appeler la fonction et imprimer le résultat
# json_output = parse_quiz_text(quiz_text)
# print(json_output)


# Etape 2: Transformer la version de quizz intermédaire en quizz finale grâce à un algorithme intermédiaire
def transform_to_multichoice(json_input):
    # Charger les données JSON
    quizzes = json.loads(json_input)['quizzes']
    
    # Préparer un dictionnaire pour la sortie
    multichoice_quizzes = {'quizzes': []}
    
    # Pour chaque question, ajouter des réponses incorrectes
    for quiz in quizzes:
        # Créer un objet question
        question_obj = {
            "question": quiz["question"],
            "answers": [
                {"text": quiz["answer"], "correct": True}  # La réponse correcte
            ]
        }
        
        # Ajouter des réponses incorrectes
        # Piocher au hasard 3 autres réponses du quiz comme réponses fausses
        incorrect_answers = [q["answer"] for q in quizzes if q != quiz]
        random.shuffle(incorrect_answers)
        incorrect_answers = incorrect_answers[:3]  # Prendre seulement 3 réponses incorrectes
        
        # Ajouter ces réponses incorrectes à la question
        for answer in incorrect_answers:
            question_obj["answers"].append({"text": answer, "correct": False})
        
        # Mélanger toutes les réponses pour diversifier les options
        random.shuffle(question_obj["answers"])
        
        # Ajouter l'objet question au quiz multichoice
        multichoice_quizzes['quizzes'].append(question_obj)

    return json.dumps(multichoice_quizzes, indent=4, ensure_ascii=False)

# Utiliser la fonction précédente pour obtenir le JSON initial
json_input = parse_quiz_text(quiz_text)



print("**********************  Raw quizz generated  **********************")

print(json_input)


# Transformer le quiz en format multichoice
multichoice_output = transform_to_multichoice(json_input)


print("**********************  Lastest format **********************")
print(multichoice_output)

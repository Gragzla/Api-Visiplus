# Api-Visiplus
Répertoire de l'API en python pour l'étude de cas 2 de visiplus

Dans le répertoir API Visiplus, il y a le code pour une API afin d'obtenir via le lancement uvicorn un swagger qui a deux routes, une pour prédire si il va pleuvoir, la deuxième pour déterminer la quantité de pluie qui devrait tomber si il pleut. 

Afin que l'APi fonctionne, il vous faudra resynthétiser les modèles en les nommant : modele_classification.joblib et modele_regression.joblib et le positionner dans le répertoire. 

Afin de faciliter la création des deux fichiers, a coté de ce README, il y a un fichier ScriptModeleMeteo.ipynb il permet via collab de générer les modèles. 

Pour la génération des modèles, il vous faudra extraire le fichier synop_2026.csv qui se trouve dans le fichier zip du meme nom et le mettre à disposition dans collab.

Une fois les fichiers obtenus, il vous sera possible de lancer l'application via uvicorn ( uvicorn  main:app --reload)
Cela vous donnera une route en local (ex : http://127.0.0.1:8000) a laquelle il vous faudra ajouter /docs (http://127.0.0.1:8000/docs)

Cela permet d'obtenir un swagger sur lequel il vous sera possible d'utiliser les routes. 

1 - Cliquer sur la route voulue
2 - Cliquer sur Try out
3 - Completer le json avec les valeurs attendues
4 - Cliquer sur exécuter
=> Vous obtiendrez le résultat de la prédiction

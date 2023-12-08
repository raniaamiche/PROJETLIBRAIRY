# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:26:40 2023

@author: MSI
"""

Avocat={ 'AA123' :{'nom':'ahmed abidi','spécialité':'divorce','nbre-exp':'7'},
        'RS124':{'nom':'rahma soussi','spécialité':'héritage','nbre-exp':'3'},
        'BT125':{'nom':'Bassem tlili','spécialité':'Assurance et banque','nbre-exp':'10'}}
client=[{'CIN':' 043865s' ,'nom':'Med Yassine','tel':'202224444','type de cas':'Divorce'},
        {'CIN': '213445p' ,'nom':'dali','tel':'26026127','type de cas':'Divorce'},
        {'CIN': '56987c' ,'nom':'mohamed','tel':'50452457','type de cas':'Divorce'}]
def créer_casTraité():
    CIN_client=input("donner le CIN : ")
    description_cas=input("donner la description de cas")
    etat_avencement=input("donner letat davencement")
    date_ouverture=input("donner la date douverture ")
    avocat_assignée=None
    return {"CIN_client": CIN_client, "description_cas": description_cas, "état_avancement": etat_avencement, "date_ouverture": date_ouverture, "avocat_assigné": avocat_assignée}
    
    
    
def assignation_Avocat(nom_avocat, CIN_client):
    cas_trouvé = None
    for cas in casTraité:
        if cas["CIN_client"] == CIN_client:
            cas_trouvé = cas
            cas["avocat_assigné"] = nom_avocat
            break
    if cas_trouvé is None:
        print("Aucun cas trouvé")
        


def étatAvancement(nom_cas):
    for cas in casTraité:
        if cas["description_cas"] == nom_cas:
            nouvel_état = input("Entrez le nouvel état d'avancement du cas (résolue/en cours/en attente) : ")
            cas["état_avancement"] = nouvel_état
            break
    else:
        print("Aucun cas trouvé avec ce nom.")


casTraité = []

while True:
    print("\n1. Créer un cas traité")
    print("2. Assigner un avocat à un cas")
    print("3. Mettre à jour l'état d'avancement d'un cas")
    print("4. Quitter")

    choix = input("Choisissez (1/2/3/4) : ")

    if choix == "1":
        cas = créer_casTraité()
        casTraité.append(cas)
        print("Cas traité ajouté avec succès.")

    elif choix == "2":
        nom_avocat = input("Entrez le nom de l'avocat : ")
        CIN_client = input("Entrez le CIN du client : ")
        assignation_Avocat(nom_avocat, CIN_client)

    elif choix == "3":
        nom_cas = input("Entrez le nom du cas : ")
        étatAvancement(nom_cas)

    elif choix == "4":
        print("Vous avez quitter.")
        break

    else:
        print("Option invalide. Veuillez choisir parmi les options proposées.")

    
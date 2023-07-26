
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status, generics
from caisse.models import ArticleModel,ReglementTempModel,LigneTicketTemp,UsersessionModel,PAgentModel,PFamilleArtModel,InfosartPrmppampModel
from caisse.serializers import ArticleSerializer,ArticleDetailSerializer,PanierSerializer,PanierDetailInsertSerializer,VenteSerializer
import math
from datetime import datetime



class Articles(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    queryset = ArticleModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        articles = ArticleModel.objects.all()
        total_articles = articles.count()
        if search_param:
            articles = articles.filter(title__icontains=search_param)
        serializer = self.serializer_class(articles[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_articles,
            "page": page_num,
            "last_page": math.ceil(total_articles / limit_num),
            "articles": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"article": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(generics.GenericAPIView):
    queryset = ArticleModel.objects.all()
    serializer_class = ArticleDetailSerializer

    def get_article(self, pk):
        try:
            return ArticleModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        article = self.get_article(pk=pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(article)
        return Response({"status": "success", "data": {"article": serializer.data}})

    def patch(self, request, pk):
        article = self.get_article(pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"article": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_article(pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Paniers(generics.GenericAPIView):
    serializer_class = PanierSerializer
    queryset = ReglementTempModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        paniers = ReglementTempModel.objects.all()
        total_paniers = paniers.count()
        if search_param:
            paniers = paniers.filter(title__icontains=search_param)
        serializer = self.serializer_class(paniers[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_paniers,
            "page": page_num,
            "last_page": math.ceil(total_paniers / limit_num),
            "paniers": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
       # Insertion dans la base de données des données serializers
            instant = serializer.save()
       # Stockage du numero de caisse pour identifier la caisse et retrouver l'identifiant généré par le trigger
            caisse = instant.num_caisse
       # Requete pour identifier le dernier element crée avec l'identifiant de cette caisse 
            glad= ReglementTempModel.objects.filter(num_caisse=caisse).latest('date_reg')
       # Le dernier element crée avec l'identifiant de cette caisse 
            panier = glad.code_reg

            return Response({"status": "success", "data": {"panier": panier}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PanierDetail(generics.GenericAPIView):
    queryset = LigneTicketTemp.objects.all()
    serializer_class_art = ArticleDetailSerializer
    serializer_class_caisse = PanierSerializer
    serializer_class = PanierDetailInsertSerializer


    def get_article(self, pk):
        try:
            return ArticleModel.objects.get(pk=pk)
        except:
            return None
    
    def post(self, request, pk):

        prmp = 0
        tauxtva = 18
        flagtva = 1
        tauxarsi = 2
        flagarsi = 1

        datas=request.data
        # print('datas')
        # print(datas)
    
     

        # Recuperation de l'identifiant de l'utilisateur
        num_utilisateur = datas['user_id']

       

        # Recuperation des autres informations de l'utilisateur
        # utilisateur = PAgentModel.objects.filter(code_agent=num_utilisateur).latest('date_reg')
        utilisateur = PAgentModel.objects.get(code_agent=num_utilisateur)
        # fields = ('code_reg','code_clt','num_caisse','date_reg','flag_acpte','code_agent','code_agce')

         #Recuperons la caisse en activité
        caisse = utilisateur.codecaisse
        code_clt = 1
        date = datetime.now()
        flag = 1
        agence = utilisateur.code_agce
        

        #Création du data pour le reglement temp
        data_reg_temp = {}
        data_reg_temp['code_clt'] = code_clt
        data_reg_temp['num_caisse'] = caisse
        data_reg_temp['date_reg'] = date
        data_reg_temp['flag_acpte'] = flag
        data_reg_temp['code_agent'] = num_utilisateur
        data_reg_temp['code_agce'] = agence
        data_reg_temp['flag_tick_fact'] = 0
        data_reg_temp['flag_annule'] = 0
        data_reg_temp['flag_clo'] = 0
        data_reg_temp['flag_imp_tick_fact'] = 0
        data_reg_temp['flag_tva_fact'] = 1
        data_reg_temp['flag_arsi_fact'] = 0
        data_reg_temp['vente_apisoft'] = 0
        data_reg_temp['montant'] = 0

       

        # Supprimez la clé "test" du dictionnaire serializer.data
        datas.pop("user_id", None)
      
        article = self.get_article(pk=pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class_art(article)
        famille = PFamilleArtModel.objects.get(code_fa=serializer.data['code_fa'])
        taxable = famille.taxable_fa
        sous_rayon = serializer.data['code_sr']
        flagsco = serializer.data['flag_sco_art']

        if taxable == False or sous_rayon == "1521" or sous_rayon == "1522" :
          tauxtva = 0 
          flagtva = 0

        if flagsco == False :
          tauxarsi = 5
          flagarsi = 0

        # print('taux')
        # print(tauxtva)
        # print(flagtva)
        # print(tauxarsi)
        # print(flagarsi)

        info = InfosartPrmppampModel.objects.get(pk=pk)
        if info.nouv_prmp == None:
         prmp_value = 0
        else:
         prmp_value = info.nouv_prmp

        print('info')
        print(prmp_value)


        #Verification de l'existence d'un TAMPON de vente 
        # tampon= UsersessionModel.objects.filter(caisse=caisse).latest('created_at')
        tamp =  UsersessionModel.objects.filter(caisse=caisse).count()
        # print('tampon')
        # print(tamp)
        if tamp > 1:
         tampon = UsersessionModel.objects.filter(caisse=caisse).order_by('-created_at').reverse()[1]
        else:
         tampon= UsersessionModel.objects.filter(caisse=caisse).latest('created_at')

        # print('tampon')
        # print(tampon)
        # print(tampon.tampon)

        numero_tampon = tampon.tampon
        
        if numero_tampon == 0:
          
            serializer_vente = self.serializer_class_caisse(data=data_reg_temp)
            if serializer_vente.is_valid():
        # Insertion dans la base de données des données serializers
                instant = serializer_vente.save()
        # Stockage du numero de caisse pour identifier la caisse et retrouver l'identifiant généré par le trigger
                caisse = instant.num_caisse
        # Requete pour identifier le dernier element crée avec l'identifiant de cette caisse 
                glad= ReglementTempModel.objects.filter(num_caisse=caisse).latest('date_reg')
        # Le dernier element crée avec l'identifiant de cette caisse 
                panier = glad.code_reg

                tampon.tampon = panier
                tampon.save()
                try:
                    article_ticket = LigneTicketTemp.objects.get(code_reg=panier,code_art=pk)
                except LigneTicketTemp.DoesNotExist:
                    article_ticket = 0
                

                if article_ticket == 0:                 
                #Création du data pour la ligne ticket temp
                    datas = {}
                    datas['code_clt'] = 1
                    datas['code_art'] = serializer.data['code_art']
                    datas['num_caisse'] = caisse
                    datas['code_reg'] = panier
                    datas['quantite'] = 1
                    datas['prix_unit'] = serializer.data['prix_ttc']
                    datas['remise'] = 0
                    datas['tot_net'] = serializer.data['prix_ttc']
                    datas['tot_brut'] = serializer.data['prix_ttc']
                    datas['tot_net_ht'] = serializer.data['prix_ttc']
                    datas['marge'] = serializer.data['marge']
                    datas['prmp'] = prmp_value
                    datas['tot_brut_ht'] = serializer.data['marge']
                    datas['remise_mont'] = 0
                    datas['code_agce'] = agence
                    datas['prix_vente'] = serializer.data['prix_ttc']
                    datas['date_lt'] = date
                    datas['prix_ht_ticket'] = serializer.data['prix_ht']
                    datas['code_agent'] = num_utilisateur
                    datas['prix_ht_remise'] = 0
                    datas['flag_tva_lt'] = flagtva
                    datas['flag_arsi_lt'] = flagarsi
                    datas['mt_tva_lt'] = 0
                    datas['mt_arsi_lt'] = 0
                    datas['taux_tva_lt'] = tauxtva
                    datas['taux_arsi_lt'] = tauxarsi
                    datas['vente_apisoft'] = 0
                    datas['nom_art'] = serializer.data['nom_art']
                    datas['flag_stock_ln'] = 1
                    datas['flag_stock_ln_ann'] = 0
                    serializer_ligne = self.serializer_class(data=datas) 
                    if serializer_ligne.is_valid():
                # Insertion dans la base de données des données serializers
                        bref = serializer_ligne.save()

                    tableau = []
                    total = 0
                    for article in LigneTicketTemp.objects.filter(code_reg=panier):
                        total = total + article.tot_net_ht
                        untable = {
                            'code_art' :  article.code_art,
                            'nom_art'  : article.nom_art,
                            'prix_moyen' : article.prix_vente,
                            'prix_vente' : article.prix_vente,
                            'remise' : article.remise,
                            'quantite' : article.quantite,
                            'montant' : article.tot_net_ht                      
                            }
                        tableau.append(untable)

                        context= {
                            'article':tableau
                            }
                        context['total'] = total
                        context['ticket'] = panier

                        
                else:
              
                 ligne = get_object_or_404(LigneTicketTemp, code_reg=panier, code_art=pk)
                 ligne.quantite += 1
                 ligne.date_lt = datetime.now()
                 ligne.tot_brut = ligne.quantite * ligne.prix_unit
                 ligne.tot_brut_ht = ligne.quantite * ligne.prix_unit
                 ligne.tot_net = ligne.quantite * ligne.prix_unit
                 ligne.tot_net_ht = ligne.quantite * ligne.prix_unit
                 ligne.prix_ht_ticket = ligne.quantite * ligne.prix_unit
                 ligne.save()
                
                tableau = []
                total = 0
                for article in LigneTicketTemp.objects.filter(code_reg=panier):
                   total = total + article.tot_net_ht
                   untable = {
                      'code_art' :  article.code_art,
                      'nom_art'  : article.nom_art,
                      'prix_moyen' : article.prix_vente,
                      'prix_vente' : article.prix_vente,
                      'remise' : article.remise,
                      'quantite' : article.quantite,
                      'montant' : article.tot_net_ht                      
                    }
                   tableau.append(untable)

                   context= {
                       'article':tableau
                    }
                   context['total'] = total
                   context['ticket'] = panier


                return JsonResponse(context)
                 

        else:
                panier = numero_tampon
        
                try:
                    article_ticket = LigneTicketTemp.objects.get(code_reg=panier,code_art=pk)
                except LigneTicketTemp.DoesNotExist:
                    article_ticket = 0
                

                if article_ticket == 0:                 
                #Création du data pour la ligne ticket temp
                    datas = {}
                    datas['code_clt'] = 1
                    datas['code_art'] = serializer.data['code_art']
                    datas['num_caisse'] = caisse
                    datas['code_reg'] = panier
                    datas['quantite'] = 1
                    datas['prix_unit'] = serializer.data['prix_ttc']
                    datas['remise'] = 0
                    datas['tot_net'] = serializer.data['prix_ttc']
                    datas['tot_brut'] = serializer.data['prix_ttc']
                    datas['tot_net_ht'] = serializer.data['prix_ttc']
                    datas['marge'] = serializer.data['marge']
                    datas['prmp'] = prmp_value
                    datas['tot_brut_ht'] = serializer.data['marge']
                    datas['remise_mont'] = 0
                    datas['code_agce'] = agence
                    datas['prix_vente'] = serializer.data['prix_ttc']
                    datas['date_lt'] = date
                    datas['prix_ht_ticket'] = serializer.data['prix_ht']
                    datas['code_agent'] = num_utilisateur
                    datas['prix_ht_remise'] = 0
                    datas['flag_tva_lt'] = flagtva
                    datas['flag_arsi_lt'] = flagarsi
                    datas['mt_tva_lt'] = 0
                    datas['mt_arsi_lt'] = 0
                    datas['taux_tva_lt'] = tauxtva
                    datas['taux_arsi_lt'] = tauxarsi
                    datas['vente_apisoft'] = 0
                    datas['nom_art'] = serializer.data['nom_art']
                    datas['flag_stock_ln'] = 1
                    datas['flag_stock_ln_ann'] = 0
                    serializer_ligne = self.serializer_class(data=datas) 
                    if serializer_ligne.is_valid():
                # Insertion dans la base de données des données serializers
                        bref = serializer_ligne.save()
                    
                    tableau = []
                    total = 0
                    for article in LigneTicketTemp.objects.filter(code_reg=panier):
                        total = total + article.tot_net_ht
                        untable = {
                            'code_art' :  article.code_art,
                            'nom_art'  : article.nom_art,
                            'prix_moyen' : article.prix_vente,
                            'prix_vente' : article.prix_vente,
                            'remise' : article.remise,
                            'quantite' : article.quantite,
                            'montant' : article.tot_net_ht                      
                            }
                        tableau.append(untable)

                        context= {
                            'article':tableau
                            }
                        context['total'] = total
                        context['ticket'] = panier

                    
                else:
                 ligne = get_object_or_404(LigneTicketTemp, code_reg=panier, code_art=pk)
                 ligne.quantite += 1
                 ligne.date_lt = datetime.now()
                 ligne.tot_brut = ligne.quantite * ligne.prix_unit
                 ligne.tot_brut_ht = ligne.quantite * ligne.prix_unit
                 ligne.tot_net = ligne.quantite * ligne.prix_unit
                 ligne.tot_net_ht = ligne.quantite * ligne.prix_unit
                 ligne.prix_ht_ticket = ligne.quantite * ligne.prix_unit
                 ligne.save()

                 tableau = []
                 total = 0
                 for article in LigneTicketTemp.objects.filter(code_reg=panier):
                   total = total + article.tot_net_ht
                   untable = {
                      'code_art' :  article.code_art,
                      'nom_art'  : article.nom_art,
                      'prix_moyen' : article.prix_vente,
                      'prix_vente' : article.prix_vente,
                      'remise' : article.remise,
                      'quantite' : article.quantite,
                      'montant total' : article.tot_net_ht                      
                    }
                   tableau.append(untable)

                   context= {
                       'article':tableau
                    }
                   context['total'] = total
                   context['ticket'] = panier


                return JsonResponse(context)
 


    # def get(self, request, pk):
    #     article = self.get_article(pk=pk)
    #     if article == None:
    #         return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = self.serializer_class(article)
    #     return Response({"status": "success", "data": {"article": serializer.data}})

    def get(self, request, pk):
        num_utilisateur = pk
        utilisateur = PAgentModel.objects.get(code_agent=num_utilisateur)
        caisse = utilisateur.codecaisse
        tamp =  UsersessionModel.objects.filter(caisse=caisse).count()
        # print('tampon')
        # print(tamp)
        if tamp > 1:
         tampon = UsersessionModel.objects.filter(caisse=caisse).order_by('-created_at').reverse()[1]
        else:
         tampon= UsersessionModel.objects.filter(caisse=caisse).latest('created_at')
        numero_tampon = tampon.tampon
        tableau = []
        total = 0
        variable = LigneTicketTemp.objects.filter(code_reg=numero_tampon)
        # print(variable)
        try:
            article_ticket = ReglementTempModel.objects.get(code_reg=numero_tampon)
        except ReglementTempModel.DoesNotExist:
            variable = 0
        
        if variable == 0 :
            return Response({"status": "fail", "message": f"Panier : {numero_tampon} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        else:
           for article in variable:
            total = total + article.tot_net_ht
            untable = {
                'code_art' :  article.code_art,
                'nom_art'  : article.nom_art,
                'prix_moyen' : article.prix_vente,
                'prix_vente' : article.prix_vente,
                'remise' : article.remise,
                'quantite' : article.quantite,
                'montant' : article.tot_net_ht                      
                }
            tableau.append(untable)

            context= {
                'article':tableau
                }
            context['total'] = total
            context['ticket'] = numero_tampon

        return JsonResponse(context)


    def patch(self, request, pk):
        article = self.get_article(pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"article": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_article(pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Vente(generics.GenericAPIView):
    serializer_class = VenteSerializer
    queryset = ReglementTempModel.objects.all()

    def post(self, request):
        datas=request.data
        print(datas)
        panier = datas['code_reg']
        ligne = get_object_or_404(ReglementTempModel, code_reg=panier)
        ligne.code_mr = 1
        ligne.code_reg = panier
        ligne.montant = 0
        ligne.montant_reg = datas['montant_reg']
        ligne.montant_remis = datas['montant_remis']
        ligne.mont_mde_reg1 = datas['mont_mde_reg1']
        ligne.mont_mde_reg2 = datas['mont_mde_reg2']
        ligne.mont_mde_reg3 = datas['mont_mde_reg3']
        ligne.monnaie_rendue = datas['monnaie_rendue']
        ligne.quittance_reg = 0
        # ligne.flag_tick_fact = datas['flag_tick_fact']
        ligne.flag_annule = 0
        ligne.flag_acpte = 1
        ligne.flag_imp_tick_fact = 1
        # ligne.flag_imp_tick_fact = datas['flag_imp_tick_fact']
        ligne.flag_clo = 0
        ligne.mont_mde_reg1_temp = datas['mont_mde_reg1_temp']
        ligne.mont_mde_reg2_temp = datas['mont_mde_reg2_temp']
        ligne.mont_mde_reg3_temp = datas['mont_mde_reg3_temp']
        # ligne.flag_tva_fact = datas['flag_tva_fact']
        # ligne.flag_arsi_fact = datas['flag_arsi_fact']
        ligne.flag_tva_fact = 1
        ligne.flag_arsi_fact = 0
        ligne.vente_apisoft = datas['vente_apisoft']
        ligne.save()

        tamp =  UsersessionModel.objects.filter(caisse=ligne.num_caisse).count()
        if tamp > 1:
         tampon = UsersessionModel.objects.filter(caisse=ligne.num_caisse).order_by('-created_at').reverse()[1]
        else:
         tampon= UsersessionModel.objects.filter(caisse=ligne.num_caisse).latest('created_at')

        session = get_object_or_404(UsersessionModel, tampon=tampon.tampon)
        session.tampon = 0
        session.save()

        return Response({"status": "success", "data": {"panier": panier}}, status=status.HTTP_201_CREATED)

class VenteDifferee(generics.GenericAPIView):
    queryset = LigneTicketTemp.objects.all()
    serializer_class_art = ArticleDetailSerializer
    serializer_class_caisse = PanierSerializer
    serializer_class = PanierDetailInsertSerializer


    def get_article(self, pk):
        try:
            return ArticleModel.objects.get(pk=pk)
        except:
            return None
    
    def post(self, request, pk):

        prmp = 0
        tauxtva = 18
        flagtva = 1
        tauxarsi = 2
        flagarsi = 1

        datas=request.data
        print('datas')
        print(datas)
    
     

        # Recuperation de l'identifiant de l'utilisateur
        num_utilisateur = datas['user_id']

       

        # Recuperation des autres informations de l'utilisateur
        # utilisateur = PAgentModel.objects.filter(code_agent=num_utilisateur).latest('date_reg')
        utilisateur = PAgentModel.objects.get(code_agent=num_utilisateur)
        # fields = ('code_reg','code_clt','num_caisse','date_reg','flag_acpte','code_agent','code_agce')

         #Recuperons la caisse en activité
        caisse = utilisateur.codecaisse
        code_clt = 1
        date = datetime.now()
        flag = 1
        agence = utilisateur.code_agce
        

        #Création du data pour le reglement temp
        data_reg_temp = {}
        data_reg_temp['code_clt'] = code_clt
        data_reg_temp['num_caisse'] = caisse
        data_reg_temp['date_reg'] = date
        data_reg_temp['flag_acpte'] = flag
        data_reg_temp['code_agent'] = num_utilisateur
        data_reg_temp['code_agce'] = agence
        data_reg_temp['flag_tick_fact'] = 0
        data_reg_temp['flag_annule'] = 0
        data_reg_temp['flag_clo'] = 0
        data_reg_temp['flag_imp_tick_fact'] = 0
        data_reg_temp['flag_tva_fact'] = 1
        data_reg_temp['flag_arsi_fact'] = 0
        data_reg_temp['vente_apisoft'] = 0
        data_reg_temp['montant'] = 0

       

        # Supprimez la clé "test" du dictionnaire serializer.data
        datas.pop("user_id", None)
      
        article = self.get_article(pk=pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class_art(article)
        famille = PFamilleArtModel.objects.get(code_fa=serializer.data['code_fa'])
        taxable = famille.taxable_fa
        sous_rayon = serializer.data['code_sr']
        flagsco = serializer.data['flag_sco_art']

        if taxable == False or sous_rayon == "1521" or sous_rayon == "1522" :
          tauxtva = 0 
          flagtva = 0

        if flagsco == False :
          tauxarsi = 5
          flagarsi = 0

        # print('taux')
        # print(tauxtva)
        # print(flagtva)
        # print(tauxarsi)
        # print(flagarsi)

        info = InfosartPrmppampModel.objects.get(pk=pk)
        if info.nouv_prmp == None:
         prmp_value = 0
        else:
         prmp_value = info.nouv_prmp

        print('info')
        print(prmp_value)


        #Verification de l'existence d'un TAMPON de vente 
        # tampon= UsersessionModel.objects.filter(caisse=caisse).latest('created_at')
        tamp =  UsersessionModel.objects.filter(caisse=caisse).count()
        # print('tampon')
        # print(tamp)
        if tamp > 1:
         tampon = UsersessionModel.objects.filter(caisse=caisse).order_by('-created_at').reverse()[1]
        else:
         tampon= UsersessionModel.objects.filter(caisse=caisse).latest('created_at')

        # print('tampon')
        # print(tampon)
        # print(tampon.tampon)

        numero_tampon = tampon.tampon
        
        if numero_tampon == 0:
          
            serializer_vente = self.serializer_class_caisse(data=data_reg_temp)
            if serializer_vente.is_valid():
        # Insertion dans la base de données des données serializers
                instant = serializer_vente.save()
        # Stockage du numero de caisse pour identifier la caisse et retrouver l'identifiant généré par le trigger
                caisse = instant.num_caisse
        # Requete pour identifier le dernier element crée avec l'identifiant de cette caisse 
                glad= ReglementTempModel.objects.filter(num_caisse=caisse).latest('date_reg')
        # Le dernier element crée avec l'identifiant de cette caisse 
                panier = glad.code_reg

                tampon.tampon = panier
                tampon.save()
                try:
                    article_ticket = LigneTicketTemp.objects.get(code_reg=panier,code_art=pk)
                except LigneTicketTemp.DoesNotExist:
                    article_ticket = 0
                

                if article_ticket == 0:                 
                #Création du data pour la ligne ticket temp
                    datas = {}
                    datas['code_clt'] = 1
                    datas['code_art'] = serializer.data['code_art']
                    datas['num_caisse'] = caisse
                    datas['code_reg'] = panier
                    datas['quantite'] = 1
                    datas['prix_unit'] = serializer.data['prix_ttc']
                    datas['remise'] = 0
                    datas['tot_net'] = serializer.data['prix_ttc']
                    datas['tot_brut'] = serializer.data['prix_ttc']
                    datas['tot_net_ht'] = serializer.data['prix_ttc']
                    datas['marge'] = serializer.data['marge']
                    datas['prmp'] = prmp_value
                    datas['tot_brut_ht'] = serializer.data['marge']
                    datas['remise_mont'] = 0
                    datas['code_agce'] = agence
                    datas['prix_vente'] = serializer.data['prix_ttc']
                    datas['date_lt'] = date
                    datas['prix_ht_ticket'] = serializer.data['prix_ht']
                    datas['code_agent'] = num_utilisateur
                    datas['prix_ht_remise'] = 0
                    datas['flag_tva_lt'] = flagtva
                    datas['flag_arsi_lt'] = flagarsi
                    datas['mt_tva_lt'] = 0
                    datas['mt_arsi_lt'] = 0
                    datas['taux_tva_lt'] = tauxtva
                    datas['taux_arsi_lt'] = tauxarsi
                    datas['vente_apisoft'] = 0
                    datas['nom_art'] = serializer.data['nom_art']
                    datas['flag_stock_ln'] = 1
                    datas['flag_stock_ln_ann'] = 0
                    serializer_ligne = self.serializer_class(data=datas) 
                    if serializer_ligne.is_valid():
                # Insertion dans la base de données des données serializers
                        bref = serializer_ligne.save()

                    tableau = []
                    total = 0
                    for article in LigneTicketTemp.objects.filter(code_reg=panier):
                        total = total + article.tot_net_ht
                        untable = {
                            'code_art' :  article.code_art,
                            'nom_art'  : article.nom_art,
                            'prix_moyen' : article.prix_vente,
                            'prix_vente' : article.prix_vente,
                            'remise' : article.remise,
                            'quantite' : article.quantite,
                            'montant' : article.tot_net_ht                      
                            }
                        tableau.append(untable)

                        context= {
                            'article':tableau
                            }
                        context['total'] = total
                        context['ticket'] = panier

                        
                else:
              
                 ligne = get_object_or_404(LigneTicketTemp, code_reg=panier, code_art=pk)
                 ligne.quantite += 1
                 ligne.date_lt = datetime.now()
                 ligne.tot_brut = ligne.quantite * ligne.prix_unit
                 ligne.tot_brut_ht = ligne.quantite * ligne.prix_unit
                 ligne.tot_net = ligne.quantite * ligne.prix_unit
                 ligne.tot_net_ht = ligne.quantite * ligne.prix_unit
                 ligne.prix_ht_ticket = ligne.quantite * ligne.prix_unit
                 ligne.save()
                
                tableau = []
                total = 0
                for article in LigneTicketTemp.objects.filter(code_reg=panier):
                   total = total + article.tot_net_ht
                   untable = {
                      'code_art' :  article.code_art,
                      'nom_art'  : article.nom_art,
                      'prix_moyen' : article.prix_vente,
                      'prix_vente' : article.prix_vente,
                      'remise' : article.remise,
                      'quantite' : article.quantite,
                      'montant' : article.tot_net_ht                      
                    }
                   tableau.append(untable)

                   context= {
                       'article':tableau
                    }
                   context['total'] = total
                   context['ticket'] = panier


                return JsonResponse(context)
                 

        else:
                panier = numero_tampon
        
                try:
                    article_ticket = LigneTicketTemp.objects.get(code_reg=panier,code_art=pk)
                except LigneTicketTemp.DoesNotExist:
                    article_ticket = 0
                

                if article_ticket == 0:                 
                #Création du data pour la ligne ticket temp
                    datas = {}
                    datas['code_clt'] = 1
                    datas['code_art'] = serializer.data['code_art']
                    datas['num_caisse'] = caisse
                    datas['code_reg'] = panier
                    datas['quantite'] = 1
                    datas['prix_unit'] = serializer.data['prix_ttc']
                    datas['remise'] = 0
                    datas['tot_net'] = serializer.data['prix_ttc']
                    datas['tot_brut'] = serializer.data['prix_ttc']
                    datas['tot_net_ht'] = serializer.data['prix_ttc']
                    datas['marge'] = serializer.data['marge']
                    datas['prmp'] = prmp_value
                    datas['tot_brut_ht'] = serializer.data['marge']
                    datas['remise_mont'] = 0
                    datas['code_agce'] = agence
                    datas['prix_vente'] = serializer.data['prix_ttc']
                    datas['date_lt'] = date
                    datas['prix_ht_ticket'] = serializer.data['prix_ht']
                    datas['code_agent'] = num_utilisateur
                    datas['prix_ht_remise'] = 0
                    datas['flag_tva_lt'] = flagtva
                    datas['flag_arsi_lt'] = flagarsi
                    datas['mt_tva_lt'] = 0
                    datas['mt_arsi_lt'] = 0
                    datas['taux_tva_lt'] = tauxtva
                    datas['taux_arsi_lt'] = tauxarsi
                    datas['vente_apisoft'] = 0
                    datas['nom_art'] = serializer.data['nom_art']
                    datas['flag_stock_ln'] = 1
                    datas['flag_stock_ln_ann'] = 0
                    serializer_ligne = self.serializer_class(data=datas) 
                    if serializer_ligne.is_valid():
                # Insertion dans la base de données des données serializers
                        bref = serializer_ligne.save()
                    
                    tableau = []
                    total = 0
                    for article in LigneTicketTemp.objects.filter(code_reg=panier):
                        total = total + article.tot_net_ht
                        untable = {
                            'code_art' :  article.code_art,
                            'nom_art'  : article.nom_art,
                            'prix_moyen' : article.prix_vente,
                            'prix_vente' : article.prix_vente,
                            'remise' : article.remise,
                            'quantite' : article.quantite,
                            'montant' : article.tot_net_ht                      
                            }
                        tableau.append(untable)

                        context= {
                            'article':tableau
                            }
                        context['total'] = total
                        context['ticket'] = panier

                    
                else:
                 ligne = get_object_or_404(LigneTicketTemp, code_reg=panier, code_art=pk)
                 ligne.quantite += 1
                 ligne.date_lt = datetime.now()
                 ligne.tot_brut = ligne.quantite * ligne.prix_unit
                 ligne.tot_brut_ht = ligne.quantite * ligne.prix_unit
                 ligne.tot_net = ligne.quantite * ligne.prix_unit
                 ligne.tot_net_ht = ligne.quantite * ligne.prix_unit
                 ligne.prix_ht_ticket = ligne.quantite * ligne.prix_unit
                 ligne.save()

                 tableau = []
                 total = 0
                 for article in LigneTicketTemp.objects.filter(code_reg=panier):
                   total = total + article.tot_net_ht
                   untable = {
                      'code_art' :  article.code_art,
                      'nom_art'  : article.nom_art,
                      'prix_moyen' : article.prix_vente,
                      'prix_vente' : article.prix_vente,
                      'remise' : article.remise,
                      'quantite' : article.quantite,
                      'montant total' : article.tot_net_ht                      
                    }
                   tableau.append(untable)

                   context= {
                       'article':tableau
                    }
                   context['total'] = total
                   context['ticket'] = panier


                return JsonResponse(context)
 


    # def get(self, request, pk):
    #     article = self.get_article(pk=pk)
    #     if article == None:
    #         return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = self.serializer_class(article)
    #     return Response({"status": "success", "data": {"article": serializer.data}})

    def get(self, request, pk):
        num_utilisateur = pk
        utilisateur = PAgentModel.objects.get(code_agent=num_utilisateur)
        caisse = utilisateur.codecaisse
        tamp =  UsersessionModel.objects.filter(caisse=caisse).count()
        # print('tampon')
        # print(tamp)
        if tamp > 1:
         tampon = UsersessionModel.objects.filter(caisse=caisse).order_by('-created_at').reverse()[1]
        else:
         tampon= UsersessionModel.objects.filter(caisse=caisse).latest('created_at')
        numero_tampon = tampon.tampon
        tableau = []
        total = 0
        variable = LigneTicketTemp.objects.filter(code_reg=numero_tampon)
        # print(variable)
        try:
            article_ticket = ReglementTempModel.objects.get(code_reg=numero_tampon)
        except ReglementTempModel.DoesNotExist:
            variable = 0
        
        if variable == 0 :
            return Response({"status": "fail", "message": f"Panier : {numero_tampon} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        else:
           for article in variable:
            total = total + article.tot_net_ht
            untable = {
                'code_art' :  article.code_art,
                'nom_art'  : article.nom_art,
                'prix_moyen' : article.prix_vente,
                'prix_vente' : article.prix_vente,
                'remise' : article.remise,
                'quantite' : article.quantite,
                'montant' : article.tot_net_ht                      
                }
            tableau.append(untable)

            context= {
                'article':tableau
                }
            context['total'] = total
            context['ticket'] = numero_tampon

        return JsonResponse(context)


    def patch(self, request, pk):
        article = self.get_article(pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"article": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_article(pk)
        if article == None:
            return Response({"status": "fail", "message": f"Article avec l'identifiant: {pk} inexistant"}, status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

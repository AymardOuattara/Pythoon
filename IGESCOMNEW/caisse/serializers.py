from rest_framework import serializers
from caisse.models import ArticleModel, ReglementTempModel,LigneTicketTemp, UsersessionModel


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = '__all__'

class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        # fields = ('code_art','nom_art','code_sr','code_barre','prix_ttc')
        fields = '__all__'


class PanierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReglementTempModel
        fields = ('code_reg','code_clt','num_caisse','date_reg','flag_acpte','code_agent','code_agce',
                  'flag_tick_fact','flag_annule','flag_clo','flag_imp_tick_fact','flag_tva_fact','flag_arsi_fact',
                  'vente_apisoft','montant')
        # CODE_REG, CODE_CLT, NUM_CAISSE, DATE_REG, FLAG_ACPTE, CODE_AGENT , CODE_AGCE
        # fields = ('code_mr','p_m_code_mr','p_m2_code_mr','code_clt','num_caisse','montant','echeance','date_reg','montant_reg','flag_acpte','montant_remis','mont_mde_reg1','mont_mde_reg2','mont_mde_reg3','monnaie_rendue','code_agce','quittance_reg','ref_bsc','comment_bsc','code_motif','flag_tick_fact','code_agent','flag_annule','flag_clo','code_agent_modif','pass_nomclt','pass_tel','pass_adresse','pass_cc','flag_imp_tick_fact','mont_mde_reg1_temp','mont_mde_reg2_temp','mont_mde_reg3_temp','flag_tva_fact','flag_arsi_fact','code_comer','vente_apisoft','nom_art','code_vdeur')

class PanierDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneTicketTemp
        fields = '__all__'

class PanierDetailInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneTicketTemp
        fields = ('code_clt','code_art','num_caisse','code_reg','quantite','prix_unit','remise','tot_net','tot_brut','tot_net_ht','marge',
                  'prmp','tot_brut_ht','remise_mont','code_agce','prix_vente','date_lt','prix_ht_ticket','code_agent',
                  'prix_ht_remise','nom_art','flag_tva_lt','flag_arsi_lt','mt_tva_lt','mt_arsi_lt',
                  'taux_tva_lt','taux_arsi_lt','vente_apisoft','flag_stock_ln','flag_stock_ln_ann')
   
class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersessionModel
        fields = '__all__' 

class TamponVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersessionModel
        fields = 'tampon' 

class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReglementTempModel
        fields = ('code_reg','code_mr','montant','montant_reg','montant_remis','mont_mde_reg1','mont_mde_reg2','mont_mde_reg3',
                  'monnaie_rendue','flag_clo',
                  'mont_mde_reg1_temp','mont_mde_reg2_temp','mont_mde_reg3_temp','vente_apisoft')
        # fields = ('code_reg','code_mr','montant','montant_reg','montant_remis','mont_mde_reg1','mont_mde_reg2','mont_mde_reg3',
        #           'monnaie_rendue','quittance_reg','flag_tick_fact','flag_annule','flag_clo','flag_imp_tick_fact',
        #           'mont_mde_reg1_temp','mont_mde_reg2_temp','mont_mde_reg3_temp','flag_tva_fact',
        #           'flag_arsi_fact','vente_apisoft')
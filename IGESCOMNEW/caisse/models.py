# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class PFamilleArtModel(models.Model):
    code_fa = models.CharField(primary_key=True, max_length=20)
    lib_fa = models.CharField(max_length=200, blank=True, null=True)
    taxable_fa = models.BooleanField(blank=True, null=True)
    num_cpte_cptable = models.CharField(max_length=20, blank=True, null=True)
    abr_fa = models.CharField(max_length=1, blank=True, null=True)
    tmc_fa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    code_serv = models.FloatField(blank=True, null=True)
    code_depot = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'P_FAMILLE_ART'
        ordering = ['-code_fa']
        def __str__(self) -> str:
            return self.code_fa

class ArticleModel(models.Model):
    code_art = models.CharField(primary_key=True, max_length=25)
    code_sr = models.CharField(max_length=25, blank=True, null=True)
    code_ta = models.CharField(max_length=1, blank=True, null=True)
    code_taxe = models.FloatField(blank=True, null=True)
    code_barre = models.CharField(max_length=20, blank=True, null=True)
    nom_art = models.CharField(max_length=255, blank=True, null=True)
    flag_actif = models.BooleanField(blank=True, null=True)
    pamp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    prix_ht = models.FloatField(blank=True, null=True)
    prix_ttc = models.FloatField(blank=True, null=True)
    marge = models.FloatField(blank=True, null=True)
    marque_art = models.FloatField(blank=True, null=True)
    longeur = models.FloatField(blank=True, null=True)
    largeur = models.FloatField(blank=True, null=True)
    epaisseur = models.FloatField(blank=True, null=True)
    poids_brut = models.FloatField(blank=True, null=True)
    poids_net = models.FloatField(blank=True, null=True)
    stock_min_gen = models.FloatField(blank=True, null=True)
    stock_max_gen = models.FloatField(blank=True, null=True)
    stock_phys_gen = models.FloatField(blank=True, null=True)
    unite_vente = models.CharField(max_length=10, blank=True, null=True)
    descr_art = models.CharField(max_length=200, blank=True, null=True)
    image_art = models.CharField(max_length=100, blank=True, null=True)
    date_creat = models.DateField(blank=True, null=True)
    date_modif = models.DateField(blank=True, null=True)
    gestionstock = models.BooleanField(blank=True, null=True)
    marge_pourcent = models.FloatField(blank=True, null=True)
    auteur_art = models.CharField(max_length=100, blank=True, null=True)
    editeur_art = models.CharField(max_length=100, blank=True, null=True)
    collection_art = models.CharField(max_length=100, blank=True, null=True)
    date_paru_art = models.DateField(blank=True, null=True)
    flag_art_dcom = models.BooleanField(blank=True, null=True)
    coeff_vente = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    flag_sco_art = models.BooleanField(blank=True, null=True)
    code_four = models.CharField(max_length=25, blank=True, null=True)
    code_ndp = models.CharField(max_length=25, blank=True, null=True)
    famille = models.CharField(max_length=25, blank=True, null=True)
    code_ma = models.FloatField(blank=True, null=True)
    code_fa = models.CharField(max_length=25, blank=True, null=True)
    # code_fa = models.ForeignKey(PFamilleArtModel, on_delete=models.CASCADE)


    code_start2 = models.CharField(max_length=3, blank=True, null=True)
    date_peremp = models.DateField(blank=True, null=True)
    code_ray = models.CharField(max_length=25, blank=True, null=True)
    isbn_art = models.CharField(max_length=25, blank=True, null=True)
    solde_art = models.FloatField(blank=True, null=True)
    flag_caravan = models.BooleanField(blank=True, null=True)
    flag_etiqtble = models.BooleanField(blank=True, null=True)
    flag_modprix = models.FloatField(blank=True, null=True)
    code_start = models.CharField(max_length=3, blank=True, null=True)
    date_dernvte = models.DateField(blank=True, null=True)
    date_prement = models.DateField(blank=True, null=True)
    date_dernent = models.DateField(blank=True, null=True)
    periodicite_art = models.CharField(max_length=100, blank=True, null=True)
    conditionem_art = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ARTICLE'
        ordering = ['-code_art']

        def __str__(self) -> str:
            return self.code_art

class ReglementTempModel(models.Model):
    code_reg = models.FloatField(primary_key=True,blank=True,null=True)
    code_mr = models.FloatField(blank=True, null=True)
    p_m_code_mr = models.FloatField(blank=True, null=True)
    p_m2_code_mr = models.FloatField(blank=True, null=True)
    code_clt = models.CharField(max_length=25, blank=True, null=True)
    num_caisse = models.FloatField(blank=True, null=True)
    montant = models.FloatField(blank=True, null=True)
    echeance = models.DateField(blank=True, null=True)
    date_reg = models.DateTimeField(blank=True, null=True)
    montant_reg = models.FloatField(blank=True, null=True)
    flag_acpte = models.BooleanField()
    montant_remis = models.FloatField(blank=True, null=True)
    mont_mde_reg1 = models.FloatField(blank=True, null=True)
    mont_mde_reg2 = models.FloatField(blank=True, null=True)
    mont_mde_reg3 = models.FloatField(blank=True, null=True)
    monnaie_rendue = models.FloatField(blank=True, null=True)
    code_agce = models.CharField(max_length=5, blank=True, null=True)
    quittance_reg = models.FloatField(blank=True, null=True)
    ref_bsc = models.CharField(max_length=20, blank=True, null=True)
    comment_bsc = models.CharField(max_length=255, blank=True, null=True)
    code_motif = models.FloatField(blank=True, null=True)
    flag_tick_fact = models.BooleanField(blank=True, null=True)
    code_agent = models.CharField(max_length=15, blank=True, null=True)
    flag_annule = models.BooleanField(blank=True, null=True)
    flag_clo = models.BooleanField(blank=True, null=True)
    code_agent_modif = models.CharField(max_length=10, blank=True, null=True)
    pass_nomclt = models.CharField(max_length=100, blank=True, null=True)
    pass_tel = models.CharField(max_length=45, blank=True, null=True)
    pass_adresse = models.CharField(max_length=100, blank=True, null=True)
    pass_cc = models.CharField(max_length=100, blank=True, null=True)
    flag_imp_tick_fact = models.BooleanField(blank=True, null=True)
    mont_mde_reg1_temp = models.FloatField(blank=True, null=True)
    mont_mde_reg2_temp = models.FloatField(blank=True, null=True)
    mont_mde_reg3_temp = models.FloatField(blank=True, null=True)
    flag_tva_fact = models.BooleanField(blank=True, null=True)
    flag_arsi_fact = models.BooleanField(blank=True, null=True)
    code_comer = models.CharField(max_length=15, blank=True, null=True)
    vente_apisoft = models.BooleanField(blank=True, null=True)
    nom_art = models.CharField(max_length=255, blank=True, null=True)
    code_vdeur = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Reglement_Temp'
        ordering = ['-code_reg']
        def __str__(self) -> str:
            return self.code_reg

class LigneTicketTemp(models.Model):
    code_lt = models.FloatField(primary_key=True)
    code_clt = models.CharField(max_length=25, blank=True, null=True)
    code_art = models.CharField(max_length=25, blank=True, null=True)
    num_caisse = models.FloatField(blank=True, null=True)
    code_reg = models.FloatField(blank=True, null=True)
    quantite = models.FloatField(blank=True, null=True)
    prix_unit = models.FloatField(blank=True, null=True)
    remise = models.FloatField(blank=True, null=True)
    numligne = models.FloatField(blank=True, null=True)
    tot_net = models.FloatField(blank=True, null=True)
    tot_brut = models.FloatField(blank=True, null=True)
    tot_net_ht = models.FloatField(blank=True, null=True)
    marge = models.FloatField(blank=True, null=True)
    prmp = models.FloatField(blank=True, null=True)
    tot_brut_ht = models.FloatField(blank=True, null=True)
    remise_mont = models.FloatField(blank=True, null=True)
    code_agce = models.CharField(max_length=5, blank=True, null=True)
    prix_vente = models.FloatField(blank=True, null=True)
    date_lt = models.DateTimeField(blank=True, null=True)
    marque_ligne = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    prix_ht_ticket = models.FloatField(blank=True, null=True)
    code_agent = models.CharField(max_length=15, blank=True, null=True)
    prix_ht_remise = models.FloatField(blank=True, null=True)
    flag_tva_lt = models.BooleanField(blank=True, null=True)
    flag_arsi_lt = models.BooleanField(blank=True, null=True)
    mt_tva_lt = models.FloatField(blank=True, null=True)
    mt_arsi_lt = models.FloatField(blank=True, null=True)
    taux_tva_lt = models.IntegerField(blank=True, null=True)
    taux_arsi_lt = models.IntegerField(blank=True, null=True)
    vente_apisoft = models.BooleanField(blank=True, null=True)
    nom_art = models.CharField(max_length=255, blank=True, null=True)
    flag_stock_ln = models.BooleanField(blank=True, null=True)
    flag_stock_ln_ann = models.BooleanField(blank=True, null=True)
    # user_id = models.FloatField(blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'LIGNE_TICKET_TEMP'
        ordering = ['-code_lt']
        def __str__(self) -> str:
            return self.code_lt

class UsersessionModel(models.Model):
    id = models.FloatField(primary_key=True)
    # ip = models.CharField(max_length=255, blank=True, null=True)
    # token = models.CharField(max_length=255, blank=True, null=True)
    # status = models.FloatField()
    created_at = models.DateTimeField()
    # updated_at = models.DateTimeField(blank=True, null=True)
    # user_id = models.FloatField()
    tampon = models.FloatField(blank=True, null=True)
    caisse = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'USERSESSION'
        ordering = ['-id']
        def __str__(self) -> str:
            return self.id

class PAgentModel(models.Model):
    code_agent = models.CharField(primary_key=True, max_length=15)
    code_fonct = models.BooleanField(blank=True, null=True)
    code_serv = models.BooleanField(blank=True, null=True)
    nom_agent = models.CharField(max_length=100)
    pnom_agent = models.CharField(max_length=100)
    tel_agent = models.CharField(max_length=20, blank=True, null=True)
    portable_agent = models.CharField(max_length=20, blank=True, null=True)
    email_agent = models.CharField(max_length=100, blank=True, null=True)
    nom_util = models.CharField(max_length=40)
    mdpasse = models.CharField(max_length=255)
    date_creat = models.DateField(blank=True, null=True)
    flag_actif = models.BooleanField(blank=True, null=True)
    code_agce = models.CharField(max_length=5, blank=True, null=True)
    addr_agent = models.CharField(max_length=100, blank=True, null=True)
    dnais_agent = models.DateField(blank=True, null=True)
    lnais_agent = models.CharField(max_length=100, blank=True, null=True)
    mat_agent = models.CharField(max_length=10, blank=True, null=True)
    photo_agent = models.CharField(max_length=255, blank=True, null=True)
    code_clt = models.CharField(max_length=15, blank=True, null=True)
    codecaisse = models.CharField(max_length=255, blank=True, null=True)
    is_root = models.BooleanField(blank=True, null=True)
    is_admin = models.BooleanField(blank=True, null=True)
    new_session = models.BooleanField(blank=True, null=True)
    notification_register_status = models.BooleanField(blank=True, null=True)
    added_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'P_AGENT'
        ordering = ['-code_agent']
        def __str__(self) -> str:
            return self.code_agent
        
class ArtFourModel(models.Model):
    code_art_four = models.FloatField(primary_key=True)
    code_four = models.CharField(max_length=25, blank=True, null=True)
    code_pua = models.FloatField(blank=True, null=True)
    # code_art = models.CharField(max_length=25, blank=True, null=True)
    code_art = models.ForeignKey(ArticleModel,models.DO_NOTHING)

    prix_achat_art_four = models.FloatField(blank=True, null=True)
    date_art_four = models.DateField(blank=True, null=True)
    ref_art_four = models.CharField(max_length=50, blank=True, null=True)
    flag_princ = models.BooleanField(blank=True, null=True)
    unite_achat_artf = models.CharField(max_length=15, blank=True, null=True)
    remise_fourart = models.FloatField(blank=True, null=True)
    coef_fourart = models.FloatField(blank=True, null=True)
    code_four_anc = models.CharField(max_length=25, blank=True, null=True)
    code_four_nou = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ART_FOUR'
        ordering = ['-code_art_four']
        def __str__(self) -> str:
            return self.code_art_four


class PFamilleArtModel(models.Model):
    code_fa = models.CharField(primary_key=True, max_length=20)
    lib_fa = models.CharField(max_length=200, blank=True, null=True)
    taxable_fa = models.BooleanField(blank=True, null=True)
    num_cpte_cptable = models.CharField(max_length=20, blank=True, null=True)
    abr_fa = models.CharField(max_length=1, blank=True, null=True)
    tmc_fa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    code_serv = models.FloatField(blank=True, null=True)
    code_depot = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'P_FAMILLE_ART'
        ordering = ['-code_fa']
        def __str__(self) -> str:
            return self.code_fa
        
class InfosartPrmppampModel(models.Model):
    code_art = models.CharField(primary_key=True,max_length=25, db_collation='USING_NLS_COMP')
    code_barre = models.CharField(max_length=20, db_collation='USING_NLS_COMP', blank=True, null=True)
    code_fa = models.CharField(max_length=25, db_collation='USING_NLS_COMP', blank=True, null=True)
    code_sr = models.CharField(max_length=25, db_collation='USING_NLS_COMP', blank=True, null=True)
    nom_art = models.CharField(max_length=255, db_collation='USING_NLS_COMP', blank=True, null=True)
    prix_ht = models.FloatField(blank=True, null=True)
    prix_ttc = models.FloatField(blank=True, null=True)
    anc_prmp = models.IntegerField(blank=True, null=True)
    nouv_prmp = models.IntegerField(blank=True, null=True)
    prix_achat_prmp = models.IntegerField(blank=True, null=True)
    prix_revient_prmp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'INFOSART_PRMPPAMP'
        ordering = ['-code_art']
        def __str__(self) -> str:
            return self.code_art
        
class Ventesession(models.Model):
    id = models.FloatField(primary_key=True)
    caisse = models.CharField(max_length=255)
    ticket = models.FloatField(blank=True, null=True)
    agent = models.CharField(max_length=15)
    etat = models.FloatField()
    flag = models.FloatField()

    class Meta:
        managed = False
        db_table = 'VENTESESSION'
        ordering = ['-id']
        def __str__(self) -> str:
            return self.id
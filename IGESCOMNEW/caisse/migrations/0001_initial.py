# Generated by Django 4.1.3 on 2023-06-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('code_art', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('code_sr', models.CharField(blank=True, max_length=25, null=True)),
                ('code_ta', models.CharField(blank=True, max_length=1, null=True)),
                ('code_taxe', models.FloatField(blank=True, null=True)),
                ('code_barre', models.CharField(blank=True, max_length=20, null=True)),
                ('nom_art', models.CharField(blank=True, max_length=255, null=True)),
                ('flag_actif', models.BooleanField(blank=True, null=True)),
                ('pamp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('prix_ht', models.FloatField(blank=True, null=True)),
                ('prix_ttc', models.FloatField(blank=True, null=True)),
                ('marge', models.FloatField(blank=True, null=True)),
                ('marque_art', models.FloatField(blank=True, null=True)),
                ('longeur', models.FloatField(blank=True, null=True)),
                ('largeur', models.FloatField(blank=True, null=True)),
                ('epaisseur', models.FloatField(blank=True, null=True)),
                ('poids_brut', models.FloatField(blank=True, null=True)),
                ('poids_net', models.FloatField(blank=True, null=True)),
                ('stock_min_gen', models.FloatField(blank=True, null=True)),
                ('stock_max_gen', models.FloatField(blank=True, null=True)),
                ('stock_phys_gen', models.FloatField(blank=True, null=True)),
                ('unite_vente', models.CharField(blank=True, max_length=10, null=True)),
                ('descr_art', models.CharField(blank=True, max_length=200, null=True)),
                ('image_art', models.CharField(blank=True, max_length=100, null=True)),
                ('date_creat', models.DateField(blank=True, null=True)),
                ('date_modif', models.DateField(blank=True, null=True)),
                ('gestionstock', models.BooleanField(blank=True, null=True)),
                ('marge_pourcent', models.FloatField(blank=True, null=True)),
                ('auteur_art', models.CharField(blank=True, max_length=100, null=True)),
                ('editeur_art', models.CharField(blank=True, max_length=100, null=True)),
                ('collection_art', models.CharField(blank=True, max_length=100, null=True)),
                ('date_paru_art', models.DateField(blank=True, null=True)),
                ('flag_art_dcom', models.BooleanField(blank=True, null=True)),
                ('coeff_vente', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('flag_sco_art', models.BooleanField(blank=True, null=True)),
                ('code_four', models.CharField(blank=True, max_length=25, null=True)),
                ('code_ndp', models.CharField(blank=True, max_length=25, null=True)),
                ('famille', models.CharField(blank=True, max_length=25, null=True)),
                ('code_ma', models.FloatField(blank=True, null=True)),
                ('code_fa', models.CharField(blank=True, max_length=25, null=True)),
                ('code_start2', models.CharField(blank=True, max_length=3, null=True)),
                ('date_peremp', models.DateField(blank=True, null=True)),
                ('code_ray', models.CharField(blank=True, max_length=25, null=True)),
                ('isbn_art', models.CharField(blank=True, max_length=25, null=True)),
                ('solde_art', models.FloatField(blank=True, null=True)),
                ('flag_caravan', models.BooleanField(blank=True, null=True)),
                ('flag_etiqtble', models.BooleanField(blank=True, null=True)),
                ('flag_modprix', models.FloatField(blank=True, null=True)),
                ('code_start', models.CharField(blank=True, max_length=3, null=True)),
                ('date_dernvte', models.DateField(blank=True, null=True)),
                ('date_prement', models.DateField(blank=True, null=True)),
                ('date_dernent', models.DateField(blank=True, null=True)),
                ('periodicite_art', models.CharField(blank=True, max_length=100, null=True)),
                ('conditionem_art', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ARTICLE',
                'ordering': ['-code_art'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReglementTempModel',
            fields=[
                ('code_reg', models.FloatField(primary_key=True, serialize=False)),
                ('code_mr', models.FloatField(blank=True, null=True)),
                ('p_m_code_mr', models.FloatField(blank=True, null=True)),
                ('p_m2_code_mr', models.FloatField(blank=True, null=True)),
                ('code_clt', models.CharField(blank=True, max_length=25, null=True)),
                ('num_caisse', models.FloatField(blank=True, null=True)),
                ('montant', models.FloatField(blank=True, null=True)),
                ('echeance', models.DateField(blank=True, null=True)),
                ('date_reg', models.DateField(blank=True, null=True)),
                ('montant_reg', models.FloatField(blank=True, null=True)),
                ('flag_acpte', models.BooleanField()),
                ('montant_remis', models.FloatField(blank=True, null=True)),
                ('mont_mde_reg1', models.FloatField(blank=True, null=True)),
                ('mont_mde_reg2', models.FloatField(blank=True, null=True)),
                ('mont_mde_reg3', models.FloatField(blank=True, null=True)),
                ('monnaie_rendue', models.FloatField(blank=True, null=True)),
                ('code_agce', models.CharField(blank=True, max_length=5, null=True)),
                ('quittance_reg', models.FloatField(blank=True, null=True)),
                ('ref_bsc', models.CharField(blank=True, max_length=20, null=True)),
                ('comment_bsc', models.CharField(blank=True, max_length=255, null=True)),
                ('code_motif', models.FloatField(blank=True, null=True)),
                ('flag_tick_fact', models.BooleanField(blank=True, null=True)),
                ('code_agent', models.CharField(blank=True, max_length=15, null=True)),
                ('flag_annule', models.BooleanField(blank=True, null=True)),
                ('flag_clo', models.BooleanField(blank=True, null=True)),
                ('code_agent_modif', models.CharField(blank=True, max_length=10, null=True)),
                ('pass_nomclt', models.CharField(blank=True, max_length=100, null=True)),
                ('pass_tel', models.CharField(blank=True, max_length=45, null=True)),
                ('pass_adresse', models.CharField(blank=True, max_length=100, null=True)),
                ('pass_cc', models.CharField(blank=True, max_length=100, null=True)),
                ('flag_imp_tick_fact', models.BooleanField(blank=True, null=True)),
                ('mont_mde_reg1_temp', models.FloatField(blank=True, null=True)),
                ('mont_mde_reg2_temp', models.FloatField(blank=True, null=True)),
                ('mont_mde_reg3_temp', models.FloatField(blank=True, null=True)),
                ('flag_tva_fact', models.BooleanField(blank=True, null=True)),
                ('flag_arsi_fact', models.BooleanField(blank=True, null=True)),
                ('code_comer', models.CharField(blank=True, max_length=15, null=True)),
                ('vente_apisoft', models.BooleanField(blank=True, null=True)),
                ('nom_art', models.CharField(blank=True, max_length=255, null=True)),
                ('code_vdeur', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'Reglement_Temp',
                'ordering': ['-code_reg'],
                'managed': True,
            },
        ),
    ]

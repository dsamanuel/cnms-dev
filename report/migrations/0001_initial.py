# Generated by Django 4.2.10 on 2024-03-05 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import report.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('portfolio', '0002_fieldoffice'),
        ('conceptnote', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_admin', '0001_initial'),
        ('program', '0003_program_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_start_date', models.DateField()),
                ('actual_end_date', models.DateField()),
                ('actual_reporting_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('actual_mc_budget_usd', models.FloatField(blank=True, null=True)),
                ('actual_cost_sharing_budget_usd', models.FloatField(blank=True, null=True)),
                ('status', models.BooleanField(choices=[(False, 'Draft'), (True, 'Submitted')], default=False, verbose_name='Status')),
                ('approval_status', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('activity', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='conceptnote.activity')),
                ('alead_agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='arcns', to='portfolio.portfolio')),
                ('alead_co_agency', models.ManyToManyField(blank=True, related_name='arco_leads', to='portfolio.portfolio')),
                ('finance_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='arfinance_lead', to='program.userroles')),
                ('program_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='arprogram_lead', to='program.userroles')),
                ('technical_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='artechnical_lead', to='program.userroles')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityReportDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('document', models.FileField(blank=True, max_length=500, null=True, upload_to=report.models.path_and_rename)),
                ('ver', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('activityreport', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='report.activityreport')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activityreportuploaded_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-uploaded_at',),
            },
        ),
        migrations.CreateModel(
            name='ActivityReportSubmit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('submission_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Draft'), (2, 'Request Submitted')], default=2, null=True)),
                ('submission_note', models.TextField(blank=True, null=True)),
                ('activityreport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.activityreport')),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.activityreportdocument')),
            ],
            options={
                'ordering': ('-submission_date',),
            },
        ),
        migrations.CreateModel(
            name='IcnReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_start_date', models.DateField()),
                ('actual_end_date', models.DateField()),
                ('actual_report_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('actual_mc_budget_usd', models.FloatField(blank=True, null=True)),
                ('actual_cost_sharing_budget_usd', models.FloatField(blank=True, null=True)),
                ('status', models.BooleanField(choices=[(False, 'Draft'), (True, 'Submitted')], default=False, verbose_name='Status')),
                ('approval_status', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('finance_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='irfinance_lead', to='program.userroles')),
                ('icn', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='conceptnote.icn')),
                ('ilead_agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ricns', to='portfolio.portfolio')),
                ('ilead_co_agency', models.ManyToManyField(blank=True, related_name='rco_leads', to='portfolio.portfolio')),
                ('program_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='irprogram_lead', to='program.userroles')),
                ('technical_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='irtechnical_lead', to='program.userroles')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IcnReportDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('document', models.FileField(blank=True, max_length=500, null=True, upload_to=report.models.path_and_rename)),
                ('ver', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('icnreport', models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='report.icnreport')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='icnreportuploaded_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-uploaded_at',),
            },
        ),
        migrations.CreateModel(
            name='IcnReportSubmit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('submission_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Draft'), (2, 'Request Submitted')], default=2, null=True)),
                ('submission_note', models.TextField(blank=True, null=True)),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.icnreportdocument')),
                ('icnreport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.icnreport')),
            ],
            options={
                'ordering': ('-submission_date',),
            },
        ),
        migrations.CreateModel(
            name='IcnReportSubmitApproval_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('approval_note', models.TextField(blank=True, null=True)),
                ('approval_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending Review'), (2, 'Require Doc Update'), (3, 'Request Approved'), (4, 'Request Rejected')], default=1, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.icnreportdocument')),
                ('submit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.icnreportsubmit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.userroles')),
            ],
        ),
        migrations.CreateModel(
            name='IcnReportSubmitApproval_P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('approval_note', models.TextField(blank=True, null=True)),
                ('approval_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending Review'), (2, 'Require Doc Update'), (3, 'Request Approved'), (4, 'Request Rejected')], default=1, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.icnreportdocument')),
                ('submit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.icnreportsubmit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.userroles')),
            ],
        ),
        migrations.CreateModel(
            name='IcnReportSubmitApproval_F',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('approval_note', models.TextField(blank=True, null=True)),
                ('approval_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending Review'), (2, 'Require Doc Update'), (3, 'Request Approved'), (4, 'Request Rejected')], default=1, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.icnreportdocument')),
                ('submit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.icnreportsubmit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.userroles')),
            ],
        ),
        migrations.CreateModel(
            name='IcnReportImplementationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icnreport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.icnreport')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_admin.region')),
                ('woreda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_admin.woreda')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_admin.zone')),
            ],
        ),
        migrations.CreateModel(
            name='IcnReportImpact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impact_pilot', models.IntegerField(blank=True, null=True)),
                ('impact_scaleup', models.IntegerField(blank=True, null=True)),
                ('icnreport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.icnreport')),
                ('impact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conceptnote.impact')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityReportSubmitApproval_T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('approval_note', models.TextField(blank=True, null=True)),
                ('approval_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending Review'), (2, 'Require Doc Update'), (3, 'Request Approved'), (4, 'Request Rejected')], default=1, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.activityreportdocument')),
                ('submit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.activityreportsubmit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.userroles')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityReportSubmitApproval_P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('approval_note', models.TextField(blank=True, null=True)),
                ('approval_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending Review'), (2, 'Require Doc Update'), (3, 'Request Approved'), (4, 'Request Rejected')], default=1, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.activityreportdocument')),
                ('submit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.activityreportsubmit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.userroles')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityReportSubmitApproval_F',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('approval_note', models.TextField(blank=True, null=True)),
                ('approval_status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending Review'), (2, 'Require Doc Update'), (3, 'Request Approved'), (4, 'Request Rejected')], default=1, null=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.activityreportdocument')),
                ('submit_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report.activityreportsubmit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.userroles')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityReportImplementationArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityreport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.activityreport')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_admin.region')),
                ('woreda', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_admin.woreda')),
                ('zone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_admin.zone')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityReportImpact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_impact_pilot', models.IntegerField(blank=True, null=True)),
                ('actual_impact_scaleup', models.IntegerField(blank=True, null=True)),
                ('activityimpact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conceptnote.activityimpact')),
                ('activityreport', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report.activityreport')),
            ],
        ),
    ]

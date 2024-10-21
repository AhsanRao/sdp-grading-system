# Generated by Django 4.2.9 on 2024-04-24 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_examinermidprojectpresentation_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="examinermidprojectpresentation",
            name="examiner",
            field=models.ForeignKey(
                default=6,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="examiner_presentations",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="examinermidprojectpresentation",
            name="format_score",
            field=models.DecimalField(
                decimal_places=0,
                help_text="Max 20 - Formatting and clarity of presentation slides, completion of presentation on time.",
                max_digits=4,
            ),
        ),
        migrations.AlterField(
            model_name="examinermidprojectpresentation",
            name="report_score",
            field=models.DecimalField(
                decimal_places=0,
                help_text="Max 20 - Report formatting, report contents and conclusions.",
                max_digits=4,
            ),
        ),
        migrations.AlterField(
            model_name="examinermidprojectpresentation",
            name="technical_content_score",
            field=models.DecimalField(
                decimal_places=0,
                help_text="Max 40 - Covering all significant design steps, decisions, analysis and results.",
                max_digits=4,
            ),
        ),
        migrations.AlterField(
            model_name="examinermidprojectpresentationqa",
            name="qa_score",
            field=models.DecimalField(
                decimal_places=0,
                help_text="Max 20 - Showing adequate knowledge and understanding of the subject and providing satisfying answers to questions.",
                max_digits=4,
            ),
        ),
    ]

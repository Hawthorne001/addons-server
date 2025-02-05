# Generated by Django 4.2.13 on 2024-06-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abuse', '0033_abusereport_illegal_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='abusereport',
            name='illegal_subcategory',
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (None, 'None'),
                    (1, 'Something else'),
                    (2, 'Insufficient information on traders'),
                    (3, 'Non-compliance with pricing regulations'),
                    (
                        4,
                        'Hidden advertisement or commercial communication, including by influencers',
                    ),
                    (
                        5,
                        'Misleading information about the characteristics of the goods and services',
                    ),
                    (6, 'Misleading information about the consumer’s rights'),
                    (7, 'Biometric data breach'),
                    (8, 'Missing processing ground for data'),
                    (9, 'Right to be forgotten'),
                    (10, 'Data falsification'),
                    (11, 'Defamation'),
                    (12, 'Discrimination'),
                    (
                        13,
                        'Illegal incitement to violence and hatred based on protected characteristics (hate speech)',
                    ),
                    (14, 'Design infringements'),
                    (15, 'Geographical indications infringements'),
                    (16, 'Patent infringements'),
                    (17, 'Trade secret infringements'),
                    (
                        18,
                        'Violation of EU law relevant to civic discourse or elections',
                    ),
                    (
                        19,
                        'Violation of national law relevant to civic discourse or elections',
                    ),
                    (
                        20,
                        'Misinformation, disinformation, foreign information manipulation and interference',
                    ),
                    (21, 'Non-consensual image sharing'),
                    (
                        22,
                        "Non-consensual items containing deepfake or similar technology using a third party's features",
                    ),
                    (23, 'Online bullying/intimidation'),
                    (24, 'Stalking'),
                    (25, 'Adult sexual material'),
                    (
                        26,
                        'Image-based sexual abuse (excluding content depicting minors)',
                    ),
                    (27, 'Age-specific restrictions concerning minors'),
                    (28, 'Child sexual abuse material'),
                    (29, 'Grooming/sexual enticement of minors'),
                    (30, 'Illegal organizations'),
                    (31, 'Risk for environmental damage'),
                    (32, 'Risk for public health'),
                    (33, 'Terrorist content'),
                    (34, 'Inauthentic accounts'),
                    (35, 'Inauthentic listings'),
                    (36, 'Inauthentic user reviews'),
                    (37, 'Impersonation or account hijacking'),
                    (38, 'Phishing'),
                    (39, 'Pyramid schemes'),
                    (40, 'Content promoting eating disorders'),
                    (41, 'Self-mutilation'),
                    (42, 'Suicide'),
                    (43, 'Prohibited or restricted products'),
                    (44, 'Unsafe or non-compliant products'),
                    (45, 'Coordinated harm'),
                    (46, 'Gender-based violence'),
                    (47, 'Human exploitation'),
                    (48, 'Human trafficking'),
                    (49, 'General calls or incitement to violence and/or hatred'),
                ],
                default=None,
                help_text='Specific violation of illegal content',
                null=True,
            ),
        ),
    ]

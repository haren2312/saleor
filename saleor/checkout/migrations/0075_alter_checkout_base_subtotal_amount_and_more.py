# Generated by Django 4.2.15 on 2025-05-06 09:54

from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0074_alter_checkout_external_shipping_method_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkout",
            name="base_subtotal_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="base_total_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="discount_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal("0.0"), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="shipping_price_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="shipping_price_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="subtotal_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="subtotal_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="total_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="total_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkout",
            name="undiscounted_base_shipping_price_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkoutline",
            name="price_override",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=20, null=True
            ),
        ),
        migrations.AlterField(
            model_name="checkoutline",
            name="total_price_gross_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkoutline",
            name="total_price_net_amount",
            field=models.DecimalField(
                decimal_places=3, default=Decimal(0), max_digits=20
            ),
        ),
        migrations.AlterField(
            model_name="checkoutline",
            name="undiscounted_unit_price_amount",
            field=models.DecimalField(
                blank=True, decimal_places=3, max_digits=20, null=True
            ),
        ),
    ]

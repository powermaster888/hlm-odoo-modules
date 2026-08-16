# Odoo Community Deployment (Dokploy)

## Current deployment

- URL: https://odoo.zentrabase.com
- Host: Dokploy on VPS 76.13.101.236 (Hostinger, Boston)
- Dokploy project: AI Infrastructure > production
- Compose name: odoo-community (composeId: GSE9ESL1tCpID32WbiFSJ)
- DB: odoo (PostgreSQL 16), 161 modules installed
- Backups: pg_dump sidecar daily, 7-day retention (odoo-community-backups volume)
- Credentials: 1Password "Odoo Community (odoo.zentrabase.com)" (admin/DB/master)
  and "HLM Odoo Community Users (odoo.zentrabase.com)" (6 user accounts)

## Architecture (docker-compose.yml)

- odoo-community-db: postgres:16-alpine, healthchecked
- odoo-community-addons: alpine/git one-shot, clones pinned addon repos into shared volume
- odoo-community-init: odoo:19.0 one-shot, waits for DB, installs module list, sets admin password
- odoo-community-web: odoo:19.0, pip installs python-barcode/openpyxl/xlrd into filestore volume
- odoo-community-backup: postgres:16-alpine sidecar, daily pg_dump -Fc, 7-day rotation
- Traefik labels injected by Dokploy domain config (odoo.zentrabase.com, letsencrypt)

## Secrets

@POSTGRES_PASSWORD@ / @MASTER_PASSWORD@ / @ODOO_ADMIN_PASSWORD@ placeholders in this file.
Actual values: Dokploy compose env config + 1Password. Never commit real secrets.

## Deploying changes

1. Edit docker-compose.yml (placeholders only, real env via Dokploy compose.saveEnvironment)
2. base64 it or update via Dokploy API compose.update (composeId above)
3. Trigger compose.deploy; init container auto-installs any new modules (idempotent guard)

## Migration to a new server (runbook)

1. New VPS: install Dokploy, create project/environment
2. Copy this compose into new Dokploy (update domain if URL changes)
3. Data: grab latest dump from odoo-community-backups volume (pg_dump -Fc format)
   Restore: pg_restore -d odoo --clean <dump> into new DB container
4. Copy filestore volume (odoo-community-filestore) - rsync or tar over SSH
5. Test: /web/login 200 + admin login + module count 161
6. DNS: flip odoo.zentrabase.com Cloudflare record to new IP
7. Verify TLS issued, then decommission old server after 30-day retention

## Addon sources (all pinned commits)

odoomates/odooapps, OCA/account-financial-reporting, OCA/account-reconcile,
OCA/reporting-engine, OCA/server-ux, OCA/mis-builder, OCA/stock-logistics-barcode,
OCA/helpdesk, OCA/bank-statement-import, OCA/account-financial-tools,
OCA/account-payment, OCA/bank-payment, OCA/currency, OCA/server-tools,
OCA/sale-workflow, OCA/web, OCA/stock-logistics-warehouse,
komit-consulting/stock-logistics-barcode (PR #742 stock_barcodes),
komit-consulting/web (PR #3429 web_widget_numeric_step),
powermaster888/hlm-odoo-modules (hlm_security, hlm_studio_rebuild)

Backup mirror of stock_barcodes PR branch: powermaster888/stock-logistics-barcode (private)

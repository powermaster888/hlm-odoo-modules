# HLM Odoo Modules

Custom Odoo 19 Community modules for Healthy Living Medical Supplies (HLM).

## Modules

### hlm_security
Rebuilds the 16 custom security groups from Odoo Online production:
- Show Menu - Master / User / Salesperson
- Per-app menu switches (Accounting, Appraisal, Attendance, Calendar, Documents, Employee, Leave, Payroll)
- HLM Cost Visibility, Mask Non-local Vendor on WH/IN, Hide Stock Report Buttons, Allow Vendor Bills Partner Button

Stage 1 (installed): group definitions only.
Stage 2 (pending): menu visibility rules + view-level cost masking.

### hlm_studio_rebuild
Rebuilds Studio customizations:
- hlm_pos_cashier: POS cashier on account.move (replaces x_studio_invoice_employee)
- hlm_delivery_origin: delivery order refs on account.move

## deploy/
Dokploy deployment files and migration runbook for https://odoo.zentrabase.com.
See deploy/README.md.

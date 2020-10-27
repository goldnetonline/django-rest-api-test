# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminBanks(models.Model):
    admin = models.ForeignKey('Admins', models.DO_NOTHING)
    bank_name = models.CharField(max_length=191)
    bank_code = models.CharField(max_length=10)
    account_number = models.CharField(max_length=10)
    account_name = models.CharField(max_length=191)
    recipient_code = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_banks'


class AdminLoanBookmarks(models.Model):
    admin = models.ForeignKey('Admins', models.DO_NOTHING)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    next_cta = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_loan_bookmarks'


class AdminLoanNotes(models.Model):
    admin = models.ForeignKey('Admins', models.DO_NOTHING)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    note = models.TextField()
    options = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_loan_notes'


class Admins(models.Model):
    first_name = models.CharField(max_length=191)
    last_name = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191)
    phone = models.CharField(unique=True, max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191)
    role_id = models.SmallIntegerField(blank=True, null=True)
    branch = models.ForeignKey('Branches', models.DO_NOTHING, blank=True, null=True)
    avatar = models.CharField(max_length=191, blank=True, null=True)
    must_change_password = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admins'


class AutomationStrategies(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=12)
    entity_id = models.PositiveIntegerField()
    require_auth = models.IntegerField()
    depends_on = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    approval_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'automation_strategies'


class Branches(models.Model):
    name = models.CharField(max_length=191)
    address = models.TextField()
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    branch_manager = models.ForeignKey(Admins, models.DO_NOTHING)
    target = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    target_begins = models.DateField(blank=True, null=True)
    target_ends = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'


class DeclineMessages(models.Model):
    title = models.CharField(max_length=191)
    subject = models.CharField(max_length=191)
    message = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decline_messages'


class ExpenseAuditTrails(models.Model):
    expense_id = models.PositiveIntegerField()
    status = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    admin_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense_audit_trails'


class Expenses(models.Model):
    admin = models.ForeignKey(Admins, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=191)
    purpose = models.TextField(blank=True, null=True)
    pending_disbursal = models.IntegerField(blank=True, null=True)
    amount_approved = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    amount_retired = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    retirement_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    disbursed_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expenses'


class Faqs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=191)
    content = models.TextField()
    category = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'faqs'


class FileTypes(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file_types'


class Files(models.Model):
    disk_name = models.TextField(blank=True, null=True)
    file_path = models.TextField()
    file_size = models.IntegerField()
    content_type = models.TextField()
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    entity = models.CharField(max_length=191, blank=True, null=True)
    entity_id = models.PositiveIntegerField(blank=True, null=True)
    is_public = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class InvestmentCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    image = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=191, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investment_categories'


class InvestmentReferrals(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=191)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(unique=True, max_length=191, blank=True, null=True)
    email = models.CharField(unique=True, max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investment_referrals'


class Investments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=191)
    category = models.ForeignKey(InvestmentCategories, models.DO_NOTHING, blank=True, null=True)
    image = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=8)
    tenor = models.IntegerField()
    rate = models.FloatField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_name = models.CharField(max_length=191)
    investor_count = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investments'


class LoanRepayments(models.Model):
    transaction_history = models.ForeignKey('Transactions', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    no_of_days = models.SmallIntegerField()
    is_waived = models.IntegerField()
    waiver_reason = models.CharField(max_length=191, blank=True, null=True)
    waiver_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    waived_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='waived_by', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    loandisk_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_repayments'


class LoanStatusAuditTrails(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    loan = models.ForeignKey('Loans', models.DO_NOTHING)
    status = models.CharField(max_length=30)
    entered_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='entered_by', blank=True, null=True)
    admin = models.ForeignKey('TenantAdmins', models.DO_NOTHING, blank=True, null=True)
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_status_audit_trails'


class LoanType(models.Model):
    title = models.CharField(max_length=199)
    description = models.TextField(blank=True, null=True)
    interest_rate = models.DecimalField(max_digits=3, decimal_places=2)
    overdue_interest = models.DecimalField(max_digits=3, decimal_places=2)
    is_active = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    amounts = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loan_type'


class Loans(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tenor = models.SmallIntegerField()
    purpose = models.CharField(max_length=191)
    status = models.CharField(max_length=30)
    decline_reason = models.SmallIntegerField(blank=True, null=True)
    request_ip_address = models.CharField(max_length=45, blank=True, null=True)
    offer_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_payable = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_principal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    outstanding_interest = models.DecimalField(max_digits=8, decimal_places=2)
    repayment_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    interest = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    offer_date = models.DateTimeField(blank=True, null=True)
    interest_initial_date = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    due_payable = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    overdue_interest = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    should_service_by = models.ForeignKey('Tenants', models.DO_NOTHING, db_column='should_service_by', blank=True, null=True)
    is_serviced_by = models.ForeignKey('Tenants', models.DO_NOTHING, db_column='is_serviced_by', blank=True, null=True)
    uses_system_balance = models.IntegerField(blank=True, null=True)
    last_rejected_by = models.ForeignKey('Tenants', models.DO_NOTHING, db_column='last_rejected_by', blank=True, null=True)
    current_due = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    revenue = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    transaction_charges = models.DecimalField(max_digits=15, decimal_places=4)
    commission = models.DecimalField(max_digits=15, decimal_places=4)
    tenant_profit = models.DecimalField(max_digits=15, decimal_places=4)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    loan_type_id = models.SmallIntegerField(blank=True, null=True)
    lead_source_id = models.PositiveIntegerField(blank=True, null=True)
    repayment_links = models.TextField(blank=True, null=True)
    repayment_links_added = models.DateTimeField(blank=True, null=True)
    repayment_links_expires = models.DateTimeField(blank=True, null=True)
    loandisk_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loans'


class LoginAsTenants(models.Model):
    tenant_id = models.PositiveIntegerField()
    hash = models.CharField(max_length=191)
    redirect = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_as_tenants'


class LoginAsUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    hash = models.CharField(max_length=191)
    redirect = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_as_users'


class PendingDisbursals(models.Model):
    type = models.CharField(max_length=13, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    loan = models.OneToOneField(Loans, models.DO_NOTHING, blank=True, null=True)
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING, blank=True, null=True)
    tenant_payout_id = models.PositiveIntegerField(blank=True, null=True)
    expense_id = models.PositiveIntegerField(blank=True, null=True)
    reference = models.CharField(unique=True, max_length=100)
    transfer_code = models.CharField(max_length=100)
    transfer_id = models.IntegerField(unique=True)
    status = models.CharField(max_length=100)
    integration = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=191, blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    account = models.CharField(max_length=191, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pending_disbursals'


class ProductionTasks(models.Model):
    class_field = models.CharField(db_column='class', max_length=191)  # Field renamed because it was a Python reserved word.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'production_tasks'


class ProspectiveUserSources(models.Model):
    name = models.CharField(max_length=191)
    short_name = models.CharField(max_length=191)
    company = models.CharField(max_length=191, blank=True, null=True)
    contact_email = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospective_user_sources'


class ProspectiveUsers(models.Model):
    name = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191)
    phone = models.CharField(max_length=191, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    source = models.ForeignKey(ProspectiveUserSources, models.DO_NOTHING, blank=True, null=True)
    signed_up = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prospective_users'


class PublicHolidays(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_holidays'


class RedirectLinks(models.Model):
    user_id = models.PositiveIntegerField()
    hash_key = models.TextField()
    redirect_link = models.TextField()
    guard = models.CharField(max_length=9, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expire_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redirect_links'


class Reports(models.Model):
    key = models.CharField(max_length=191)
    value = models.TextField()
    entity = models.CharField(max_length=191, blank=True, null=True)
    entity_id = models.PositiveIntegerField(blank=True, null=True)
    expiry = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reports'


class SetupCompleted(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    step = models.CharField(max_length=30)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setup_completed'


class TenancyPlans(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField()
    signon_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_trading_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_daily_loans = models.SmallIntegerField(blank=True, null=True)
    commision = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenancy_plans'


class TenantAdmins(models.Model):
    first_name = models.CharField(max_length=191)
    last_name = models.CharField(max_length=191)
    email = models.CharField(unique=True, max_length=191)
    phone = models.CharField(unique=True, max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191)
    role_id = models.SmallIntegerField(blank=True, null=True)
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING, blank=True, null=True)
    must_change_password = models.IntegerField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_admins'


class TenantBalanceBackups(models.Model):
    tenant_id = models.PositiveIntegerField()
    key = models.CharField(max_length=191, blank=True, null=True)
    data = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_balance_backups'


class TenantBalanceHistories(models.Model):
    tenant_id = models.PositiveIntegerField()
    type = models.CharField(max_length=24, blank=True, null=True)
    previous_balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    new_balance = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    computed_balance = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    topup_accumulation = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    transaction_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    duplicate_transaction_id = models.PositiveIntegerField(blank=True, null=True)
    duplicate_transaction_treated = models.IntegerField(blank=True, null=True)
    loan_id = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_balance_histories'


class TenantBalances(models.Model):
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING)
    disbursable_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    payout_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    last_payout = models.DateTimeField(blank=True, null=True)
    last_topup = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_balances'


class TenantBankPendingVerifications(models.Model):
    tenant_id = models.PositiveIntegerField()
    tenant_bank_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_bank_pending_verifications'


class TenantBanks(models.Model):
    tenant_id = models.PositiveIntegerField()
    bank_name = models.CharField(max_length=191)
    bank_code = models.CharField(max_length=10)
    account_number = models.CharField(max_length=10)
    account_name = models.CharField(max_length=191)
    recipient_code = models.CharField(max_length=191, blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    verified_by = models.ForeignKey(Admins, models.DO_NOTHING, db_column='verified_by', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_banks'


class TenantOldDatas(models.Model):
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING)
    table = models.CharField(max_length=191)
    data = models.TextField()
    action = models.CharField(max_length=6, blank=True, null=True)
    performed_by = models.ForeignKey(TenantAdmins, models.DO_NOTHING, db_column='performed_by', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_old_datas'


class TenantPayoutRequests(models.Model):
    tenant_id = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=10)
    pending_disbursal = models.IntegerField(blank=True, null=True)
    processed_by = models.PositiveIntegerField(blank=True, null=True)
    disbursed_at = models.DateTimeField(blank=True, null=True)
    processed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_payout_requests'


class TenantPaystackRecipients(models.Model):
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    recipient_code = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_paystack_recipients'


class TenantReferrals(models.Model):
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING, blank=True, null=True)
    hash = models.CharField(unique=True, max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191)
    phone = models.CharField(max_length=191, blank=True, null=True)
    company_name = models.CharField(max_length=191, blank=True, null=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    referral_note = models.CharField(max_length=191, blank=True, null=True)
    referred_tenant = models.ForeignKey('Tenants', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=19)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_referrals'


class TenantRelationshipOfficerHistories(models.Model):
    tenant_id = models.PositiveIntegerField()
    old_officer_id = models.PositiveIntegerField()
    new_officer_id = models.PositiveIntegerField()
    date_of_reassignment = models.DateField()
    reason_of_reassignment = models.CharField(max_length=191)
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_relationship_officer_histories'


class TenantServicedLoans(models.Model):
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING, blank=True, null=True)
    loan = models.ForeignKey(Loans, models.DO_NOTHING, blank=True, null=True)
    action = models.CharField(max_length=9)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_serviced_loans'


class TenantSubscriptionHistories(models.Model):
    tenant = models.ForeignKey('Tenants', models.DO_NOTHING)
    plan = models.ForeignKey(TenancyPlans, models.DO_NOTHING)
    transaction = models.ForeignKey('Transactions', models.DO_NOTHING, blank=True, null=True)
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenant_subscription_histories'


class Tenants(models.Model):
    account_number = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(TenantAdmins, models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey(TenancyPlans, models.DO_NOTHING, blank=True, null=True)
    relationship_officer = models.PositiveIntegerField(blank=True, null=True)
    signon_fee_paid = models.IntegerField()
    paystack_api_key = models.CharField(max_length=191, blank=True, null=True)
    paystack_api_secret = models.CharField(max_length=191, blank=True, null=True)
    paystack_id = models.CharField(max_length=100, blank=True, null=True)
    subscription = models.ForeignKey(TenantSubscriptionHistories, models.DO_NOTHING, blank=True, null=True)
    default_disburse_channel = models.CharField(max_length=9, blank=True, null=True)
    agreed_to_terms = models.IntegerField()
    agreed_to_terms_date = models.DateTimeField(blank=True, null=True)
    balance_reconciled = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tenants'


class Transactions(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    card_id = models.PositiveIntegerField()
    reference = models.CharField(unique=True, max_length=191, blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    is_duplicate = models.IntegerField()
    is_duplicate_of = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=191, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    customer_code = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=191, blank=True, null=True)
    loan_id = models.PositiveIntegerField(blank=True, null=True)
    expense_id = models.PositiveIntegerField(blank=True, null=True)
    type = models.CharField(max_length=19, blank=True, null=True)
    tenant = models.ForeignKey(Tenants, models.DO_NOTHING, blank=True, null=True)
    tenant_payout_id = models.PositiveIntegerField(blank=True, null=True)
    tenant_share = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    commission_rate = models.SmallIntegerField(blank=True, null=True)
    processor_share = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class UserBanks(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    bank_name = models.CharField(max_length=191)
    bank_code = models.CharField(max_length=10)
    account_number = models.CharField(max_length=11)
    account_name = models.CharField(max_length=191)
    bvn = models.CharField(unique=True, max_length=12, blank=True, null=True)
    bvn_name = models.CharField(max_length=191, blank=True, null=True)
    recipient_code = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_banks'


class UserBlockHistories(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    block_reason = models.TextField(blank=True, null=True)
    blocked_by = models.PositiveIntegerField()
    unblocked_by = models.PositiveIntegerField(blank=True, null=True)
    unblock_comment = models.TextField(blank=True, null=True)
    unblocked_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_block_histories'


class UserCards(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    authorization_code = models.TextField()
    bin = models.CharField(max_length=20, blank=True, null=True)
    last4 = models.CharField(max_length=4, blank=True, null=True)
    exp_month = models.CharField(max_length=3, blank=True, null=True)
    exp_year = models.CharField(max_length=4, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)
    card_type = models.CharField(max_length=60, blank=True, null=True)
    bank = models.CharField(max_length=120, blank=True, null=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    reusable = models.IntegerField(blank=True, null=True)
    signature = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_cards'


class UserCreditReports(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    file = models.ForeignKey(Files, models.DO_NOTHING)
    provider_key = models.CharField(max_length=5, blank=True, null=True)
    provider_name = models.CharField(max_length=191, blank=True, null=True)
    added_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='added_by', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_credit_reports'


class UserEmployers(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=191)
    qualification = models.CharField(max_length=191, blank=True, null=True)
    occupation = models.CharField(max_length=191, blank=True, null=True)
    address = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_employers'


class UserFiles(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    file_type = models.ForeignKey(FileTypes, models.DO_NOTHING, blank=True, null=True)
    file = models.ForeignKey(Files, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_files'


class UserGuarantors(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    name = models.CharField(max_length=191)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=191, blank=True, null=True)
    relationship = models.CharField(max_length=50)
    address = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    employment_status = models.CharField(max_length=50, blank=True, null=True)
    employer_name = models.CharField(max_length=191, blank=True, null=True)
    employer_address = models.CharField(max_length=191, blank=True, null=True)
    employer_city = models.CharField(max_length=191, blank=True, null=True)
    employer_state = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_guarantors'


class UserInvestments(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    investment = models.ForeignKey(Investments, models.DO_NOTHING, blank=True, null=True)
    tenor = models.IntegerField()
    rate = models.FloatField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    unit_purchased = models.IntegerField()
    investment_total = models.DecimalField(max_digits=15, decimal_places=4)
    invested_at = models.DateTimeField()
    mature_at = models.DateTimeField(blank=True, null=True)
    transaction_id = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=9)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_investments'


class UserSavingBalanceHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    saving = models.ForeignKey('UserSavings', models.DO_NOTHING)
    type = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    previous_rate = models.FloatField(blank=True, null=True)
    new_rate = models.FloatField(blank=True, null=True)
    previous_principal = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    previous_value = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    new_principal = models.DecimalField(max_digits=15, decimal_places=4)
    transaction = models.OneToOneField(Transactions, models.DO_NOTHING, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_saving_balance_histories'


class UserSavings(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    type = models.CharField(max_length=11)
    title = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    tenor = models.IntegerField(blank=True, null=True)
    rate = models.FloatField()
    principal = models.DecimalField(max_digits=15, decimal_places=4)
    status = models.CharField(max_length=9)
    commenced_at = models.DateTimeField()
    completed_at = models.DateTimeField(blank=True, null=True)
    auto_save = models.CharField(max_length=191, blank=True, null=True)
    auto_save_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    next_auto_save_date = models.DateField(blank=True, null=True)
    interest_initial_date = models.DateTimeField(blank=True, null=True)
    next_withdrawal_date = models.DateTimeField(blank=True, null=True)
    mature_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_savings'


class UserSavingsPayoutRequests(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    saving = models.ForeignKey(UserSavings, models.DO_NOTHING, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    penalty = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    disburse_amount = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    status = models.CharField(max_length=10)
    processed_by = models.PositiveIntegerField(blank=True, null=True)
    processed_at = models.DateTimeField(blank=True, null=True)
    transaction = models.OneToOneField(Transactions, models.DO_NOTHING, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=6, blank=True, null=True)
    wallet = models.CharField(max_length=191, blank=True, null=True)
    bank = models.ForeignKey(UserBanks, models.DO_NOTHING, blank=True, null=True)
    disbursed_at = models.DateTimeField(blank=True, null=True)
    pending_disbursal = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_savings_payout_requests'


class UserWalletBalanceHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    wallet = models.ForeignKey('UserWallets', models.DO_NOTHING)
    type = models.CharField(max_length=10)
    previous_balance = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    new_balance = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    transaction = models.OneToOneField(Transactions, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_wallet_balance_histories'


class UserWallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    account_type = models.CharField(max_length=14)
    balance = models.FloatField()
    last_deposit_at = models.DateTimeField(blank=True, null=True)
    last_withdrawal_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_wallets'


class Users(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(unique=True, max_length=191)
    avatar = models.CharField(max_length=191, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    house_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    town = models.CharField(max_length=191, blank=True, null=True)
    cda = models.CharField(max_length=191, blank=True, null=True)
    lcda = models.CharField(max_length=191, blank=True, null=True)
    division = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    employment_status = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=191)
    must_change_password = models.IntegerField(blank=True, null=True)
    is_blocked = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    apply_ban_lifted = models.IntegerField(blank=True, null=True)
    lead_source_id = models.PositiveIntegerField(blank=True, null=True)
    referral_code = models.ForeignKey(InvestmentReferrals, models.DO_NOTHING, db_column='referral_code', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

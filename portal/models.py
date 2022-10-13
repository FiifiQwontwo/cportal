from django.db import models


class Chapels(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        managed = False
        verbose_name = 'chapel'
        verbose_name_plural = 'chapels'
        db_table = 'chapels'

    def __str__(self):
        return self.name


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Groups(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        managed = False
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        db_table = 'groups'

    def __str__(self):
        return self.name


class Members(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=6, blank=True, null=True)
    chapel = models.ForeignKey(Chapels, models.DO_NOTHING, related_name='chapel_members')
    group = models.ForeignKey(Groups, models.DO_NOTHING, related_name='group_members')
    dob = models.DateField(blank=True, null=True)
    phone_number = models.CharField(unique=True, max_length=10)
    whatsapp_number = models.CharField(max_length=255, blank=True, null=True)
    other_phone_number = models.CharField(max_length=255, blank=True, null=True)
    area_of_residence = models.CharField(max_length=255, blank=True, null=True)
    gps_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        managed = False
        verbose_name = 'member'
        verbose_name_plural = 'members'
        db_table = 'members'

    def __str__(self):
        return self.last_name


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'roles'


class DBUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255, blank=True, null=True)
    chapel = models.ForeignKey(Chapels, models.DO_NOTHING, related_name='user_chapel')
    group = models.ForeignKey(Groups, models.DO_NOTHING, related_name='user_groups')
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.name


class RoleUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    user = models.ForeignKey('DBUser', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        managed = False
        db_table = 'role_user'


class Attendances(models.Model):
    id = models.BigAutoField(primary_key=True)
    member = models.ForeignKey('Members', models.DO_NOTHING, related_name='members_attendance')
    is_present = models.IntegerField()
    reason = models.CharField(max_length=17, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    service_date = models.DateTimeField()
    completed = models.IntegerField()
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        managed = False
        verbose_name = 'attendance'
        verbose_name_plural = 'attendances'
        db_table = 'attendances'


class AttendanceSummaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    weekday = models.CharField(max_length=255)
    attendance_date = models.DateTimeField()
    group = models.ForeignKey('Groups', models.DO_NOTHING, related_name='grouped')
    total_present = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)
    total_absent = models.CharField(max_length=255)
    present_percentage = models.CharField(max_length=255)

    class Meta:
        managed = False
        verbose_name = 'attendance_summary'
        verbose_name_plural = 'attendance_summaries'
        db_table = 'attendance_summaries'

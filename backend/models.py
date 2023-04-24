from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)


class AupData(models.Model):
    id_aup = models.ForeignKey('TblAup', models.DO_NOTHING, db_column='id_aup')
    id_block = models.ForeignKey('DBlocks', models.DO_NOTHING, db_column='id_block')
    shifr = models.CharField(max_length=30)
    id_part = models.ForeignKey('DPart', models.DO_NOTHING, db_column='id_part')
    id_module = models.ForeignKey('DModules', models.DO_NOTHING, db_column='id_module')
    id_group = models.IntegerField()
    id_type_record = models.ForeignKey('DTypeRecord', models.DO_NOTHING, db_column='id_type_record')
    discipline = models.CharField(max_length=150)
    id_period = models.IntegerField()
    id_type_control = models.ForeignKey('DControlType', models.DO_NOTHING, db_column='id_type_control')
    amount = models.IntegerField()
    id_edizm = models.ForeignKey('DEdIzmereniya', models.DO_NOTHING, db_column='id_edizm')
    zet = models.IntegerField()
    num_row = models.IntegerField()


class DBlocks(models.Model):
    title = models.CharField(max_length=255)


class DCompetencyCode(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Код компетенции"
        verbose_name_plural = "Коды компетенции"


class DControlType(models.Model):
    title = models.CharField(max_length=255)


class DEdIzmereniya(models.Model):
    title = models.CharField(max_length=255)


class DGeneration(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ="Поколение"
        verbose_name_plural = "Поколения"


class DModules(models.Model):
    title = models.CharField(max_length=255)


class DPart(models.Model):
    title = models.CharField(max_length=255)


class DPeriod(models.Model):
    title = models.CharField(max_length=255)


class DSpecialozationType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип специализации"
        verbose_name_plural = "Типы специализаций"


class DTypeRecord(models.Model):
    title = models.CharField(max_length=255)


class DTypeStandard(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Стандарт"
        verbose_name_plural = "Стандарты"


class Groups(models.Model):
    id_group = models.AutoField(primary_key=True)
    name_group = models.CharField(max_length=255)
    color = models.CharField(max_length=8)
    weight = models.IntegerField()


class SprBranch(models.Model):
    id_branch = models.AutoField(primary_key=True)
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.city


class SprCompetency(models.Model):
    d_competency_code = models.ForeignKey(DCompetencyCode, models.DO_NOTHING)
    code_number = models.IntegerField(default=0)
    title = models.TextField()

    def __str__(self):
        return f"[{self.d_competency_code.title}-{self.code_number}] {self.title}"

    class Meta:
        verbose_name = "Компетенция"
        verbose_name_plural = "Компетенции"


class SprCompulsoryDiscipline(models.Model):
    name = models.CharField(max_length=255, db_column="name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обязательная дисциплина"
        verbose_name_plural = "Обязательные дисциплины"


class SprDegreeEducation(models.Model):
    name_deg = models.CharField(max_length=255)


class SprFaculty(models.Model):
    id_faculty = models.AutoField(primary_key=True)
    name_faculty = models.CharField(max_length=255)
    id_branch = models.ForeignKey(SprBranch, models.DO_NOTHING, db_column='id_branch')
    dean = models.CharField(max_length=255)


class TblRealizedOkso(models.Model):
    spr_branch = models.ForeignKey(SprBranch, models.DO_NOTHING, db_column='spr_branch_id_branch')
    program_code = models.ForeignKey("SprOkco", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.program_code}, {self.spr_branch.city}"

    class Meta:
        verbose_name = 'Реализуемый ОКСО'
        verbose_name_plural = "Реализуемые ОКСО"


class SprFgosVo(models.Model):
    tbl_realized_okso = models.ForeignKey(TblRealizedOkso, models.DO_NOTHING, verbose_name="Реализуемый ОКСО")
    type_standard = models.ForeignKey(DTypeStandard, on_delete=models.DO_NOTHING, db_column="d_type_standard_id", verbose_name="Стандарт")
    generation = models.ForeignKey(DGeneration, on_delete=models.DO_NOTHING, db_column="d_generation_id", verbose_name="Стандарт")
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True, verbose_name="Активно", default=False)
    number = models.IntegerField(verbose_name="Номер")
    approval_date = models.DateField(verbose_name="Дата утверждения")
    modification_date = models.DateField(verbose_name="Дата изменения")
    active_from = models.DateField(verbose_name="Вступает в силу с")

    compulsory_disciplines = models.ManyToManyField(SprCompulsoryDiscipline, verbose_name='Обязательные дисциплины')
    competencies = models.ManyToManyField(SprCompetency, verbose_name='Компетенции')
    specialozations = models.ManyToManyField("SprSpecialization", blank=True, verbose_name='Специализации')

    class Meta:
        verbose_name = verbose_name_plural = "ФГОС ВО"


class SprFormEducation(models.Model):
    id_form = models.AutoField(primary_key=True)
    form = models.CharField(max_length=255)


class SprNameOp(models.Model):
    id_spec = models.AutoField(primary_key=True)
    program_code = models.ForeignKey('SprOkco', models.DO_NOTHING, db_column='program_code')
    num_profile = models.CharField(max_length=255)
    name_spec = models.CharField(max_length=255)


class SprOkco(models.Model):
    program_code = models.CharField(primary_key=True, max_length=255)
    name_okco = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.program_code}] {self.name_okco}"


class SprRop(models.Model):
    id_rop = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)


class TblAup(models.Model):
    id_aup = models.AutoField(primary_key=True)
    file = models.CharField(max_length=255)
    num_aup = models.CharField(max_length=255)
    base = models.CharField(max_length=255)
    id_faculty = models.ForeignKey(SprFaculty, models.DO_NOTHING, db_column='id_faculty')
    id_rop = models.ForeignKey(SprRop, models.DO_NOTHING, db_column='id_rop')
    type_educ = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    type_standard = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    period_educ = models.CharField(max_length=255)
    id_degree = models.ForeignKey(SprDegreeEducation, models.DO_NOTHING, db_column='id_degree')
    id_form = models.ForeignKey(SprFormEducation, models.DO_NOTHING, db_column='id_form')
    years = models.IntegerField()
    months = models.IntegerField(blank=True, null=True)
    id_spec = models.ForeignKey(SprNameOp, models.DO_NOTHING, db_column='id_spec')
    year_beg = models.IntegerField()
    year_end = models.IntegerField()
    is_actual = models.IntegerField()
    zet = models.IntegerField()
    effective_date = models.DateField(blank=True, null=True)


class SprSpecialization(models.Model):
    d_specialozation_type = models.ForeignKey(DSpecialozationType, models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"[{self.d_specialozation_type.title}] {self.title}"

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class SprStandardZet(models.Model):
    id_standard = models.AutoField(primary_key=True)
    type_standard = models.CharField(max_length=255)


class SprVolumeDegreeZet(models.Model):
    id_volume_deg = models.AutoField(primary_key=True)
    program_code = models.ForeignKey(SprOkco, models.DO_NOTHING, db_column='program_code')
    id_standard = models.IntegerField()

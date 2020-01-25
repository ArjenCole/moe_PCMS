from django.db import models

# Create your models here.


class Roles(models.Model):
    """角色"""
    Name = models.CharField(max_length=40)
    Abbreviation = models.CharField(max_length=40)
    Parent = models.CharField(max_length=40, null=True)
    Remark = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return self.Name


class Project_Info(models.Model):
    """项目"""
    Name = models.CharField(max_length=254)
    Location = models.CharField(max_length=50)
    Client = models.CharField(max_length=50)
    Manager = models.CharField(max_length=50)
    ChiefEngineer = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.Name


class User_Info(models.Model):
    """用户"""
    Account = models.EmailField()
    Password = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    RoleID = models.ForeignKey(Roles)
    Project = models.ManyToManyField(Project_Info)
    Email = models.EmailField()
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.Account


class Investment_Estimate_Info(models.Model):
    """估算"""
    Name = models.CharField(max_length=50)
    PriceDate = models.DateField(null=True)
    QuotaName = models.CharField(max_length=50)
    CreateDate = models.DateField(null=True)
    EditDate = models.DateField(null=True)
    ProjectID = models.ForeignKey(Project_Info)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.Name


class Investment_Estimate_Element(models.Model):
    """估算项"""
    ConstructionCost = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    InstallationCost = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    EquipmentCost = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    SumCost = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    Quantities = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    Unit = models.CharField(max_length=50)
    InvestmentEstimateId = models.ForeignKey(Investment_Estimate_Info)
    ParentId = models.IntegerField(null=True)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.SumCost


class Tender_Offer_Info(models.Model):
    """投标报价"""
    Name = models.CharField(max_length=50)
    ListVersion = models.CharField(max_length=50)
    BidSection = models.CharField(max_length=50)
    CreateDate = models.DateField(null=True)
    EditDate = models.DateField(null=True)
    ProjectID = models.ForeignKey(Project_Info)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.Name


class Tender_Offer_Element(models.Model):
    """投标报价项"""
    ListID = models.CharField(max_length=50)
    Unit = models.CharField(max_length=50)
    Quantities = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    Price = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    TendOfferId = models.ForeignKey(Tender_Offer_Info)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.ListID


class Monthly_Report_Info(models.Model):
    """月报信息表"""
    Name = models.CharField(max_length=50)
    CreateDate = models.DateField(null=True)
    EditDate = models.DateField(null=True)
    Operator = models.ForeignKey(User_Info)
    ProjectID = models.ForeignKey(Project_Info)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.Name


class Monthly_Report_Element(models.Model):
    """月报项信息表"""
    Name = models.CharField(max_length=50)
    ListVersion = models.CharField(max_length=50)
    ListID = models.CharField(max_length=50)
    Unit = models.CharField(max_length=50)
    Quantities = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    Price = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    ContractQuantities = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    ContractPrice = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    MonthlyReportId = models.ForeignKey(Monthly_Report_Info)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.Name


class Technical_Economic_Indicators(models.Model):
    """技术经济指标表"""
    Name = models.CharField(max_length=50)
    Scale = models.CharField(max_length=50)
    Unit = models.CharField(max_length=50)
    InvestmentEstimate = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    DesignEstimate = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    BudgetElement = models.DecimalField(max_digits=19, decimal_places=4, default=0.00)
    ProjectId = models.ForeignKey(Project_Info)
    Remark = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.Name


class Departments(models.Model):
    """部门"""
    Name = models.CharField(max_length=40)
    Abbreviation = models.CharField(max_length=40)
    Parent = models.CharField(max_length=40, null=True)
    Remark = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return self.Name


class Premsisons(models.Model):
    """权限"""
    Name = models.CharField(max_length=40)
    Abbreviation = models.CharField(max_length=40)
    Parent = models.CharField(max_length=40, null=True)
    Remark = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return self.Name

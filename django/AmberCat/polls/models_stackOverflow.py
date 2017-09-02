from django.db import models

class Person(models.Model):
    name     = models.CharField(max_length = 50)
    birthday = models.DateField()

    def __unicode__(self):
        return u'%s' % (self.name)

class Address(models.Model):
    person  = models.ForeignKey(Person)
    address = models.CharField(max_length = 150)

    def __unicode__(self):
        return u'%s' % (self.address)

class Anniversy(models.Model):
    person    = models.ForeignKey(Person)
    anniversy = models.DateField()

    def __unicode__(self):
        return u'%s' % (self.anniversy)



class Person(models.Model):
    name        = models.CharField(max_length = 50)
    birthday    = models.DateField()
    anniversary = models.ForeignKey(Anniversary)
    address     = models.ForeignKey(Address)

class Address(models.Model):
    line1      = models.CharField(max_length = 150)
    line2      = models.CharField(max_length = 150)
    postalcode = models.CharField(max_length =  10)
    city       = models.CharField(max_length = 150)
    country    = models.CharField(max_length = 150)

class Anniversary(models.Model):
    date = models.DateField()
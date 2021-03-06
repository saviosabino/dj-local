from django.db import models
from django.contrib.auth.models import User

class Local(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=80)
    coordinates = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User)

class Comment(models.Model):
    def __unicode__(self):
        return self.comment
    local = models.ForeignKey(Local)
    by = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField()

def sendmail(**kwargs):
    #print('sendmail called')
    try:
        local = kwargs['instance']
    except KeyError: return

    if local.user.email:
        data = (local.name, local.cord, local.addr)
#        local.user.email_user(
        print(
            "New Local: %s" % data[0],
            "Local: %s, coord: %s, addr: %s" % data,
            local.user.email)

models.signals.post_save.connect(sendmail,
    sender = Local,
    dispatch_uid = 'core.models.Local')


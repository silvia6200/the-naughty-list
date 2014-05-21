# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Voice'
        db.create_table(u'naughtylist_voice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.TextField')()),
            ('datetime_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('offender', self.gf('django.db.models.fields.TextField')()),
            ('reason', self.gf('django.db.models.fields.TextField')()),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('naughty', self.gf('django.db.models.fields.BooleanField')()),
            ('fuzzy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'naughtylist', ['Voice'])


    def backwards(self, orm):
        # Deleting model 'Voice'
        db.delete_table(u'naughtylist_voice')


    models = {
        u'naughtylist.voice': {
            'Meta': {'object_name': 'Voice'},
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fuzzy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'naughty': ('django.db.models.fields.BooleanField', [], {}),
            'offender': ('django.db.models.fields.TextField', [], {}),
            'reason': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.TextField', [], {}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['naughtylist']
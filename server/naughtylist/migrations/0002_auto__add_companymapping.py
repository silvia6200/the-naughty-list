# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompanyMapping'
        db.create_table(u'naughtylist_companymapping', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('current_name', self.gf('django.db.models.fields.TextField')()),
            ('correct_name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'naughtylist', ['CompanyMapping'])


    def backwards(self, orm):
        # Deleting model 'CompanyMapping'
        db.delete_table(u'naughtylist_companymapping')


    models = {
        u'naughtylist.companymapping': {
            'Meta': {'object_name': 'CompanyMapping'},
            'correct_name': ('django.db.models.fields.TextField', [], {}),
            'current_name': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
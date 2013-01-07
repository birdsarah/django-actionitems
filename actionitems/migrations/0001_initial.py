# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActionItem'
        db.create_table('actionitems_actionitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('responsible', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('deadline', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('completed_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 7, 0, 0))),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('manager', self.gf('django.db.models.fields.CharField')(default='internal', max_length=10)),
        ))
        db.send_create_signal('actionitems', ['ActionItem'])


    def backwards(self, orm):
        # Deleting model 'ActionItem'
        db.delete_table('actionitems_actionitem')


    models = {
        'actionitems.actionitem': {
            'Meta': {'object_name': 'ActionItem'},
            'completed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 7, 0, 0)'}),
            'deadline': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.CharField', [], {'default': "'internal'", 'max_length': '10'}),
            'responsible': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['actionitems']
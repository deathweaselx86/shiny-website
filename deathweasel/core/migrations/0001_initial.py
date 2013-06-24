# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KeywordModel'
        db.create_table('core_keywordmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('core', ['KeywordModel'])


    def backwards(self, orm):
        # Deleting model 'KeywordModel'
        db.delete_table('core_keywordmodel')


    models = {
        'core.keywordmodel': {
            'Meta': {'object_name': 'KeywordModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']
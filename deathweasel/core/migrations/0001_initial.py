<<<<<<< HEAD
# -*- coding: utf-8 -*-
=======
# encoding: utf-8
>>>>>>> comments
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

<<<<<<< HEAD

class Migration(SchemaMigration):

    def forwards(self, orm):
=======
class Migration(SchemaMigration):

    def forwards(self, orm):
        
>>>>>>> comments
        # Adding model 'KeywordModel'
        db.create_table('core_keywordmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('core', ['KeywordModel'])


    def backwards(self, orm):
<<<<<<< HEAD
=======
        
>>>>>>> comments
        # Deleting model 'KeywordModel'
        db.delete_table('core_keywordmodel')


    models = {
        'core.keywordmodel': {
            'Meta': {'object_name': 'KeywordModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

<<<<<<< HEAD
    complete_apps = ['core']
=======
    complete_apps = ['core']
>>>>>>> comments
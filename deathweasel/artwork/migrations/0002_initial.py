# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ArtworkModel'
        db.create_table('artwork_artworkmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('medium', self.gf('django.db.models.fields.CharField')(default='graphite', max_length=200)),
            ('upload_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal('artwork', ['ArtworkModel'])

        # Adding M2M table for field keywords on 'ArtworkModel'
        db.create_table('artwork_artworkmodel_keywords', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('artworkmodel', models.ForeignKey(orm['artwork.artworkmodel'], null=False)),
            ('keywordmodel', models.ForeignKey(orm['artwork.keywordmodel'], null=False))
        ))
        db.create_unique('artwork_artworkmodel_keywords', ['artworkmodel_id', 'keywordmodel_id'])

        # Adding model 'CommentModel'
        db.create_table('artwork_commentmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['artwork.CommentModel'], unique=True, null=True)),
            ('artwork', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['artwork.ArtworkModel'])),
        ))
        db.send_create_signal('artwork', ['CommentModel'])

        # Adding model 'KeywordModel'
        db.create_table('artwork_keywordmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keyword', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('artwork', ['KeywordModel'])


    def backwards(self, orm):
        
        # Deleting model 'ArtworkModel'
        db.delete_table('artwork_artworkmodel')

        # Removing M2M table for field keywords on 'ArtworkModel'
        db.delete_table('artwork_artworkmodel_keywords')

        # Deleting model 'CommentModel'
        db.delete_table('artwork_commentmodel')

        # Deleting model 'KeywordModel'
        db.delete_table('artwork_keywordmodel')


    models = {
        'artwork.artworkmodel': {
            'Meta': {'ordering': "['title']", 'object_name': 'ArtworkModel'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'desc': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['artwork.KeywordModel']", 'symmetrical': 'False'}),
            'medium': ('django.db.models.fields.CharField', [], {'default': "'graphite'", 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'artwork.commentmodel': {
            'Meta': {'ordering': "['-date']", 'object_name': 'CommentModel'},
            'artwork': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['artwork.ArtworkModel']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['artwork.CommentModel']", 'unique': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'artwork.keywordmodel': {
            'Meta': {'object_name': 'KeywordModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyword': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 23, 15, 23, 10, 237753, tzinfo=<UTC>)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 5, 23, 15, 23, 10, 237074, tzinfo=<UTC>)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['artwork']

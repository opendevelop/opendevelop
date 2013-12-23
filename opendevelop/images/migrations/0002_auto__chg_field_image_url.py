# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Image.url'
        db.alter_column(u'images_image', 'url', self.gf('django.db.models.fields.URLField')(max_length=64, null=True))

    def backwards(self, orm):

        # Changing field 'Image.url'
        db.alter_column(u'images_image', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=64))

    models = {
        u'images.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'docker_image_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '32'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '64', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['images']
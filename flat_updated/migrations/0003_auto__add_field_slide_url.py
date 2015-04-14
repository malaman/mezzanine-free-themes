# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Slide.url'
        db.add_column('theme_slide', 'url',
                      self.gf('django.db.models.fields.CharField')(default='#', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Slide.url'
        db.delete_column('theme_slide', 'url')


    models = {
        'pages.page': {
            'Meta': {'object_name': 'Page', 'ordering': "('titles',)"},
            '_meta_title': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '500'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'null': 'True', 'blank': 'True', 'default': '(1, 2, 3)', 'max_length': '100'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '500'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['pages.Page']", 'related_name': "'children'"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '2000'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1000'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'", 'object_name': 'Site', 'ordering': "('domain',)"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'theme.homepage': {
            'Meta': {'_ormbases': ['pages.Page'], 'object_name': 'HomePage', 'ordering': "('_order',)"},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['pages.Page']", 'unique': 'True'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'theme.slide': {
            'Meta': {'object_name': 'Slide', 'ordering': "('_order',)"},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['theme.HomePage']", 'related_name': "'slides'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'null': 'True', 'blank': 'True', 'max_length': '255'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'#'", 'max_length': '200'})
        }
    }

    complete_apps = ['theme']
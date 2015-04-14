# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table('theme_slide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theme.HomePage'], related_name='slides')),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, blank=True, null=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subheading', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('theme', ['Slide'])

        # Adding model 'HomePage'
        db.create_table('theme_homepage', (
            ('page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['pages.Page'], unique=True)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subheading', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('theme', ['HomePage'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table('theme_slide')

        # Deleting model 'HomePage'
        db.delete_table('theme_homepage')


    models = {
        'pages.page': {
            'Meta': {'object_name': 'Page', 'ordering': "('titles',)"},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True', 'null': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'max_length': '100', 'default': '(1, 2, 3)', 'blank': 'True', 'null': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pages.Page']", 'related_name': "'children'", 'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True', 'null': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True', 'null': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'ordering': "('domain',)", 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'theme.homepage': {
            'Meta': {'object_name': 'HomePage', 'ordering': "('_order',)", '_ormbases': ['pages.Page']},
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
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['theme']
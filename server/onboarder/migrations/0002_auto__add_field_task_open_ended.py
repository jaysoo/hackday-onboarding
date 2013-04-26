# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Task.open_ended'
        db.add_column(u'onboarder_task', 'open_ended',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Task.open_ended'
        db.delete_column(u'onboarder_task', 'open_ended')


    models = {
        u'onboarder.badge': {
            'Meta': {'object_name': 'Badge'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'onboarder.choice': {
            'Meta': {'object_name': 'Choice'},
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'choices'", 'null': 'True', 'to': u"orm['onboarder.Task']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'onboarder.newrecruit': {
            'Meta': {'object_name': 'NewRecruit'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'to': u"orm['onboarder.Profile']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'onboarder.profile': {
            'Meta': {'object_name': 'Profile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tasks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'profiles'", 'blank': 'True', 'to': u"orm['onboarder.Task']"})
        },
        u'onboarder.randomfact': {
            'Meta': {'object_name': 'RandomFact'},
            'fact': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'picture': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'onboarder.task': {
            'Meta': {'ordering': "['number']", 'object_name': 'Task'},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tasks'", 'null': 'True', 'to': u"orm['onboarder.Badge']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'open_ended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pre_step': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'onboarder.taskstatus': {
            'Meta': {'object_name': 'TaskStatus'},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recruit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'responses'", 'to': u"orm['onboarder.NewRecruit']"}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'null': 'True', 'to': u"orm['onboarder.Task']"})
        }
    }

    complete_apps = ['onboarder']
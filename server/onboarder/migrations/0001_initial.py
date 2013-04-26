# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Badge'
        db.create_table(u'onboarder_badge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'onboarder', ['Badge'])

        # Adding model 'Task'
        db.create_table(u'onboarder_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('pre_step', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('badge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', null=True, to=orm['onboarder.Badge'])),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'onboarder', ['Task'])

        # Adding model 'Profile'
        db.create_table(u'onboarder_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'onboarder', ['Profile'])

        # Adding M2M table for field tasks on 'Profile'
        db.create_table(u'onboarder_profile_tasks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm[u'onboarder.profile'], null=False)),
            ('task', models.ForeignKey(orm[u'onboarder.task'], null=False))
        ))
        db.create_unique(u'onboarder_profile_tasks', ['profile_id', 'task_id'])

        # Adding model 'NewRecruit'
        db.create_table(u'onboarder_newrecruit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('job_title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(related_name='members', to=orm['onboarder.Profile'])),
        ))
        db.send_create_signal(u'onboarder', ['NewRecruit'])

        # Adding model 'Choice'
        db.create_table(u'onboarder_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='choices', null=True, to=orm['onboarder.Task'])),
        ))
        db.send_create_signal(u'onboarder', ['Choice'])

        # Adding model 'TaskStatus'
        db.create_table(u'onboarder_taskstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks', null=True, to=orm['onboarder.Task'])),
            ('recruit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='responses', to=orm['onboarder.NewRecruit'])),
            ('complete', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'onboarder', ['TaskStatus'])

        # Adding model 'RandomFact'
        db.create_table(u'onboarder_randomfact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fact', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('picture', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'onboarder', ['RandomFact'])


    def backwards(self, orm):
        # Deleting model 'Badge'
        db.delete_table(u'onboarder_badge')

        # Deleting model 'Task'
        db.delete_table(u'onboarder_task')

        # Deleting model 'Profile'
        db.delete_table(u'onboarder_profile')

        # Removing M2M table for field tasks on 'Profile'
        db.delete_table('onboarder_profile_tasks')

        # Deleting model 'NewRecruit'
        db.delete_table(u'onboarder_newrecruit')

        # Deleting model 'Choice'
        db.delete_table(u'onboarder_choice')

        # Deleting model 'TaskStatus'
        db.delete_table(u'onboarder_taskstatus')

        # Deleting model 'RandomFact'
        db.delete_table(u'onboarder_randomfact')


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
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks'", 'null': 'True', 'to': u"orm['onboarder.Badge']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
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
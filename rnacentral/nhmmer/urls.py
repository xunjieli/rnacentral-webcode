"""
Copyright [2009-2014] EMBL-European Bioinformatics Institute
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
     http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
import views

# exporting metadata search results
urlpatterns = patterns('',
    # export search results
    url(r'^submit-query/?$',
        'nhmmer.views.submit_job',
        name='nhmmer-submit-job'),

    # get nhmmer search job status
    url(r'^job-status/?$',
        'nhmmer.views.get_status',
        name='nhmmer-job-status'),

    # get nhmmer results
    url(r'^get-results/?$',
        views.ResultsView.as_view(),
        name='nhmmer-job-results'),

    # user interface
    url(r'^$', TemplateView.as_view(template_name='nhmmer/sequence-search.html'),
        name='nhmmer-sequence-search'),
)

from django.conf.urls.defaults import *

urlpatterns = patterns('quest.views',
    (r'^$', 'view_all_snippets', {'all_snippets_template':'all_snippets.html'}, 'all_snippets'),
    (r'^search/$', 'view_search_snippets', {'search_snippets_template':'search_snippets.html'}, 'search_snippets'),
    (r'^tags/$', 'view_tagcloud_snippets', {'tagcloud_snippets_template':'tagcloud_snippets.html'}, 'tagcloud_snippets'),
    (r'^recent/$', 'view_recent_snippets', {'recent_snippets_template':'recent_snippets.html'}, 'recent_snippets'),
    (r'^popular/$', 'view_popular_snippets', {'popular_snippets_template':'popular_snippets.html'}, 'popular_snippets'),
    (r'^(?P<snippet_id>\d+)/(?P<snippet_slug>[\w-]+)/$', 'view_snippet_profile', {'snippet_profile_template':'snippet_profile.html'}, 'snippet_profile'),
    (r'^add/$', 'view_add_snippet', {'add_snippet_template':'add_snippet.html', 'snippet_profile_template':'snippet_profile.html'}, 'add_snippet'),
    (r'^(?P<snippet_id>\d+)/(?P<snippet_slug>[\w-]+)/delete/$', 'view_delete_snippet', {}, 'delete_snippet'),
    (r'^(?P<snippet_id>\d+)/(?P<snippet_slug>[\w-]+)/modify/$', 'view_modify_snippet', {'modify_snippet_template':'add_snippet.html', 'snippet_profile_template':'snippet_profile.html'}, 'modify_snippet'),
    (r'^(?P<tag_name>[\w-]+)/$', 'view_tagged_snippets', {'tagged_snippets_template':'all_snippets.html'}, 'tagged_snippets'),
)
from django.conf.urls import url
from api.views import (wiki_api,assets_api,
                       deploy_api,cron_api,
                       logs_api,ansible_api,
                       db_api,users_api,
                       orders_api)
urlpatterns = [
            url(r'assets/$', assets_api.asset_list), 
            url(r'assets/(?P<id>[0-9]+)/$', assets_api.asset_detail),
            url(r'service/$', assets_api.service_list), 
            url(r'service/(?P<id>[0-9]+)/$', assets_api.service_detail), 
            url(r'project/$', assets_api.project_list), 
            url(r'project/(?P<id>[0-9]+)/$', assets_api.project_detail),     
            url(r'group/$', assets_api.group_list), 
            url(r'group/(?P<id>[0-9]+)/$',assets_api.group_detail), 
            url(r'user/$', users_api.user_list), 
            url(r'user/(?P<id>[0-9]+)/$',users_api.user_detail), 
            url(r'zone/$', assets_api.zone_list), 
            url(r'zone/(?P<id>[0-9]+)/$',assets_api.zone_detail), 
            url(r'line/$', assets_api.line_list), 
            url(r'line/(?P<id>[0-9]+)/$',assets_api.line_detail),     
            url(r'raid/$', assets_api.raid_list), 
            url(r'raid/(?P<id>[0-9]+)/$',assets_api.raid_detail),     
            url(r'server/$', assets_api.asset_server_list), 
            url(r'server/(?P<id>[0-9]+)/$', assets_api.asset_server_detail), 
            url(r'net/$', assets_api.asset_net_list), 
            url(r'net/(?P<id>[0-9]+)/$', assets_api.asset_net_detail),  
            url(r'cron/$', cron_api.cron_list),  
            url(r'cron/(?P<id>[0-9]+)/$', cron_api.cron_detail),  
            url(r'deploy/$', deploy_api.deploy_list),  
            url(r'deploy/(?P<id>[0-9]+)/$', deploy_api.deploy_detail),    
            url(r'playbook/$', ansible_api.playbook_list),  
            url(r'playbook/(?P<id>[0-9]+)/$', ansible_api.playbook_detail),
#             url(r'order/(?P<username>.+)/$', deploy_api.OrderList.as_view()),
            url(r'logs/assets/(?P<id>[0-9]+)/$', assets_api.assetsLog_detail),
            url(r'logs/cron/(?P<id>[0-9]+)/$', cron_api.cronLogsdetail),
            url(r'logs/ansible/model/(?P<id>[0-9]+)/$', ansible_api.modelLogsdetail),
            url(r'logs/ansible/playbook/(?P<id>[0-9]+)/$', ansible_api.playbookLogsdetail),
            url(r'logs/deploy/(?P<id>[0-9]+)/$', deploy_api.deployLogs_detail),
            url(r'logs/search/model/$', logs_api.AnsibleModelLogsList),
            url(r'logs/search/playbook/$', logs_api.AnsiblePlayBookLogsList),
            url(r'logs/sql/(?P<id>[0-9]+)/$', db_api.sql_exec_logs),
            url(r'inc/config/$', db_api.inc_list),
            url(r'inc/config/(?P<id>[0-9]+)/$', db_api.inc_detail),
            url(r'db/config/$', db_api.db_list),
            url(r'db/config/(?P<id>[0-9]+)/$', db_api.db_detail),
            url(r'orders/(?P<id>[0-9]+)/$', orders_api.order_detail),
            url(r'sql/custom/$', db_api.sql_custom_list),
            url(r'sql/custom/(?P<id>[0-9]+)/$', db_api.sql_custom_detail),  
            url(r'wiki/tag/$', wiki_api.tag_list),
            url(r'wiki/tag/(?P<id>[0-9]+)/$', wiki_api.tag_detail),
            url(r'wiki/category/$', wiki_api.category_list),
            url(r'wiki/category/(?P<id>[0-9]+)/$', wiki_api.category_detail),   
            url(r'wiki/archive/(?P<id>[0-9]+)/$', wiki_api.archive_detail),                     
    ]    
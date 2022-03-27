from django.urls import path
from .views import AdFiltered, AdList, AdDetail, AdCreate, AdEdit, AdDelete,\
    ReplyCreate, ReplyDelete, ReplyConfirmApprove, ReplyList, approve_reply,\
    NewsList, NewsDetail, NewsCreate, NewsEdit, NewsDelete, news_subscribe,\
    news_unsubscribe, NewsMailingConfirm, news_mailing_confirm

urlpatterns = [
    path('ad', AdList.as_view(), name='ad_list_view'),
    path('ad/<int:pk>', AdDetail.as_view(), name='ad_detail_view'),
    path('ad/create', AdCreate.as_view(), name='ad_create_view'),
    path('ad/<int:pk>/edit', AdEdit.as_view(), name='ad_edit_view'),
    path('ad/<int:pk>/delete', AdDelete.as_view(), name='ad_delete_view'),
    path('ad/filtered', AdFiltered.as_view(), name='ad_filtered_view'),
    path('reply', ReplyList.as_view(), name='reply_list_view'),
    path('reply/<int:ad_id>/create', ReplyCreate.as_view(),
         name='reply_create_view'),
    path('reply/<int:pk>/delete', ReplyDelete.as_view(),
         name='reply_delete_view'),
    path('reply/<int:pk>/approve', ReplyConfirmApprove.as_view(),
         name='reply_approve_view'),
    path('reply/<int:pk>/approve_confirm', approve_reply,
         name='reply_approve_button'),
    path('news', NewsList.as_view(), name='news_list_view'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail_view'),
    path('news/create', NewsCreate.as_view(), name='news_create_view'),
    path('news/<int:pk>/edit', NewsEdit.as_view(), name='news_edit_view'),
    path('news/<int:pk>/delete', NewsDelete.as_view(),
         name='news_delete_view'),
    path('news/subscribe', news_subscribe, name='news_subscribe_button'),
    path('news/unsubscribe', news_unsubscribe, name='news_unsubscribe_button'),
    path('news/<int:pk>/mailing', NewsMailingConfirm.as_view(),
         name='news_confirm_mailing_view'),
    path('news/<int:pk>/mailing_confirm', news_mailing_confirm,
         name='news_confirm_mailing_button'),
]

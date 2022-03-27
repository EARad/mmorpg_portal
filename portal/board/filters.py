from django_filters import FilterSet
from django_filters.filters import CharFilter, DateTimeFilter,\
    ModelChoiceFilter, OrderingFilter
from .models import Ad, Category


class AdFilter(FilterSet):
    # category_list = [(rec['id'], rec['name']) for rec in
    #                  Category.objects.all().values()]

    creation_time = DateTimeFilter(label='Дата создания после',
                                   field_name='creation_time',
                                   lookup_expr='gt')
    category_id = ModelChoiceFilter(field_name='category_id',
                                    label='Категория',
                                    # choices=category_list,
                                    lookup_expr='exact',
                                    queryset=Category.objects.all())
    header = CharFilter(label='Заголовок содержит',
                        field_name='header',
                        lookup_expr='icontains')
    ad = CharFilter(label='Объявление содержит',
                    field_name='ad',
                    lookup_expr='icontains')
    o = OrderingFilter(
        label='Сортировка по',
        # tuple-mapping retains order
        fields=(
            ('creation_time', 'creation_time'),
            ('category_id__name', 'category_id'),
            ('header', 'header'),
            ('ad', 'ad'),
        ),

        # labels do not need to retain order
        field_labels={
            'creation_time': 'времени создания',
            'category_id__name': 'категории',
            'header': 'заголовку',
            'ad': 'объявлению',
        }
    )

    class Meta:
        model = Ad
        fields = ['creation_time', 'category_id', 'header', 'ad']

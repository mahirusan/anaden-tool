from django import template

register = template.Library() #Djangoのテンプレートタグライブラリ

# カスタムフィルタとして登録する
@register.filter
def sort_task(queryset,order):
    return queryset.order_by(order)
    
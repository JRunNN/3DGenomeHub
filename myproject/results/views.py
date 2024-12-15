from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from results import models
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method='get',
    operation_description="获取示例数据列表",
    responses={200: "成功返回数据"}
)
@api_view(['GET'])
def get_samples(request):
    # 获取所有数据
    all_samples = models.Samples.objects.all()[:100]  # 限制最大返回记录

    # 分页设置
    page = request.GET.get('page', 1)  # 获取当前页码，默认为第 1 页
    per_page = 10  # 每页显示的数据条数

    paginator = Paginator(all_samples, per_page)

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页数据
        page = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页数据
        page = paginator.page(paginator.num_pages)

    # 构造 JSON 数据
    data = {
        "samples": [
            {
                "id": sample.id,
                "name": sample.name,
                "description": sample.description,
            }
            for sample in page
        ],
        "pagination": {
            "current_page": page.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_previous": page.has_previous(),
            "has_next": page.has_next(),
        },
    }

    return JsonResponse(data)

from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from results import models
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 定义查询参数
id_param = openapi.Parameter(
    name='id',  # 参数名称
    in_=openapi.IN_QUERY,  # 参数位置：查询参数
    description="根据样本 ID 进行精确过滤，例如：1",  # 参数意义
    type=openapi.TYPE_INTEGER  # 参数类型：整数
)
sample_name_param = openapi.Parameter(
    name='sample_name',
    in_=openapi.IN_QUERY,
    description="根据样本名称进行搜索，例如：'GSM4072742'（不区分大小写）",
    type=openapi.TYPE_STRING  # 参数类型：字符串
)
page_param = openapi.Parameter(
    name='page',
    in_=openapi.IN_QUERY,
    description="分页页码，默认为 1，用于获取第几页的数据，例如：2",
    type=openapi.TYPE_INTEGER,  # 参数类型：整数
    default=1  # 默认值
)

@swagger_auto_schema(
    method='get',
    operation_description="根据条件（如 ID 或名称）获取示例数据列表，支持分页",
    manual_parameters=[id_param, sample_name_param, page_param]
)
@api_view(['GET'])
def get_samples(request):
    # 获取查询参数
    sample_id = request.GET.get('id')
    sample_name = request.GET.get('sample_name')

    # 查询条件过滤
    all_samples = models.Samples.objects.all()
    if sample_id:
        all_samples = all_samples.filter(id=sample_id)
    if sample_name:
        all_samples = all_samples.filter(sample=sample_name)

    # 限制最大返回记录
    all_samples = all_samples[:100]

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
                "sample": sample.sample,
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

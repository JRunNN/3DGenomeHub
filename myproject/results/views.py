from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from results import models
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from results.models import Enhancer, Loop, Stripe, Compartment, DomainBound, Overview

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
    all_samples = all_samples[:1000]

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

    return JsonResponse({"data": data})


# 定义 Swagger 参数
chrom_param = openapi.Parameter(
    name='chrom',
    in_=openapi.IN_QUERY,
    description="染色体名称，例如：chr1",
    type=openapi.TYPE_STRING,
    required=True
)
start_param = openapi.Parameter(
    name='start',
    in_=openapi.IN_QUERY,
    description="区间的起始位置，例如：10000",
    type=openapi.TYPE_INTEGER,
    required=True
)
end_param = openapi.Parameter(
    name='end',
    in_=openapi.IN_QUERY,
    description="区间的结束位置，例如：20000",
    type=openapi.TYPE_INTEGER,
    required=True
)


@swagger_auto_schema(
    method='get',
    operation_description="根据 chrom、start 和 end 参数查询有重叠的 enhancer 数据",
    manual_parameters=[chrom_param, start_param, end_param],
    responses={200: "成功返回数据"}
)
@api_view(['GET'])
def get_enhancers(request):
    # 获取输入参数
    chrom = request.GET.get('chrom')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # 校验参数
    if not chrom or not start or not end:
        return JsonResponse({"error": "缺少必要的参数 chrom, start 或 end"}, status=400)

    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return JsonResponse({"error": "start 和 end 必须是整数"}, status=400)

    if start > end:
        return JsonResponse({"error": "start 不能大于 end"}, status=400)

    # 查询满足条件的数据
    all_enhancers = Enhancer.objects.filter(
        chrom=chrom,  # 确保 chrom 相等
        start__lte=end,  # start <= 参数的 end
        end__gte=start  # end >= 参数的 start
    )

    # 限制最大返回记录
    enhancers = all_enhancers[:1000]

    # 分页设置
    page = request.GET.get('page', 1)  # 获取当前页码，默认为第 1 页
    per_page = 10  # 每页显示的数据条数

    paginator = Paginator(enhancers, per_page)

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页数据
        page = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页数据
        page = paginator.page(paginator.num_pages)

    # 构造 JSON 返回数据
    data = {
        "enhancers": [
            {
                "id": enhancer.id,
                "chrom": enhancer.chrom,
                "start": enhancer.start,
                "end": enhancer.end,
                "log_pvalue": enhancer.log_pvalue,
                "file_id": enhancer.file_id,
                "experiment": enhancer.experiment,
                "subtissue": enhancer.subtissue,
                "tissue": enhancer.tissue
            }
            for enhancer in enhancers
        ],
        "pagination": {
            "current_page": page.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_previous": page.has_previous(),
            "has_next": page.has_next(),
        },
    }

    return JsonResponse({"data": data})


# 定义 Swagger 查询参数
chrom_param = openapi.Parameter(
    name='chrom',
    in_=openapi.IN_QUERY,
    description="染色体名称，例如：chr1",
    type=openapi.TYPE_STRING,
    required=True
)
start_param = openapi.Parameter(
    name='start',
    in_=openapi.IN_QUERY,
    description="区间的起始位置，例如：10000",
    type=openapi.TYPE_INTEGER,
    required=True
)
end_param = openapi.Parameter(
    name='end',
    in_=openapi.IN_QUERY,
    description="区间的结束位置，例如：20000",
    type=openapi.TYPE_INTEGER,
    required=True
)


@swagger_auto_schema(
    method='get',
    operation_description="输入 chrom 和区间 [start, end]，查询 Loop 表中任意 chrom1 或 chrom2 上有重叠区间的数据",
    manual_parameters=[chrom_param, start_param, end_param],
    responses={200: "成功返回数据"}
)
@api_view(['GET'])
def get_loops(request):
    # 获取输入参数
    chrom = request.GET.get('chrom')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # 参数校验
    if not chrom or not start or not end:
        return JsonResponse({"error": "缺少必要的参数 chrom, start 或 end"}, status=400)
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return JsonResponse({"error": "start 和 end 必须是整数"}, status=400)
    if start > end:
        return JsonResponse({"error": "start 不能大于 end"}, status=400)

    # 查询满足条件的数据
    all_loops = Loop.objects.filter(
        # 条件1：chrom1 重叠
        Q(chrom1=chrom, start1__lte=end, end1__gte=start) |
        # 条件2：chrom2 重叠
        Q(chrom2=chrom, start2__lte=end, end2__gte=start)
    )

    # 限制最大返回记录
    loops = all_loops[:1000]

    # 分页设置
    page = request.GET.get('page', 1)  # 获取当前页码，默认为第 1 页
    per_page = 10  # 每页显示的数据条数

    paginator = Paginator(loops, per_page)

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页数据
        page = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页数据
        page = paginator.page(paginator.num_pages)

    # 构建返回数据
    data = {
        "loops": [
            {
                "id": loop.id,
                "sample_name": loop.sample_name.sample,  # 外键字段显示 sample 名称
                "chrom1": loop.chrom1,
                "start1": loop.start1,
                "end1": loop.end1,
                "chrom2": loop.chrom2,
                "start2": loop.start2,
                "end2": loop.end2,
                "counts": loop.counts,
                "gene_anno_1": loop.gene_anno_1,
                "gene_anno_2": loop.gene_anno_2,
            }
            for loop in loops
        ],
        "pagination": {
            "current_page": page.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_previous": page.has_previous(),
            "has_next": page.has_next(),
        },
    }

    return JsonResponse({"loops": data}, safe=False)


# 定义 Swagger 查询参数
chrom_param = openapi.Parameter(
    name='chrom',
    in_=openapi.IN_QUERY,
    description="染色体名称，例如：chr1",
    type=openapi.TYPE_STRING,
    required=True
)
start_param = openapi.Parameter(
    name='start',
    in_=openapi.IN_QUERY,
    description="区间的起始位置，例如：10000",
    type=openapi.TYPE_INTEGER,
    required=True
)
end_param = openapi.Parameter(
    name='end',
    in_=openapi.IN_QUERY,
    description="区间的结束位置，例如：20000",
    type=openapi.TYPE_INTEGER,
    required=True
)


@swagger_auto_schema(
    method='get',
    operation_description="输入 chrom 和区间 [start, end]，查询 Stripe 表中任意 chrom1 或 chrom2 上有重叠区间的数据",
    manual_parameters=[chrom_param, start_param, end_param],
    responses={200: "成功返回数据"}
)
@api_view(['GET'])
def get_stripes(request):
    # 获取输入参数
    chrom = request.GET.get('chrom')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # 参数校验
    if not chrom or not start or not end:
        return JsonResponse({"error": "缺少必要的参数 chrom, start 或 end"}, status=400)
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return JsonResponse({"error": "start 和 end 必须是整数"}, status=400)
    if start > end:
        return JsonResponse({"error": "start 不能大于 end"}, status=400)

    # 查询满足条件的数据
    all_stripes = Stripe.objects.filter(
        # 条件1：chrom1 重叠
        Q(chrom1=chrom, pos1__lte=end, pos2__gte=start) |
        # 条件2：chrom2 重叠
        Q(chrom2=chrom, pos3__lte=end, pos4__gte=start)
    )

    stripes = all_stripes[:1000]

    # 分页设置
    page = request.GET.get('page', 1)  # 获取当前页码，默认为第 1 页
    per_page = 10  # 每页显示的数据条数

    paginator = Paginator(stripes, per_page)

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页数据
        page = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页数据
        page = paginator.page(paginator.num_pages)

    # 构建返回数据
    data = {
        "stripes": [
            {
                "id": stripe.id,
                "sample_name": stripe.sample_name.sample,  # 外键字段显示 sample 名称
                "chrom1": stripe.chrom1,
                "pos1": stripe.pos1,
                "pos2": stripe.pos2,
                "chrom2": stripe.chrom2,
                "pos3": stripe.pos3,
                "pos4": stripe.pos4,
                "pvalue": stripe.pvalue,
                "gene_anno_1": stripe.gene_anno_1,
                "gene_anno_2": stripe.gene_anno_2,
                "chipseq_anno_1": stripe.chipseq_anno_1,
                "chipseq_anno_2": stripe.chipseq_anno_2,
                "stripe_type": stripe.stripe_type
            }
            for stripe in stripes  # 假设 `stripes` 是查询结果集
        ],
        "pagination": {
            "current_page": page.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_previous": page.has_previous(),
            "has_next": page.has_next(),
        },
    }

    return JsonResponse({"stripes": data}, safe=False)


# 定义 Swagger 参数
chrom_param = openapi.Parameter(
    name='chrom',
    in_=openapi.IN_QUERY,
    description="染色体名称，例如：chr1",
    type=openapi.TYPE_STRING,
    required=True
)
start_param = openapi.Parameter(
    name='start',
    in_=openapi.IN_QUERY,
    description="区间的起始位置，例如：10000",
    type=openapi.TYPE_INTEGER,
    required=True
)
end_param = openapi.Parameter(
    name='end',
    in_=openapi.IN_QUERY,
    description="区间的结束位置，例如：20000",
    type=openapi.TYPE_INTEGER,
    required=True
)


@swagger_auto_schema(
    method='get',
    operation_description="根据 chrom、start 和 end 参数查询有重叠的 compartments 数据",
    manual_parameters=[chrom_param, start_param, end_param],
    responses={200: "成功返回数据"}
)
@api_view(['GET'])
def get_compartments(request):
    # 获取输入参数
    chrom = request.GET.get('chrom')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # 校验参数
    if not chrom or not start or not end:
        return JsonResponse({"error": "缺少必要的参数 chrom, start 或 end"}, status=400)

    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return JsonResponse({"error": "start 和 end 必须是整数"}, status=400)

    if start > end:
        return JsonResponse({"error": "start 不能大于 end"}, status=400)

    # 查询满足条件的数据
    all_compartments = Compartment.objects.filter(
        chrom=chrom,  # 确保 chrom 相等
        start__lte=end,  # start <= 参数的 end
        end__gte=start  # end >= 参数的 start
    ).order_by('chrom')

    compartments = all_compartments[:1000]

    # 分页设置
    page = request.GET.get('page', 1)  # 获取当前页码，默认为第 1 页
    per_page = 10  # 每页显示的数据条数

    paginator = Paginator(compartments, per_page)

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页数据
        page = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页数据
        page = paginator.page(paginator.num_pages)

    # 构造 JSON 返回数据
    data = {
        "compartments": [
            {
                "id": compartment.id,
                "chrom": compartment.chrom,
                "start": compartment.start,
                "end": compartment.end,
                "E1score": compartment.value,
                "sample_id": compartment.sample_name.sample,
                "tissue": compartment.sample_name.tissue,
                "health_status": compartment.sample_name.health_status
            }
            for compartment in compartments
        ],
        "pagination": {
            "page": page.number,
            "page_size": paginator.per_page,
            "total_pages": paginator.num_pages,
            "total": paginator.count,
            "has_previous": page.has_previous(),
            "has_next": page.has_next(),
        },
    }

    return JsonResponse({"data": data})

# 定义 Swagger 参数
chrom_param = openapi.Parameter(
    name='chrom',
    in_=openapi.IN_QUERY,
    description="染色体名称，例如：chr1",
    type=openapi.TYPE_STRING,
    required=True
)
start_param = openapi.Parameter(
    name='start',
    in_=openapi.IN_QUERY,
    description="区间的起始位置，例如：10000",
    type=openapi.TYPE_INTEGER,
    required=True
)
end_param = openapi.Parameter(
    name='end',
    in_=openapi.IN_QUERY,
    description="区间的结束位置，例如：20000",
    type=openapi.TYPE_INTEGER,
    required=True
)


@swagger_auto_schema(
    method='get',
    operation_description="根据 chrom、start 和 end 参数查询有重叠带有 bound 的 domains 数据",
    manual_parameters=[chrom_param, start_param, end_param],
    responses={200: "成功返回数据"}
)
@api_view(['GET'])
def get_domain_bound_samples(request):
    # 获取输入参数
    chrom = request.GET.get('chrom')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # 校验参数
    if not chrom or not start or not end:
        return JsonResponse({"error": "缺少必要的参数 chrom, start 或 end"}, status=400)

    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return JsonResponse({"error": "start 和 end 必须是整数"}, status=400)

    if start > end:
        return JsonResponse({"error": "start 不能大于 end"}, status=400)

    # 查询满足条件的数据
    all_domain_bound = DomainBound.objects.filter(
        chrom=chrom,  # 确保 chrom 相等
        start__lte=end,  # start <= 参数的 end
        end__gte=start  # end >= 参数的 start
    )

    domain_bound_samples = all_domain_bound[:1000]

    # 分页设置
    page = request.GET.get('page', 1)  # 获取当前页码，默认为第 1 页
    per_page = 10  # 每页显示的数据条数

    paginator = Paginator(domain_bound_samples, per_page)

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页数据
        page = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页数据
        page = paginator.page(paginator.num_pages)

    # 构造 JSON 返回数据
    data = {
        "domain_bound_samples": [
            {
                "id": domain_bound_sample.id,
                "chrom": domain_bound_sample.chrom,
                "start": domain_bound_sample.start,
                "end": domain_bound_sample.end,
                "sample_name": domain_bound_sample.sample_name.sample
            }
            for domain_bound_sample in domain_bound_samples
        ],
        "pagination": {
            "current_page": page.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_previous": page.has_previous(),
            "has_next": page.has_next(),
        },
    }

    return JsonResponse({"data": data})


# 定义 Swagger 参数
chrom_param = openapi.Parameter(
    name='chrom',
    in_=openapi.IN_QUERY,
    description="染色体名称，例如：chr1",
    type=openapi.TYPE_STRING,
    required=True
)
start_param = openapi.Parameter(
    name='start',
    in_=openapi.IN_QUERY,
    description="区间的起始位置，例如：10000",
    type=openapi.TYPE_INTEGER,
    required=True
)
end_param = openapi.Parameter(
    name='end',
    in_=openapi.IN_QUERY,
    description="区间的结束位置，例如：20000",
    type=openapi.TYPE_INTEGER,
    required=True
)


@swagger_auto_schema(
    method='get',
    operation_description="根据 chrom、start 和 end 参数查询有重叠带有 bound 的 overview 数据",
    manual_parameters=[chrom_param, start_param, end_param],
    responses={200: "成功返回数据"}
)
@api_view(['GET'])
def get_overview(request):
    # 获取输入参数
    chrom = request.GET.get('chrom')
    start = request.GET.get('start')
    end = request.GET.get('end')

    # 校验参数
    if not chrom or not start or not end:
        return JsonResponse({"error": "缺少必要的参数 chrom, start 或 end"}, status=400)

    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return JsonResponse({"error": "start 和 end 必须是整数"}, status=400)

    if start > end:
        return JsonResponse({"error": "start 不能大于 end"}, status=400)

    # 查询满足条件的数据
    all_overview = Overview.objects.filter(
        chrom=chrom,  # 确保 chrom 相等
        start__lte=end,  # start <= 参数的 end
        end__gte=start  # end >= 参数的 start
    )

    overviews = all_overview[:1000]

    # 分页设置
    page = request.GET.get('page', 1)  # 获取当前页码，默认为第 1 页
    per_page = 10  # 每页显示的数据条数

    paginator = Paginator(overviews, per_page)

    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页数据
        page = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页数据
        page = paginator.page(paginator.num_pages)

    # 构造 JSON 返回数据
    data = {
        "overview": [
            {
                "id": overview.id,
                "chrom": overview.chrom,
                "start": overview.start,
                "end": overview.end,
                "A_compartment": overview.A_compartment,
                "B_compartment" : overview.B_compartment,
                "NA_compartment": overview.NA_compartment,
                "IS_lower_bound": overview.IS_lower_bound,
                "IS_average": overview.IS_average,
                "IS_higher_bound": overview.IS_higher_bound
            }
            for overview in overviews
        ],
        "pagination": {
            "current_page": page.number,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
            "has_previous": page.has_previous(),
            "has_next": page.has_next(),
        },
    }

    return JsonResponse({"data": data})
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# from .tasks import add_random_numbers
from celery.result import AsyncResult
from .tasks import process_file

from django.core.files.storage import default_storage
import os
import datetime
from .pagination import MyPageNumberPagination
from django.db.models import Q
from celery import states

def validate_file(file):
    """验证上传的文件"""
    # 文件大小限制 (例如 50MB)
    if file.size > 50 * 1024 * 1024:
        return False, "File size exceeds 50MB limit"
    
    # 文件类型验证
    # allowed_extensions = ['.bedpe']
    # ext = os.path.splitext(file.name)[1].lower()
    # if ext not in allowed_extensions:
    #     return False, "Only .bedpe files are allowed"
    
    return True, ""

# @csrf_exempt
# def get_task_info(request, task_id):
#     try:
#         task_result = AsyncResult(task_id)
        
#         response_data = {
#             'task_id': task_id,
#             'task_status': task_result.status,
#             'percent': 0,  # 默认进度为0
#             'notation': 'Unknown status'  # 默认状态说明
#         }
        
#         if task_result.status == states.PENDING:
#             response_data.update({
#                 'percent': 0,
#                 'notation': 'Task is pending...',
#                 'current_step': 'Waiting to start'
#             })
            
#         elif task_result.status == states.SUCCESS:
#             # 从meta中获取结果信息
#             if isinstance(task_result.result, dict):
#                 response_data.update({
#                     'percent': 100,
#                     'notation': 'Task completed successfully',
#                     'results': task_result.result,
#                     'current_step': 'Completed'
#                 })
#             else:
#                 # 处理直接返回结果的情况
#                 response_data.update({
#                     'percent': 100,
#                     'notation': 'Task completed successfully',
#                     'results': {'data': task_result.result},
#                     'current_step': 'Completed'
#                 })
            
#         elif task_result.status == states.FAILURE:
#             error_msg = str(task_result.result) if task_result.result else "Unknown error occurred"
#             response_data.update({
#                 'percent': 0,
#                 'notation': f'Task failed: {error_msg}',
#                 'error': error_msg,
#                 'current_step': 'Failed'
#             })
            
#         elif task_result.status == 'PROGRESS':
#             # 处理进度信息
#             if task_result.info:
#                 meta = task_result.info
#                 response_data.update({
#                     'percent': meta.get('percent', 0),
#                     'notation': meta.get('notation', 'Processing...'),
#                     'current_step': meta.get('current_step', ''),
#                     'results': meta.get('results', None)  # 可能的中间结果
#                 })
        
#         # 添加时间戳
#         response_data['timestamp'] = datetime.datetime.now().isoformat()
        
#         return JsonResponse(response_data)
            
#     except Exception as e:
#         logger.error(f"Error in get_task_info: {str(e)}")
#         return JsonResponse({
#             'task_id': task_id,
#             'task_status': 'ERROR',
#             'error': str(e),
#             'notation': 'Internal server error',
#             'percent': 0,
#             'timestamp': datetime.datetime.now().isoformat()
#         }, status=500)
@csrf_exempt
def get_task_info(request, task_id):
    try:
        task_result = AsyncResult(task_id)
        
        response_data = {
            'task_id': task_id,
            'task_status': task_result.status,
            'timestamp': datetime.datetime.now().isoformat(),
            'percent': 0,
            'current_step': '',
            'notation': 'Task initialized'
        }
        
        if task_result.status == states.SUCCESS:
            response_data.update({
                'percent': 100,
                'current_step': 'completed',
                'notation': 'Processing completed successfully',
                'results': task_result.result
            })
        elif task_result.status == states.FAILURE:
            response_data.update({
                'percent': 0,
                'current_step': 'error',
                'notation': f'Task failed: {str(task_result.result)}',
                'error': str(task_result.result)
            })
        elif task_result.status == 'PROGRESS':
            meta = task_result.info or {}
            print(meta)
            response_data.update({
                'percent': meta.get('percent', 0),
                'current_step': meta.get('current_step', 'processing'),
                'notation': meta.get('notation', 'Processing...'),
                'intermediate_results': meta.get('intermediate_results', None)
            })
            
        return JsonResponse(response_data)
            
    except Exception as e:
        logger.error(f"Error in get_task_info: {str(e)}")
        return JsonResponse({
            'task_id': task_id,
            'task_status': 'ERROR',
            'error': str(e),
            'timestamp': datetime.datetime.now().isoformat()
        }, status=500)

@csrf_exempt
def file_upload(request):
    print('ttttttttttttttttt')
    if request.method == 'POST' and request.FILES.get('file'):
        bed_file = request.FILES['file']
        # 步骤 2.1: 创建上传目录
        now = datetime.datetime.now()
        upload_dir = f"uploads/{now.strftime('%Y/%m/%d')}"
        
        # 步骤 2.2: 确保目录存在
        if not os.path.exists('media/' + upload_dir):
            os.makedirs('media/' + upload_dir)

        os.chmod('media/' + upload_dir, 0o777)    

        # 步骤 2.3: 保存文件
        bed_file_path = os.path.join(upload_dir, bed_file.name)
        with default_storage.open(bed_file_path, 'wb+') as destination:
            for chunk in bed_file.chunks():
                destination.write(chunk)
                
        # 步骤 2.4: 获取完整文件路径
        full_bed_path = default_storage.path(bed_file_path)
        print(full_bed_path)
        print(bed_file_path)
        # return JsonResponse({'task_id': 111111}, status=202)
        # 步骤 2.5: 启动 Celery 异步任务
        task = process_file.delay(full_bed_path)
        # task = process_file.delay(1,2)

        # 步骤 2.6: 返回任务 ID
        # return 111
        return JsonResponse({'task_id': task.id}, status=202)
    else:
        return JsonResponse({'error': 'No file uploaded.'}, status=400)

# @csrf_exempt
# def file_upload(request):
#     print('ttttttttttttttttt')
#     if request.method == 'POST' and request.FILES.get('file'):
#         bed_file = request.FILES['file']
        
#         # 步骤 2.1: 创建上传目录
#         now = datetime.datetime.now()
#         upload_dir = f"uploads/{now.strftime('%Y/%m/%d')}"
        
#         # 步骤 2.2: 创建任务并获取task_id
#         task = process_file.delay('placeholder')  # 先创建任务获取ID
#         task_id = task.id
        
#         # 步骤 2.3: 创建带有task_id的子目录
#         task_dir = os.path.join(upload_dir, task_id)
#         full_task_dir = os.path.join('media', task_dir)
        
#         # 步骤 2.4: 确保目录存在并设置权限
#         if not os.path.exists(full_task_dir):
#             os.makedirs(full_task_dir)
#             os.chmod(full_task_dir, 0o777)  # 给予完全权限
            
#         # 步骤 2.5: 保存文件到task子目录
#         bed_file_path = os.path.join(task_dir, bed_file.name)
#         with default_storage.open(bed_file_path, 'wb+') as destination:
#             for chunk in bed_file.chunks():
#                 destination.write(chunk)
                
#         # 步骤 2.6: 获取完整文件路径
#         full_bed_path = default_storage.path(bed_file_path)
#         print(full_bed_path)
#         print(bed_file_path)

#         # 步骤 2.7: 重新启动带有正确文件路径的任务
#         task.revoke()  # 取消占位任务
#         task = process_file.delay(full_bed_path)

#         return JsonResponse({'task_id': task.id}, status=202)
#     else:
#         return JsonResponse({'error': 'No file uploaded.'}, status=400)
# myapp/tasks.py
from celery import shared_task
from celery import states
# import random
# import os
# import subprocess
# from celery import current_task
from celery.utils.log import get_task_logger
# import time
# import rpy2.robjects as robjects
import time
from typing import Dict, Any

logger = get_task_logger(__name__)
import os
import subprocess  # 添加这行导入

# @shared_task(bind=True)
# def process_file(self, bed_file_path):
#     print('ssssssss')
#     print(bed_file_path)
#     """
#     Fake task that reads and returns the first line of the uploaded file
#     """
#     # try:
#     # 模拟处理过程
#     total_steps = 3
    
#     # 步骤1：模拟文件读取准备
#     self.update_state(
#         state='PROGRESS',
#         meta={
#             'percent': 33,
#             'notation': 'Reading file...'
#         }
#     )
#     time.sleep(2)  # 模拟处理时间
    
#     # # 步骤2：读取文件第一行
#     self.update_state(
#         state='PROGRESS',
#         meta={
#             'percent': 66,
#             'notation': 'Processing first line...'
#         }
#     )
    
#     try:
#         with open(bed_file_path, 'r') as file:
#             first_line = file.readline().strip()
#     except Exception as e:
#         logger.error(f"Error reading file: {str(e)}")
#         raise
        
#     time.sleep(5)  # 模拟处理时间
    
#     # 步骤3：完成处理
#     result = {
#         'first_line': first_line,
#         'file_path': bed_file_path
#     }
    
#     self.update_state(
#         state='SUCCESS',
#         meta={
#             'percent': 100,
#             'notation': f'Completed! First line: {first_line}'
#         }
#     )
    
#     # return result
    
logger = get_task_logger(__name__)

# def determine_input_type(file_path: str) -> str:
#     """Determine the type of input data"""
#     try:
#         df = pd.read_csv(file_path, sep='\t', nrows=1)
#         # Add your logic to determine file type based on columns
#         if 'loop' in df.columns:
#             return 'chromatin_loops'
#         elif 'snv' in df.columns:
#             return 'SNV'
#         else:
#             return 'cis_regulatory'
#     except Exception as e:
#         logger.error(f"Error determining input type: {str(e)}")
#         return 'unknown'

@shared_task(bind=True)
def process_file(self, file_path: str) -> Dict[str, Any]:
    try:

        # 确保输出目录有正确的权限
        # output_dir = os.path.dirname(file_path)
        # os.chmod(output_dir, 0o777)  # 给予完全权限

        # Step 1: Load and determine input type
        self.update_state(
            state='PROGRESS',
            meta={
                'current_step': 'loading',
                'percent': 10,
                'notation': 'Loading input datasets...',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        )
        
        # input_type = determine_input_type(file_path)
        # element_count = 1000  # Replace with actual count
        input_type = 'bed'
        element_count = 1000
        # 构建annotation文件路径 (在others volume中)
        annotation_file = '/var/www/html/myproject/others/3d_annotation/hg38_windows_10kb.txt'
        matrix_file = '/var/www/html/myproject/others/3d_annotation/matrix2_tmp2.txt'

        # 构建输出文件路径
        output_dir = os.path.dirname(file_path)
        output_file = os.path.join(output_dir, 'overlap_results.txt')
        matrix_output_file = os.path.join(output_dir, 'matrix_data.txt')

        # 构建脚本路径
        script_path = '/var/www/html/myproject/others/3d_annotation/get_bins.sh'
        
        # 确保脚本有执行权限
        os.chmod(output_dir, 0o777)
        os.chmod(script_path, 0o777)
        
        # 执行shell脚本
        command = [script_path, file_path, annotation_file]
        
        # Step 2: Initial annotation
        self.update_state(
            state='PROGRESS',
            meta={
                'current_step': 'initial_annotation',
                'percent': 20,
                'notation': f'Start annotating {element_count} {input_type}',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        )
        # time.sleep(2)  # Replace with actual processing
        process = subprocess.run(command, 
                        capture_output=True,
                        text=True,
                        check=True)

        # 读取行号
        with open(output_file, 'r') as f:
            line_numbers = [int(line.strip()) for line in f.readlines()]
        
        # 读取用户上传的bed文件内容
        bed_regions = []
        with open(file_path, 'r') as f:
            for line in f:
                fields = line.strip().split('\t')
                bed_regions.append({
                    'chrom': fields[0],
                    'start': int(fields[1]),
                    'end': int(fields[2])
                })

        # Step 3: Compartment profile
        self.update_state(
            state='PROGRESS',
            meta={
                'current_step': 'compartment_profile',
                'percent': 40,
                'notation': 'Annotating compartment profile...',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        )
        # time.sleep(2)  # Replace with actual processing
        
        # def convert_value(x):
        #     """将字符串值转换为浮点数，处理'NA'值"""
        #     if x.strip() == 'NA':
        #         return float('nan')  # 或者用 None 或 0
        #     return float(x)

        # 从matrix2_tmp2.txt中读取数据
        header = []
        matrix_data = []
        stats = []  # 存储每行的A/B/NA统计
        
        try:
            with open(matrix_file, 'r') as f:
                # 读取表头（样本名）
                header = f.readline().strip().split('\t')
                
                # 读取所有行
                all_lines = f.readlines()
                
                # 处理选定的行
                for line_num in line_numbers:
                    if 1 <= line_num <= len(all_lines):
                        line = all_lines[line_num - 1].strip().split('\t')
                        # 统计A/B/NA的数量
                        a_count = line.count('A')
                        b_count = line.count('B')
                        na_count = line.count('NA')
                        
                        stats.append({
                            'A_count': a_count,
                            'B_count': b_count,
                            'NA_count': na_count
                        })
                        
                        matrix_data.append(line)
                        
            # 保存matrix数据到文件
            with open(matrix_output_file, 'w') as f:
                # 写入表头
                f.write('\t'.join(header) + '\n')
                # 写入数据
                for line in matrix_data:
                    f.write('\t'.join(line) + '\n')
                    
        except Exception as e:
            logger.error(f"Error reading matrix file: {str(e)}")
            raise Exception(f"Failed to process matrix data: {str(e)}")
            
        # 准备发送到前端的数据
        processed_data = []
        for i, line_num in enumerate(line_numbers):
            print(i)
            print(bed_regions)
            processed_data.append({
                'line_number': line_num,
                'bed_region': bed_regions[i],
                'statistics': stats[i],
                'data': matrix_data[i]
            })
            
        self.update_state(
            state='PROGRESS',
            meta={
                'current_step': 'compartment_profile',
                'percent': 90,
                'notation': 'Compartment profile analysis completed',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'intermediate_results': {
                    'samples': header,
                    'processed_data': processed_data[:5]  # 仅预览前5行
                }
            }
        )
        
        # 构建最终返回结果
        results = {
            'samples': header,
            'processed_data': processed_data,
            # 'matrix_output_file': matrix_output_file,
            'script_output': process.stdout,
            'file_path': file_path,
            'status': 'completed',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return results

        # # Step 4: Contact domain profile
        # self.update_state(
        #     state='PROGRESS',
        #     meta={
        #         'current_step': 'contact_domain',
        #         'percent': 60,
        #         'notation': 'Annotating contact domain profile...',
        #         'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        #     }
        # )
        # time.sleep(2)  # Replace with actual processing
        
        # # Step 5: Stripe profile
        # self.update_state(
        #     state='PROGRESS',
        #     meta={
        #         'current_step': 'stripe_profile',
        #         'percent': 80,
        #         'notation': 'Annotating stripe profile...',
        #         'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        #     }
        # )
        # time.sleep(2)  # Replace with actual processing
        
        # # Step 6: Chromatin loop profile
        # self.update_state(
        #     state='PROGRESS',
        #     meta={
        #         'current_step': 'chromatin_loop',
        #         'percent': 90,
        #         'notation': 'Annotating chromatin loop profile...',
        #         'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        #     }
        # )
        # time.sleep(2)  # Replace with actual processing
        
        # Final results
        # results = {
        #     'input_type': input_type,
        #     'element_count': element_count,
        #     'annotations': {
        #         'compartment': {'data': 'compartment_results'},
        #         'domain': {'data': 'domain_results'},
        #         'stripe': {'data': 'stripe_results'},
        #         'loop': {'data': 'loop_results'}
        #     },
        #     'summary_stats': {
        #         'total_elements': element_count,
        #         'processed_time': time.strftime('%Y-%m-%d %H:%M:%S')
        #     }
        # }
        # results = {
        #     'matrix_data': matrix_data,
        #     'script_output': process.stdout,
        #     'file_path': file_path,
        #     'annotation_file': annotation_file,
        #     'status': 'completed',
        #     'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        # }
        
        # return results
        
    except Exception as e:
        logger.error(f"Error in processing: {str(e)}")
        self.update_state(
            state=states.FAILURE,
            meta={
                'current_step': 'error',
                'percent': 0,
                'notation': f'Error occurred: {str(e)}',
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
            }
        )
        raise
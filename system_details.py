import platform
import psutil
import math
import subprocess


def get_system_details():
    heading = 'System details'
    system = {
        'Processor': platform.processor(),
        'Operating System': platform.system(),
        'OS Release': platform.release(),
        'Hostname': platform.node(),
        'Architecture': platform.machine(),
        'OS_Version': platform.version()
    }
    return {'heading': heading, 'system': system}


def get_virtual_memory_details():
    virtual_memory = psutil.virtual_memory()
    heading = 'virtual Memory details'
    system = {
        'Total RAM Size': f'{math.ceil(virtual_memory.total/(1024 ** 3))} GB',
        'Available RAM': f'{math.ceil(virtual_memory.available/(1024 ** 3))} GB',
        'Used RAM': f'{math.ceil(virtual_memory.used/(1024 ** 3))} GB',
        'RAM Usage in %': f'{virtual_memory.percent}%'
    }
    return {'heading': heading, 'system': system}


def get_disk_details():
    heading = 'Disk Space details'
    partition = '/'
    disk_usage = psutil.disk_usage(partition)
    system = {
        'Total Storage': f'{math.ceil(disk_usage.total/(1024 ** 3))} GB',
        'Available Storage': f'{math.ceil(disk_usage.used/(1024 ** 3))} GB',
        'Used Storage': f'{math.ceil(disk_usage.free/(1024 ** 3))} GB',
        'Storage Usage in %': f'{math.ceil(disk_usage.percent)}%'
    }
    return {'heading': heading, 'system': system}


def get_storage_type():
    heading = 'Storage Type'
    output = subprocess.check_output(['lsblk', '--nodeps', '--output', 'TYPE'])
    lines = output.decode().strip().split('\n')
    lines = lines[1:]
    system = {'heading': heading, 'system': 'Unknown'}
    for line in lines:
        device_type = line.strip()
        system = {
            'system': 'HDD' if device_type == 'disk' else 'SSD',
            'heading': heading
        }
    return system


get_details = {
    'get_system_details': get_system_details(),
    'get_virtual_memory_details': get_virtual_memory_details(),
    'get_disk_details': get_disk_details(),
    'get_storage_type': get_storage_type()
}

for function in get_details:
    details = get_details[function]
    print(f'\n{details["heading"]}\n{details["system"]}')





























#
#
# def get_storage_type():
#     partitions = psutil.disk_partitions(all=True)
#
#     for partition in partitions:
#         if partition.device == '/':
#             drive_type = psutil.disk(partition.device).fstype
#             if drive_type == 'ntfs':
#                 return 'HDD'
#             elif drive_type == 'ext4' or drive_type == 'apfs' or drive_type == 'exfat':
#                 return 'SSD'
#
#     return 'Unknown'
#
#
# storage_type = get_storage_type()
# print("Connected storage type:", storage_type)
#


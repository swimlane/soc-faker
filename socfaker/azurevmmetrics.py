import pendulum, random, base64, datetime, ast
import matplotlib.pyplot as plt
from io import BytesIO


__METRIC_LIST__ = {
    'percent': [
        'percentage_cpu',
        'premium_data_disk_cache_read_hit',
        'premium_data_disk_cache_read_miss',
        'premium_os_disk_cache_read_hit',
        'premium_os_disk_cache_read_miss',
    ],
    'bytes': [
        'network_in_billable_deprecated',
        'network_out_billable_deprecated',
        'disk_read_bytes',
        'disk_write_bytes',
        'network_in_total',
        'network_out_total'
    ],
    'count_per_second': [
        'disk_read_operations_sec',
        'inbound_flows_maximum_creation_rate',
        'outbound_flows_maximum_creation_rate',
        'disk_write_operations_sec',
        'os_disk_write_bytes_sec',
        'os_disk_read_operations_sec',
        'data_disk_read_bytes_sec_deprecated',
        'data_disk_write_bytes_sec_deprecated',
        'data_disk_read_operations_sec_deprecated',
        'data_disk_write_operations_sec_deprecated',
        'data_disk_read_operations_sec',
        'data_disk_write_operations_sec',
        'os_disk_read_bytes_sec',
        'os_disk_write_operations_sec'
    ],
    'count': [
        'cpu_credits_remaining',
        'cpu_credits_consumed',
        'data_disk_qd_deprecated',
        'inbound_flows',
        'outbound_flows',
        'os_disk_qd_deprecated',
        'os_disk_queue_depth',
        'data_disk_queue_depth'
    ]
}

class AzureVMMetrics(object):

    __METRICS = None
    
    def __init__(self):
        self.metric_list = []
        self.timestamp_list = []
        self.metric_dict = {}
        self.plt = plt
        self.image_list = []

    def get(self):
        if not self.__METRICS:
            metric_dict = {}
            yesterday = pendulum.yesterday()
            now = pendulum.now()
            for key, val in __METRIC_LIST__.items():
                for metric in val:
                    time_stamp = yesterday
                    timestamp_list = []
                    while time_stamp <= now:
                        total_value = None
                        if key == 'percent':
                            total_value = round(float(random.randint(0, 100)),2)
                        elif key == 'bytes':
                            total_value = round(float(random.randint(50, 10000)),2)
                        elif key == 'count_per_second':
                            total_value = round(float(random.randint(50, 1000)), 2)
                        elif key == 'count':
                            total_value = round(float(random.uniform(0.0, 1000)), 2)
                        else:
                            pass
                        time_stamp = time_stamp.add(hours=1)
                        timestamp_list.append({
                                'time_stamp': time_stamp.to_iso8601_string(),
                                'total': total_value,
                                'unit': key
                            })
                    metric_dict[metric] = timestamp_list
            self.__METRICS = metric_dict
        return self.__METRICS

    #@property
    #def average(self):
    #    from .azurevmmetricsproperties import AzureVMMetricsProperties
    #    return AzureVMMetricsProperties(self.__METRICS).get_average()#

    #@property
    ##def graphs(self):
    #    from .azurevmmetricsproperties import AzureVMMetricsProperties
    #    return AzureVMMetricsProperties(self.__METRICS).get_graphs()
        
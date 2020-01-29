import pendulum, random, cStringIO, base64, datetime, ast
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

class AzureVMMetricsProperties(object):

    def __init__(self, metrics):
        self.metrics = metrics
        self.image_list = []
       
    
    def get_average(self):
        for key,val in self.metrics.iteritems():
            count = 0
            total = 0
            for details in val:
                if 'total' in details and details['total']:
                    total += details['total']
                    count += 1
            if total is not 0 or count is not 0:
                return '{} Average is {}'.format(key, (total/count))

    def get_graphs(self):
        self.__get_data(self.metrics)
        plt.close('all')
        return self.image_list

    def __add_to_plot(self, hour_list, val, color):
        self.plt.plot(hour_list, val, color=color)

    def __generate_number_of_colors(self, count):
        return ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(count)]

    def __plot_data(self, key, val, color):
        fig = plt.figure()
        timestamp_list = []
        totals_list = []
        y_label = ''
        for details in val:          
            if 'time_stamp' in details:
                timestamp_list.append(pendulum.parse(details['time_stamp']).to_day_datetime_string())
            if 'total' in details and details['total']:
                totals_list.append(details['total'])
            y_label = details['unit']

        if len(timestamp_list) == len(totals_list):
            oldest_time = max(timestamp_list)
            latest_time = min(timestamp_list)
            plt.style.use('dark_background')
            plt.plot(timestamp_list,totals_list,'#53a8dd')
            frame1 = plt.gca()
            frame1.axes.xaxis.set_ticklabels([])
            plt.xlabel('{} - {}'.format(oldest_time,latest_time))
            plt.gcf().subplots_adjust(left=0.15)
            plt.ylabel(y_label)
            plt.title(key)
            if frame1.lines:
                tmpfile = BytesIO()
                plt.savefig(tmpfile, format='JPEG')
                self.image_list.append({
                    'attachment': {
                        'filename': '{}.jpeg'.format(key.replace('/', '_')),
                        'base64': base64.b64encode(tmpfile.getvalue()).decode('utf-8')
                    }
                })

    def __get_data(self, data):
        temp_list = []
        for key,val in data.iteritems():
            temp_list.append(key)
        colors = self.__generate_number_of_colors(len(temp_list))
        random.shuffle(colors)
        for key,val in data.iteritems():
            if 'deprecated' not in key:
                color = colors.pop()
                self.__plot_data(key, val, color)
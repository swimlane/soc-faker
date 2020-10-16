import pendulum, base64
from io import BytesIO
from .baseclass import BaseClass


class AzureVMMetricsProperties(BaseClass):

    _image_list = []

    def __init__(self, metrics):
        super(AzureVMMetricsProperties, self).__init__()
        self.metrics = metrics

    def get_average(self):
        for key,val in self.metrics.items():
            count = 0
            total = 0
            for details in val:
                if 'total' in details and details['total']:
                    total += details['total']
                    count += 1
            if total is not 0 or count is not 0:
                return '{} Average is {}'.format(key, (total/count))

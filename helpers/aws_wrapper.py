import boto3
from time import sleep
from subprocess import run
from django.conf import settings
from settings.models import S3Credential

class AWS:

    def __init__(self):
        pass

    def main(self):
        pass

    def launch(self, config):
        print('Launch Worker')

        worker = {}

        ec2 = boto3.resource('ec2', region_name=config['region_name'])
        print('Create instance')
        client = boto3.client('ec2', region_name=config['region_name'])

        response = client.request_spot_instances(
            DryRun=False,
            SpotPrice=config['spot_price'],
            InstanceCount=1,
            Type='one-time',
            LaunchSpecification={
                'ImageId': config['image_id'],
                'KeyName': config['KeyName'],
                'SubnetId': config['SubnetId'],
                'InstanceType': config['instance_type'],
                'Placement': {
                    'AvailabilityZone': config['AvailabilityZone'],
                },
                'EbsOptimized': True,
                'SecurityGroupIds': [
                    config['SecurityGroupIds'],
                ],
                'IamInstanceProfile': {
                    'Name': config['IamInstanceProfile'],
                }
            }
        )

        print(response)
        # this works!
        sir_id = response['SpotInstanceRequests'][0]['SpotInstanceRequestId']
        print(sir_id)

        fulfilled = False
        while not fulfilled:
            try:
                response = client.describe_spot_instance_requests(
                    DryRun=False,
                    SpotInstanceRequestIds=[
                        sir_id,
                    ]
                )
                # print(response)
                instance_id = response['SpotInstanceRequests'][0]['InstanceId']
                fulfilled = True
            except KeyError:
                print('Sleep 30...')
                sleep(30)
                pass

        print(instance_id)

        instance = ec2.Instance(instance_id)
        tag = instance.create_tags(
            Tags=[
                {
                    'Key': 'Name',
                    'Value': 'MendelMD Worker'
                }
            ]
        )

        instance.wait_until_running()
        print(instance.private_ip_address)
        worker = {
            'id': instance_id,
            'ip': instance.private_ip_address,
        }
        return(worker)

    def terminate(self, instance_id):
        print('Terminate Worker')
        ec2 = boto3.resource('ec2', region_name='eu-west-1')
        print('Create instance')
        client = boto3.client('ec2', region_name='eu-west-1')
        response = client.terminate_instances(
            InstanceIds=[instance_id,],
            DryRun=False
        )
        return(response)

    def install(self, ip):

        print('Install Worker')
        sleep(60)
        
        command = "scp -o StrictHostKeyChecking=no /projects/scripts/install_worker_ubuntu.sh ubuntu@%s:~/" % (ip)
        run(command, shell=True)

        #
        command = """nohup bash install_worker_ubuntu.sh >nohup.out 2>&1 & sleep 2"""
        command = """ssh -o StrictHostKeyChecking=no  -t ubuntu@%s '%s'""" % (ip, command)

        run(command, shell=True)

    def update(self,ip):

        command = "scp -o StrictHostKeyChecking=no scripts/update_worker_aws.sh ubuntu@%s:~/" % (ip)
        run(command, shell=True)

        command = """nohup bash update_worker_aws.sh >nohup.out 2>&1 & sleep 5"""
        command = """ssh -o StrictHostKeyChecking=no -t ubuntu@%s '%s'""" % (ip, command)
        
        print(command)

        run(command, shell=True)

    def upload(self,source,dest):

        dest = '{}{}/'.format(settings.UPLOAD_FOLDER, dest)

        command = 'aws s3 cp --profile {} {} {}'.format(settings.UPLOAD_FOLDER_PROFILE, source, dest)
        # print(command)
        run(command, shell=True)

    def get(self,source,task_id):

        dest = '/projects/tasks/{}/'.format(task_id)

        file_location = source.replace('s3://', '')

        s3credentials = S3Credential.objects.all()
        for cred in s3credentials:
            for bucket in cred.buckets.splitlines():
                # print(bucket)
                if file_location.startswith(bucket):
                    profile = cred.name
                    file_bucket = bucket
                    params = cred.params

        if params == None:
            params = ''
        # dest = '{}{}'.format(settings.UPLOAD_FOLDER, dest)
        command = 'aws s3 cp --profile {} {} {} {}'.format(profile, params, source.strip(), dest)
        print(command)
        run(command, shell=True)



if __name__ == '__main__':
    worker = AWS().main()
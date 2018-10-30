from __future__ import unicode_literals
import boto3

ec2 = boto3.resource('ec2',region_name='eu-central-1')
#response = ec2.describe_instances()
ec2client = boto3.client('ec2')

response = ec2client.describe_instances()
for reservation in response['Reservations']:
        try:
                for instance in reservation['Instances']:
                        print ("instance",instance['InstanceId'])
                        print (instance)
                        for tag in instance['Tags']:
                                print ("Entering the tag loop")
                                if tag['Key']=='Name':
                                        Name_value=tag['Value']
                                elif tag['Key']=='Application':
                                        Application_value=tag['Value']
                                elif tag['Key']=='Product':
                                        Product_value=tag['Value']
                                elif tag['Key']=='Environment':
                                        Environment_value=tag['Value']
                                elif tag['Key']=='CostCenter':
                                        Cost_value=tag['Value']
                                elif tag['Key']=='Team':
                                        Team_value=tag['Value']
                        for iface in instance['NetworkInterfaces']:
                                print ("Entering the NetworkInterfaces loop")
                                interfaceid = ec2.NetworkInterface(iface['NetworkInterfaceId'])
                                print (interfaceid)
                                print ("Corresponding instance tag values are",Name_value,Application_value,Product_value,Team_value,Environment_value,Cost_value)
                                interfaceid.create_tags(Tags=[{'Key':'Name','Value':Name_value},{'Key':'Application','Value':Application_value},{'Key':'Product','Value':Product_value},{'Key':'Team','Value':Team_value},{'Key':'CostCenter','Value':Cost_value},{'Key':'Environment','Value':Environment_value}])
        except Exception as e:
                print (str(e))
                pass

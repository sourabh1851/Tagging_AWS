#Tagging_AWS
###Script to tag network interfaces and volumes attached to instances
###Most of the time teams keep on provisioning the instances in AWS but forgot to tag volumes and network interfaces attached to it and then its difficult to keep track of this.


Pre-requisite:
=====

1.Python3.6 
2.EC2 instances are all tagged.In this script (i have used 6 basic tags Name,Application,CostCenter,Product,Env and Team.
3.You have permission to access instances,volumes and network interfaces.

How to use:
=====

Run Volume_Tagging.py to tag all the volumes attached to the EC2 instances.
If you want to use different tags for your environment just open python file and change the tags name.

Run Network_Interfaces_Tagging.py to tag all the ENI's attached to the EC2 instances.
If you want to use different tags for your environment just open python file and change the tags name.


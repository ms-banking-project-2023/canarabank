#lambda function to send unused volume sns notification on email
import boto3
def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    sns_client = boto3.client('sns')
    volumes = ec2_client.describe_volumes()
    sns_arn = 'arn:aws:sns:ap-south-1:211125590967:lam11'
    
    unused_vols = []
    for volume in volumes['Volumes']:
        if len(volume['Attachments']) == 0:
            unused_vols.append(volume['VolumeId'])
            print(volume)
            
    
    email_body = "##### this is Unused EBS Volumes ##### \n"
    
    for vol in unused_vols:
        email_body = email_body + f"VolumeId = {vol} \n"
       
    
    # Send Email
    
    sns_client.publish(
        TopicArn = sns_arn,
        Subject = 'Unused EBS Volumes List',
        Message = email_body
    )
    print(email_body)

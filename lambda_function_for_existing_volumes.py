import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Fetch all volumes with volume type 'gp2'
    response = ec2.describe_volumes(
        Filters=[{'Name': 'volume-type', 'Values': ['gp2']}]
    )
    gp2_volumes = response['Volumes']
    for volume in gp2_volumes:
        volume_id = volume['VolumeId']
        print(f"Converting Volume {volume_id} to gp3")
        try:
            ec2.modify_volume(
                VolumeId=volume_id,
                VolumeType='gp3'
            )
        except Exception as e:
            print(f"Failed to convert volume {volume_id}: {str(e)}")

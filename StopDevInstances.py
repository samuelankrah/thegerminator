import boto3

def stop_dev_ec2_instances():
    # Initialize a session using Amazon EC2
    session = boto3.session.Session()
    ec2 = session.resource('ec2')

    # Filtering instances with tag 'Environment' and value 'Dev'
    filters = [{
            'Name': 'tag:Environment',
            'Values': ['Dev']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]

    instances = ec2.instances.filter(Filters=filters)

    # Stopping the instances
    for instance in instances:
        instance.stop()
        print(f"Stopping instance {instance.id}")

if __name__ == "__main__":
    stop_dev_ec2_instances()

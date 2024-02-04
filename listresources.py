import boto3

def list_aws_services(region):
    print(f"\nRegion: {region}")

    # Create clients for different AWS services
    ec2_client = boto3.client('ec2', region_name=region)
    s3_client = boto3.client('s3', region_name=region)
    rds_client = boto3.client('rds', region_name=region)
    lambda_client = boto3.client('lambda', region_name=region)

    # List EC2 instances
    print("\nEC2 Instances:")
    ec2_instances = ec2_client.describe_instances()
    for reservation in ec2_instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"InstanceId: {instance['InstanceId']}, State: {instance['State']['Name']}")

    # List S3 buckets
    print("\nS3 Buckets:")
    s3_buckets = s3_client.list_buckets()
    for bucket in s3_buckets['Buckets']:
        print(f"BucketName: {bucket['Name']}")

    # List RDS instances
    print("\nRDS Instances:")
    rds_instances = rds_client.describe_db_instances()
    for rds_instance in rds_instances['DBInstances']:
        print(f"DBInstanceIdentifier: {rds_instance['DBInstanceIdentifier']}, Status: {rds_instance['DBInstanceStatus']}")

    # List Lambda functions
    print("\nLambda Functions:")
    lambda_functions = lambda_client.list_functions()
    for function in lambda_functions['Functions']:
        print(f"FunctionName: {function['FunctionName']}, Runtime: {function['Runtime']}")

def main():
    # Get available AWS regions
    regions = boto3.Session().get_available_regions('ec2')

    # Prompt user for region numbers (comma-separated)
    print("Available AWS Regions:")
    for i, region in enumerate(regions, start=1):
        print(f"{i}. {region}")

    region_choices = input("\nEnter the numbers for the AWS regions (comma-separated): ")
    selected_regions = [regions[int(choice) - 1] for choice in region_choices.split(',')]

    # Run the function for each selected region
    for region in selected_regions:
        list_aws_services(region)

if __name__ == "__main__":
    main()

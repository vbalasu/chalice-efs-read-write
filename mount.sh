# Test connectivity to EFS by mounting inside an EC2 VM

# sudo yum install -y amazon-efs-utils
# sudo mkdir /mnt/efs
# sudo mkdir /mnt/lambda

# Mount the root folder
mount -t efs fs-eb8ea768:/ /mnt/efs

# https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html#mount-with-access-point
mount -t efs -o tls,accesspoint=fsap-0aaab219669174055 fs-eb8ea768: /mnt/lambda
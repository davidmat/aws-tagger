import boto.ec2
import logging


logger = logging.getLogger('AWSTagger')
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%F %T')

conn = boto.ec2.connect_to_region("eu-west-1")

# Tag Bamboo Instances
try:
    tagging_issue_detected = False
    for instance in conn.get_only_instances():
        if 'Name' in instance.tags:
            if not 'Bill' in instance.tags:
                if instance.tags['Name'].startswith("bam:"):
                    instance.add_tag('Bill','CalmWare')
                    warningmsg = 'Elastic Bamboo instance ' + instance.id + ' now has bill tag CalmWare'
                    logger.warning(warningmsg)
                else:
                    errormsg = 'Instance ' + instance.id + ' has no Bill tag'
                    logger.error(errormsg)
                    tagging_issue_detected = True;
            else:
                infomsg = 'Instance ' + instance.id + ' has Name and Bill tags'
                logger.info((infomsg))
        else:
            if 'Bill' in instance.tags:
                errormsg = 'Instance ' + instance.id + ' has no Name tag'
            else:
                errormsg = 'Instance ' + instance.id + ' has no Name and Bill tags'
            logger.error(errormsg)
            tagging_issue_detected = True
    if tagging_issue_detected:
        raise Exception
except:
    exit(3)
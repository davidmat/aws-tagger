# AWS-Tagger

## Summary

Simple script which is run on a schedule from our CI server to tag AWS resources.

It performs two simple tasks:
- Assign autocreated Atlassian Bamboo worker instances the correct billing tag
- Fail loudly and proudly when someone "forgets" to tag their instance

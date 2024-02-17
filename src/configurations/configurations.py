import argparse
from dataclasses import dataclass
import datetime

@dataclass
class Configurations:
    groupName:str 
    startDate:datetime.datetime
    endDate:datetime.datetime


def getConfigs():
    parser = argparse.ArgumentParser(
        description="Whatsapp Group Mood Monitor"
    )

    parser.add_argument("-g", "--groupName", help="Specify the Group Name", type=str)

    parser.add_argument("-sd", "--startDate", help="Specify the start Date in the following form day-month-year", type=lambda s: datetime.datetime.strptime(s, "%d-%m-%Y"))
    parser.add_argument("-ed", "--endDate", help="Specify the end date in the following format day-month-year", type=lambda s: datetime.datetime.strptime(s, "%d-%m-%Y"))
    args = parser.parse_args()
    
    return Configurations(groupName=args.groupName, startDate=args.startDate, endDate=args.endDate)

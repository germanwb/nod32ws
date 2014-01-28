__author__ = 'german_or_jane'
import os
def check(updatever):
    for keys in updatever.keys():
        if os.path.exists('base/'+updatever[keys]['file']):
            if os.path.getsize('base/'+updatever[keys]['file']) != updatever[keys]['size']:
                print(keys+' = Ok')
            else:
                print(keys+' = err of size')
        else:
            print(keys+'err of file')

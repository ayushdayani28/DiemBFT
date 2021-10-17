import sys    

if __name__ == '__main__':
    print('In application')
    configs = [{'nreplicas':3, 'nfaultyreplicas':3, 'nclients':5,'seed':101,'timeout':4,}]
    for config in configs:      
        print('Run these configs',config)
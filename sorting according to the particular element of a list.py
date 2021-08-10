import operator
def person_lister(f):
    def inner(people):
        return map(f,sorted(people,key=lambda x:int(x[2])))
        '''for i in range(3):
            for k in range(i,3):
                if people[i][2]>people[k][2]:
                    tmp=people[i]
                    people[i]=people[k]
                    people[k]=tmp
                    '''
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print('\n'.join(name_format(people)))

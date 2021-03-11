import psutil
import random
import time

names = ['Kiran','King','John','Corey']
majors = ['Math','Comps','Science']

def login(f):
    def new_function(num_people):
        print('Memory (Before): {}'.format(psutil.virtual_memory()))
        t1 = time.process_time()
        f(num_people)
        t2 = time.process_time()
        print('Memory (After): {0}Mb'.format(psutil.virtual_memory()))
        print('Took {} Seconds'.format(t2-t1))
        
    return new_function

@login
def people_list(num_people):
    print('Lists:')
    results = []
    for i in range(num_people):
        person = {
                    'id':i,
                    'name': random.choice(names),
                    'major':random.choice(majors)
                  }
        results.append(person)
    return results

@login
def people_generator(num_people):
    print('Generators:')
    for i in range(num_people):
        person = {
                    'id':i,
                    'name': random.choice(names),
                    'major':random.choice(majors)
                  }
        yield person



people_list(10000000)
people_generator(10000000)
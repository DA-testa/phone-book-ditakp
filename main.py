from collections import defaultdict

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def hash_func(number):
    prime = 10**9 + 7
    x = 263
    return (x * number) % prime

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = defaultdict(list)
    for cur_query in queries:
        hashed_num = hash_func(cur_query.number)
        if cur_query.type == 'add':
            if cur_query.name not in contacts[hashed_num]:
                contacts[hashed_num].append(cur_query.name)
        elif cur_query.type == 'del':
            if cur_query.name in contacts[hashed_num]:
                contacts[hashed_num].remove(cur_query.name)
        else:
            names = contacts[hashed_num]
            if names:
                result.append(names[-1])
            else:
                result.append('not found')
            contacts[hashed_num] = names[:-1]
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

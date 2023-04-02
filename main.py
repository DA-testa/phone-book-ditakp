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
            if cur_query.name in contacts[hashed_num]:
                for i, entry in enumerate(contacts[hashed_num]):
                    if entry[0] == cur_query.name:
                        contacts[hashed_num][i] = (cur_query.name, cur_query.number)
                        break
            else:
                contacts[hashed_num].append((cur_query.name, cur_query.number))
        elif cur_query.type == 'del':
            for i, entry in enumerate(contacts[hashed_num]):
                if entry[1] == cur_query.number:
                    contacts[hashed_num].pop(i)
                    break
        else:
            names = [entry[0] for entry in contacts[hashed_num] if entry[1] == cur_query.number]
            if names:
                result.append(names[-1])
            else:
                result.append('not found')
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
